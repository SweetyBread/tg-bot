#библиотеки, которые загружаем извне
import telebot
import requests
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("USD")
    item2 = types.KeyboardButton("EUR")
    item3 = types.KeyboardButton("CNY")
    item4 = types.KeyboardButton("AMD")
    item5 = types.KeyboardButton("KZT")
    item6 = types.KeyboardButton("KGS")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Привет! Я - бот для получения курсов валют. Нажмите кнопку с обозначением интересующей валюты, чтобы узнать ее текущий курс по отношению к российскому рублю.".format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)

#назначаем действия для кнопок

@bot.message_handler(content_types=['text'])

def courses(message):
    if message.chat.type == 'private':
        if message.text == 'USD':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            usd_rate = data['Valute']['USD']['Value']
            bot.send_message(message.chat.id, text=f"Курс доллара США к рублю: {usd_rate}")
        elif message.text == 'EUR':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            eur_rate = data['Valute']['EUR']['Value']
            bot.send_message(message.chat.id, text=f"Курс евро к рублю: {eur_rate}")
        elif message.text == 'CNY':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            cny_rate = data['Valute']['CNY']['Value']
            bot.send_message(message.chat.id, text=f"Курс юаня к рублю: {cny_rate}")
        elif message.text == 'AMD':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            amd_rate = data['Valute']['AMD']['Value']
            bot.send_message(message.chat.id, text=f"Курс армянского драма к рублю: {amd_rate}")
        elif message.text == 'KZT':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            kzt_rate = data['Valute']['KZT']['Value']
            bot.send_message(message.chat.id, text=f"Курс казахстанского тенге к рублю: {kzt_rate}")
        elif message.text == 'KGS':
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            kgs_rate = data['Valute']['KGS']['Value']
            bot.send_message(message.chat.id, text=f"Курс кыргыского сома к рублю: {kgs_rate}")


bot.polling(none_stop=True)