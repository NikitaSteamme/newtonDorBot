#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import json

from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from flask import Flask, request
app = Flask(__name__)

bot = TelegramBot('bot749857527:AAGMZgPom3lE7t_wHcxDC9YmTgRju_6Ll40')
@app.route("/telegram/", methods=['POST'])
def hello():
    message = json.loads(request.data)
    if message['message']['text'] == '/ping':
        bot.send_message(message['message']['chat']['id'], 'Pong!').wait()
    return 'ok'
