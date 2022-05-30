from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage, 
    ImageSendMessage, 
    StickerSendMessage, 
    LocationSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    DatetimePickerAction,
    ConfirmTemplate,
    ImageMessage
)
# Orchidentify
line_bot_api = LineBotApi('s5VEU8Kzq7CLxwcn89Z+H1lasYmzUhZcqF6V/DFM8k0vbdJN3tW9tApSGOxAqhqTJR1TxlS7hoxSuq8OtayXwjv4KHAW2FpbLF2aHntuJiW9lGlfQfrNAj1b2czucKQvF35AXrVq7aM4tHV1NlRkmwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('beb73af0d27f2b40717ef04c8589c471')


# line_bot_api = LineBotApi('iPxtsyhEhmFtA6k3xBwC2nxQ311PE5SKkCd3GxVLrEgR9jS2D0vG3N/zB7fbATv+T+bD6IalJ325lK2Cy1lRp/YjC0rHYUqu1UZL5YV+1w4aD685xy2gdKcj78z1cmwkbVzmOsQU/Wzh89O9HRnmmgdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('0b633be78db1a7d47a3a90692f3bfc2f')

# orchid_test
# line_bot_api = LineBotApi('J0n33kjIgEmQi1X1WwgkNKCgiH0vXbZKMMfxGXJWBTEgeDmwb4AfQjdc9QEEIQOTcTSZ5yujfAtkBJhS+JNA20AzSpcbNswDzMBqm6yCERgcIJitR/HfhIq22FDt0XYNXT5+HtpT2e98dWNff6Wb7QdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('d94060cbabea58f8db037b39957fb47a')