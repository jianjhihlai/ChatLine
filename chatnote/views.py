from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import logging
import json

from chatnote.notecost import NoteCost

logger = logging.getLogger(__name__)

print(settings.LINEMESSAGING)

line_bot_api = LineBotApi(settings.LINEMESSAGING.access_token)
handler = WebhookHandler(settings.LINEMESSAGING.secret)


# Create your views here.
def main(request):
    # get X-Line-Signature header value
    # return render(request, 'errors/variables.html', {'variables': request.META})
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        # get request body as text
        body = request.body.decode('utf-8')
        # body = json.loads(request.body)
        logger.info("Request body: " + body)

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    print(event.source)
    processor = NoteCost(event.message.text, event.source.user_id)
    reply = processor.response()
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

@handler.default()
def default(event):
    logger.info(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='不支援非文字訊息')
    )

