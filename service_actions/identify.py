from line_chatbot_api import *
import pyimgur
import pandas as pd
import os

df = pd.read_csv(os.path.join("service_actions","orchid_book.csv"), encoding = "Big5")

def get_imgur_url():
    CLIENT_ID = "4653751ffaba421"
    PATH = "static/images/temp_image.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link

def call_identify(event):
    messages=[]
    messages.append(TextSendMessage(text='請上傳一張蘭花圖片~'))
    line_bot_api.reply_message(event.reply_token, messages)

def call_identify_result(event):
    # Model 做預測
    # img path = 'static/images/temp_image.png'
    # img url = get_imgur_url()
    species = '蝴蝶蘭' 
    genus = str(df[df['species'] == species]['genus'].tolist()[0])

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=get_imgur_url(),
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


