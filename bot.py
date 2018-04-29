import telebot
from telebot import types
bot = telebot.TeleBot(token)
import flask
import redis
from telebot import types
import requests
import re
from flask import request
import json
from flask import jsonify
from flask import Flask
#################################################################################################################
import os
token = os.environ['TELEGRAM_TOKEN']

server = Flask(__name__)

#################################################################################################################



def but_name(*args):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    collect_but = []
    for i in args:
        tipk = (types.KeyboardButton(i))
        collect_but.append(tipk)
    markup.add(*collect_but)
    return markup
#################################################################################################################
def set_stage(menu, mes):
    if menu == "start":
        bot.send_message(mes.chat.id, 'In case You have any questions press ➡️/help .', reply_markup=but_name('🍹Club Events', '🏖️Festivals', '💣Rave', '🏕️Private Outdoor'))

    elif menu == 'events':
        bot.send_message(mes.chat.id, "Show top events.", reply_markup=but_name ('Parnu', 'Tallinn'))

    elif menu == "festivals":
        bot.send_message(mes.chat.id, "Here are most interesting upcoming festivals.", reply_markup=but_name('⬅️Return'))

    elif menu == "rave":
        bot.send_message(mes.chat.id, "For people with steel liver and crazy mind. If You are not to experienced, be aware !", reply_markup=but_name('Sort by Style', 'Sort by Place', '⬅️Return'))

    elif menu == "private":
        bot.send_message(mes.chat.id, "The private party means that we and our partners decide can You be a member of our team or not. Private parties are made with goal to feel maximum comfortable with each other and etc. Don't be affraid to contact us, so we can send You invitation. ", reply_markup=but_name("What it's about?", "Show events", "Send invitation", '⬅️Return'))

    elif menu == "help":
        bot.send_message(mes.chat.id, "There are some inline commands for You for faster navigation:")
        bot.send_message(mes.chat.id, "/techno To open upcoming techno music events")
        bot.send_message(mes.chat.id, "/dnb To open upcoming dnb music events")
        bot.send_message(mes.chat.id, "/edm To open upcoming edm music events")

    elif menu == "parnu":
        bot.send_message(mes.chat.id, "Here are events that held in lovely Parnu town:", reply_markup=but_name('⬅️Return'))

    elif menu == "tallinn":
        bot.send_message(mes.chat.id, "Here are events that held in lovely Tallinn town:", reply_markup=but_name('⬅️Return'))

    elif menu == "show all":
        bot.send_message(mes.chat.id, "Here is list of top upcoming events:", reply_markup=but_name('⬅️Return'))

    elif menu == "sort by style":
        bot.send_message(mes.chat.id, "Pick on of those buttons", reply_markup=but_name("Techno", "Drum & Base", "EDM", "Russian pacandobl", '⬅️Return'))

    elif menu == "sort by place":
        bot.send_message(mes.chat.id, "Here are all upcoming events:", reply_markup=but_name('⬅️Return'))

    elif menu == "what it's about?":
        bot.send_message(mes.chat.id, "Private parties which are held normaly on nature, rented appartments, forest journeys and much more !", reply_markup=but_name('⬅️Return', 'Send message'))

    elif menu == "show events":
        bot.send_message(mes.chat.id, "Sorry, but this function is only allowed for people who we trust. If You think You suit to our parties, then send message to @Archie_ru", reply_markup=but_name('⬅️Return'))

    elif menu == "send invitation":
        bot.send_message(mes.chat.id, "@Archie_ru", reply_markup=but_name('⬅️Return'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Glad to see You, buddy !" )
    bot.send_message(message.chat.id, 'Got some crazy stuff to show You🤸‍♂ ! Please, pick what kind of party You are interested in.️')
    set_stage("start", message)
#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(content_types=["text"])
def sendmessage(mess):
    if mess.text == '🍹Club Events':
        set_stage("events", mess)
        bot.send_message(mess.chat.id, "Well, here are most interesting upcoming events. Just press any button where You would like to party or press Show All to see all events. ", reply_markup = but_name('Parnu ', 'Tallinn', 'Show All', '⬅️Return'))


    elif mess.text == '🏖️Festivals':
        set_stage("festivals", mess)

    elif mess.text == '💣Rave':
        set_stage('rave', mess)

    elif mess.text == '🏕️Private Outdoor':
        set_stage("private", mess)

    elif mess.text == "⬅️Return":
        set_stage("start", mess)

    elif mess.text == "/help":
        set_stage("help", mess)

    elif mess.text == "Parnu":
        set_stage("parnu", mess)

    elif mess.text == "Tallinn":
        set_stage("tallinn", mess)

    elif mess.text == "Sort by Place":
        set_stage("sort by place", mess)

    elif mess.text == "Sort by Style":
        set_stage("sort by style", mess)

    elif mess.text == "Show All":
        set_stage("show all", mess)

    elif mess.text == "What it's about?":
        set_stage("what it's about?", mess)

    elif mess.text == "Show events":
        set_stage("show events", mess)

    elif mess.text == "Send invitation":
        set_stage("send invitation", mess)





@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://seljankatest.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    try:
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    except Exception as x:
        print(x)
