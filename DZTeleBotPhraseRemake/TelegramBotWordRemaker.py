import telebot

bot = telebot.TeleBot("504524295:AAEbuKB0hgus5y0rpzXONwXajVyUIB8MsuM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "How are you?")

from pymystem3 import Mystem
import pymorphy2
import random
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
f = open('1grams-3.txt', 'r', encoding = 'utf-8')
corpfreq = f.readlines()
corpwords=[]
corp = []
lemmas =[]
tags = []
for f in corpfreq:
    p = f.split()
    corp.append(p)
for l in corp:
    corpwords.append(l[1])
for i in corpwords:
    ana = morph.parse(i)
    first = ana[0]
    lemmas.append(first.word)
    tags.append(first.tag)
allwords = dict(zip(lemmas,tags))

def get_key(d, value):
    ke = []
    for k, v in d.items():
        if v == value:
            ke.append(k)
    return ke



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    text = text.split()
    lemmassh = []
    tagssh = []
    string = []
    for i in text:
        mp = morph.parse(i)
        frt = mp[0]
        lemmassh.append(frt.normal_form)
        tagssh.append(frt.tag)
    phrase = dict(zip(lemmassh, tagssh))
    for i in lemmassh:
        p = phrase.get(i)
        ke = get_key(allwords, p)
        string.append(random.choice(ke))
    print(' '.join(string))

    bot.reply_to(message, string)

bot.polling()

