from line_chatbot_api import *
import pyimgur
import pandas as pd
import os
from googlesearch import search

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
    species = '白拉索蘭' 
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
    link_list = get_related_link(item)
    messages=[]
    messages.append(TextSendMessage(text=item+'搜尋結果：'))
    messages.append(TextSendMessage(text=link_list[0]))
    messages.append(TextSendMessage(text=link_list[1]))
    messages.append(TextSendMessage(text=link_list[2]))
    messages.append(TextSendMessage(text=link_list[3]))
    line_bot_api.reply_message(event.reply_token, messages)

def get_related_link(query):
    link_list = []
    for j in search(query, stop=4, pause=2.0): 
        link_list.append(j)
    return link_list
