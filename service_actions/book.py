from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *
import pandas as pd
import os

df = pd.read_csv(os.path.join("service_actions","orchid_book.csv"), encoding = "Big5")

def call_book(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='蘭花圖鑑',
            text='請選擇頁數',
            actions=[
                PostbackAction(
                    label='蘭花圖鑑1',
                    display_text='蘭花圖鑑1',
                    data='action=蘭花圖鑑1&item=蘭花圖鑑1'
                ),
                PostbackAction(
                    label='蘭花圖鑑2',
                    display_text='蘭花圖鑑2',
                    data='action=蘭花圖鑑2&item=蘭花圖鑑2'
                ),
                PostbackAction(
                    label='蘭花圖鑑3',
                    display_text='蘭花圖鑑3',
                    data='action=蘭花圖鑑3&item=蘭花圖鑑3'
                ),
                PostbackAction(
                    label='蘭花圖鑑4',
                    display_text='蘭花圖鑑4',
                    data='action=蘭花圖鑑4&item=蘭花圖鑑4'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_book_one(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑1',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][0],
                    title=df['species'][0],
                    text=df['genus'][0],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][0]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][0]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][1],
                    title=df['species'][1],
                    text=df['genus'][1],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][1]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][1]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][2],
                    title=df['species'][2],
                    text=df['genus'][2],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][2]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][2]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][3],
                    title=df['species'][3],
                    text=df['genus'][3],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][3]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][3]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][4],
                    title=df['species'][4],
                    text=df['genus'][4],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][4]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][4]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][5],
                    title=df['species'][5],
                    text=df['genus'][5],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][5]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][5]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][6],
                    title=df['species'][6],
                    text=df['genus'][6],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][6]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][6]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][7],
                    title=df['species'][7],
                    text=df['genus'][7],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][7]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][7]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][8],
                    title=df['species'][8],
                    text=df['genus'][8],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][8]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][8]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][9],
                    title=df['species'][9],
                    text=df['genus'][9],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][9]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][9]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_book_two(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑1',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][10],
                    title=df['species'][10],
                    text=df['genus'][10],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][10]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][10]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][11],
                    title=df['species'][11],
                    text=df['genus'][11],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][11]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][11]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][12],
                    title=df['species'][12],
                    text=df['genus'][12],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][12]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][12]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][13],
                    title=df['species'][13],
                    text=df['genus'][13],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][13]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][13]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][14],
                    title=df['species'][14],
                    text=df['genus'][14],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][14]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][14]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][15],
                    title=df['species'][15],
                    text=df['genus'][15],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][15]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][15]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][16],
                    title=df['species'][16],
                    text=df['genus'][16],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][16]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][16]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][17],
                    title=df['species'][17],
                    text=df['genus'][17],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][17]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][17]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][18],
                    title=df['species'][18],
                    text=df['genus'][18],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][18]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][18]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][19],
                    title=df['species'][19],
                    text=df['genus'][19],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][19]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][19]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_book_three(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑1',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][20],
                    title=df['species'][20],
                    text=df['genus'][20],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][20]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][20]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][21],
                    title=df['species'][21],
                    text=df['genus'][21],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][21]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][21]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][22],
                    title=df['species'][22],
                    text=df['genus'][22],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][22]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][22]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][23],
                    title=df['species'][23],
                    text=df['genus'][23],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][23]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][23]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][24],
                    title=df['species'][24],
                    text=df['genus'][24],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][24]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][24]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][25],
                    title=df['species'][25],
                    text=df['genus'][25],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][25]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][25]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][26],
                    title=df['species'][26],
                    text=df['genus'][26],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][26]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][26]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][27],
                    title=df['species'][27],
                    text=df['genus'][27],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][27]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][27]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][28],
                    title=df['species'][28],
                    text=df['genus'][28],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][28]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][28]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][29],
                    title=df['species'][29],
                    text=df['genus'][29],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][29]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][29]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_book_four(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑1',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][30],
                    title=df['species'][30],
                    text=df['genus'][30],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][30]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][30]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][31],
                    title=df['species'][31],
                    text=df['genus'][31],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][31]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][31]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][32],
                    title=df['species'][32],
                    text=df['genus'][32],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][32]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][32]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][33],
                    title=df['species'][33],
                    text=df['genus'][33],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][33]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][33]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][34],
                    title=df['species'][34],
                    text=df['genus'][34],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][34]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][34]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][35],
                    title=df['species'][35],
                    text=df['genus'][35],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][35]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][35]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][36],
                    title=df['species'][36],
                    text=df['genus'][36],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][36]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][36]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][37],
                    title=df['species'][37],
                    text=df['genus'][37],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][37]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][37]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][38],
                    title=df['species'][38],
                    text=df['genus'][38],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][38]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][38]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][39],
                    title=df['species'][39],
                    text=df['genus'][39],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][39]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][39]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_book_five(event):
    message = TemplateSendMessage(
        alt_text='蘭花圖鑑',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][40],
                    title=df['species'][40],
                    text=df['genus'][40],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][40]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][40]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][41],
                    title=df['species'][41],
                    text=df['genus'][41],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][41]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][41]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][42],
                    title=df['species'][42],
                    text=df['genus'][42],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][42]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][42]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][43],
                    title=df['species'][43],
                    text=df['genus'][43],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][43]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][43]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][44],
                    title=df['species'][44],
                    text=df['genus'][44],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][44]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][44]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][45],
                    title=df['species'][45],
                    text=df['genus'][45],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][45]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][45]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][46],
                    title=df['species'][46],
                    text=df['genus'][46],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][46]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][46]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=df['img_url'][47],
                    title=df['species'][47],
                    text=df['genus'][47],
                    actions=[
                        PostbackAction(
                            label='品種介紹',
                            display_text='品種介紹',
                            data='action=品種介紹&item=' + df['species'][47]
                        ),
                        PostbackAction(
                            label='相關連結',
                            display_text='相關連結',
                            data='action=相關連結&item=' + df['species'][47]
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)