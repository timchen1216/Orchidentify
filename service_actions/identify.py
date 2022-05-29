from urllib.parse import parse_qsl, parse_qs
import datetime, random, json
from flask import url_for
from linebot.models import messages
from line_chatbot_api import *
import pyimgur
import pandas as pd

df = pd.read_csv("label_new.csv", encoding = "Big5")
cat = str(df[df['category'] == 4]['species'].tolist()[0])

def get_imgur_url():
    CLIENT_ID = "4653751ffaba421"
    PATH = "static/images/temp_image.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link

def call_identify(event):
    messages=[]
    messages.append(TextSendMessage(text='請上傳一張蘭花圖片：)'))
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
    #get item introduction
    messages=[]
    messages.append(TextSendMessage(text=item+'介紹：\n蝴蝶蘭是台灣的原生蘭花，其美麗的外表也帶來嚴重的人為採集，在台灣紅皮書內被列為極危等級。過去，蝴蝶蘭被歸類為Phalaenopsis amabilis，由於種名amabilis的前兩音節唸起來像「阿嬤」，故有「台灣阿嬤」之別稱。'))
    line_bot_api.reply_message(event.reply_token, messages)  

def call_related_link(event, item):
    #get item link
    messages=[]
    messages.append(TextSendMessage(text=item+'搜尋結果：\nhttps://www.google.com/search?q=%E8%9D%B4%E8%9D%B6%E8%98%AD&sxsrf=ALiCzsagktDaOea84LFzC0YxNIWf6u5fpQ%3A1653380200944&source=hp&ei=aJSMYuiVN4GJoATD8o-4BA&iflsig=AJiK0e8AAAAAYoyieLi8N8kPpJ1vS3Pty4rxBgsgI02P&ved=0ahUKEwjo6bac2ff3AhWBBIgKHUP5A0cQ4dUDCAk&uact=5&oq=%E8%9D%B4%E8%9D%B6%E8%98%AD&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhD7ATIECCMQJzIECCMQJzIFCC4QgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6CwgAEIAEELEDEIMBOgQIABADOgQILhADOggILhCABBCxAzoICAAQgAQQsQM6CwguEIAEELEDEIMBOgsILhCABBCxAxDUAjoICC4QsQMQgwE6BwguENQCEEM6DAgjELACECcQRhD7AToHCCMQsAIQJzoNCC4QsQMQgwEQ1AIQDToECAAQDToKCAAQsQMQgwEQDToHCC4QsQMQDToFCAAQogRQlRFY5R5gqSFoAnAAeACAAViIAc8EkgECMTGYAQCgAQGwAQo&sclient=gws-wiz'))
    line_bot_api.reply_message(event.reply_token, messages)
