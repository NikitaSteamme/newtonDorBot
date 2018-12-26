#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import json

from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from flask import Flask, request
app = Flask(__name__)

bot = TelegramBot('bot110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw')
@app.route("/telegram/", methods=['POST'])
def hello():
    message = json.loads(request.data)
    if message['message']['text'] == '/ping':
        bot.send_message(message['message']['chat']['id'], 'Pong!').wait()
    return 'ok'
