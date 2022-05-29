from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *

def call_book(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/P242zqu.jpg',
                    title='蝴蝶蘭',
                    text='蝴蝶蘭屬',
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=蝴蝶蘭'
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=蝴蝶蘭'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/P242zqu.jpg',
                    title='白拉索蘭',
                    text='白拉索蘭屬',
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=白拉索蘭'
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=白拉索蘭'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/P242zqu.jpg',
                    title='台灣鈴蘭',
                    text='火燒蘭屬',
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=台灣鈴蘭'
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=台灣鈴蘭'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)