from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('yWMD8OiJyix34KbvelAmFi8EpVW1QyvZPQA5sLDocXy2KJopSzPq+rIYBNKaiL66QXEFcSvOxvIa0+JVXZzyvcTCH3uK1/2pOA8DMuo7UQl/SaNkq/zV4KEEOnCBJq+ZhZ4trJ8rWun5nyLV26+0TQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('07f8b2687ff06eddd5f94b6d7b79d98f')

@app.route("/")
def test():
    return "OK"


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f'あなたは、{event.message.text}と言いました'))


if __name__ == "__main__":
    app.run()
