from line_chatbot_api import *
# import pyimgur
import pandas as pd
import os
from flask import url_for
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import numpy as np
# import cv2
from PIL import Image   

df  = pd.read_csv(os.path.join("service_actions","orchid_book.csv"), encoding = "Big5")
df2 = pd.read_csv(os.path.join("service_actions","label_new.csv"), encoding = "Big5")

# def get_imgur_url():
#     CLIENT_ID = "4653751ffaba421"
#     PATH = "static/images/temp_image.png"
#     im = pyimgur.Imgur(CLIENT_ID)
#     uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
#     return uploaded_image.link

def call_identify(event):
    messages=[]
    messages.append(TextSendMessage(text='請上傳一張蘭花圖片!!'))
    line_bot_api.reply_message(event.reply_token, messages)

def predict(img):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = torchvision.models.resnet101(pretrained=True).to(device)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 219).to(device) # 最後一層
    model.load_state_dict(torch.load('model_acc_0.874.ckpt'))
    # model = torch.load('model.pth').to(device)

    # preprocess = transforms.Compose([
    # transforms.ToPILImage(),
    # transforms.Resize((256,256)),
    # transforms.ToTensor(),
    # ])
    preprocess = transforms.Compose([         
        transforms.RandomChoice([transforms.Resize((256,256)),
                                transforms.CenterCrop((256,256))]),
        transforms.ToTensor(),
        transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])
    img_preprocessed = preprocess(img)
    batch_img_tensor = torch.unsqueeze(img_preprocessed, 0)
    x_tensor = batch_img_tensor.to(device)

    model.eval()
    out = model(x_tensor)
    label = np.argmax(out.cpu().data.numpy(), axis=1)    

    return label


def call_identify_result(event):
    # Model 做預測
    # img=cv2.imread("static/images/temp_image.png")
    # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = Image.open("static/images/temp_image.png").convert('RGB')

    label = predict(img)
    label = label.item() # numpy iny64 to python int
    species = str(df2[df2['category'] == label]['species'].tolist()[0])
    if species == 'X':
        # 辨識到未知的品種
        messages=[]
        messages.append(StickerSendMessage(package_id=11538, sticker_id=51626532))
        messages.append(TextSendMessage(text='什麼？這樣特別的蘭花我還是第一次見到呢...再上傳別張圖片試試吧！'))
        line_bot_api.reply_message(event.reply_token, messages)
    else:
        genus = str(df[df['species'] == species]['genus'].tolist()[0])
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url=url_for('static', filename='images/temp_image.png', _external=True).replace('http://', 'https://'),
                # thumbnail_image_url=get_imgur_url(),
                title=species,
                text=genus,
                actions=[
                    PostbackAction(
                        label='品種介紹',
                        display_text='品種介紹',
                        data='action=品種介紹&item=' + species
                    ),
                    PostbackAction(
                        label='相關連結',
                        display_text='相關連結',
                        data='action=相關連結&item=' + species
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

def call_introduction(event, item):
    introduction = str(df[df['species'] == item]['introduction'].tolist()[0])
    messages=[]
    messages.append(TextSendMessage(text=item+'介紹：\n'+introduction))
    line_bot_api.reply_message(event.reply_token, messages)  

def call_related_link(event, item):
    messages=[]
    messages.append(TextSendMessage(text=item+'搜尋結果：'))
    messages.append(TextSendMessage(text=df[df['species'] == item]['related_link_0'].tolist()[0]))
    messages.append(TextSendMessage(text=df[df['species'] == item]['related_link_1'].tolist()[0]))
    messages.append(TextSendMessage(text=df[df['species'] == item]['related_link_2'].tolist()[0]))
    messages.append(TextSendMessage(text=df[df['species'] == item]['related_link_3'].tolist()[0]))
    line_bot_api.reply_message(event.reply_token, messages)


