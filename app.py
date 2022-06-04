from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('zAwkB7vlXWjmj8oSU//adIMh2oG7ktCcebAHlaDWdR1QWJ6bMMu9ERdG5oMp/lKh0EX+NOkYrzns22MF36+noiWJ/lTaB8iN3semFUivh81JtF1ogEdOAT6+ZAYwTOKa/if6nu1TfjRKnm8Jeo/jCAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c726c69ff252b7642f6ce9d467f9b9d3')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()