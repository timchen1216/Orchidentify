from flask import Flask, request, abort, url_for, render_template
from urllib.parse import parse_qsl, parse_qs
import random
from linebot.models import events
from line_chatbot_api import *
from service_actions.book import call_book
from service_actions.identify import call_identify
from service_actions.identify import *
from service_actions.book import *

# create flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    # print(postback_data.get('action', ''))
    # print(postback_data.get('item', '')) 
    if postback_data.get('action')=='品種介紹':
        call_introduction(event, postback_data.get('item'))
    elif postback_data.get('action')=='相關連結':
        call_related_link(event, postback_data.get('item'))


@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        # print(recrive_text)
        if '蘭花辨識' in recrive_text:
            call_identify(event)
        elif '蘭花圖鑑' in recrive_text:
            call_book(event)
    elif event.message.type=='image':
        message_content = line_bot_api.get_message_content(event.message.id)
        with open('static/images/temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        call_identify_result(event)
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)