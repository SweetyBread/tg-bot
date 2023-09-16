#библиотеки, которые загружаем извне
from telebot import TeleBot, types
import requests
from loguru import logger

TOKEN = ''

bot = TeleBot(TOKEN, parse_mode='html') # создание бота

logger.add("runtime.log", level="TRACE") # файл для записи логов

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
    
    # отправляем ответ на команду '/start'
    logger.info("bot got start command")
    bot.send_message(
            chat_id=message.chat.id,
            text='Привет! Вы используете бот для получения курсов некоторых валют по отношению к российскому рублю. Курс приведён согласно данным ЦБ РФ на сегодня. Для получения информации об указанном курсе нажмите на кнопку с обозначением интересующей Вас валюты, приведённую ниже.',
            reply_markup=markup
        ) 

#назначаем действия для кнопок

@bot.message_handler(content_types=['text'])

def courses(message):
    if message.chat.type == 'private':
        if message.text == 'USD':
            logger.info("bot got USD")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            usd_rate = data['Valute']['USD']['Value']
            bot.send_message(message.chat.id, text=f"Курс доллара США к российскому рублю: {usd_rate}")
        elif message.text == 'EUR':
            logger.info("bot got EUR")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            eur_rate = data['Valute']['EUR']['Value']
            bot.send_message(message.chat.id, text=f"Курс евро к российскому рублю: {eur_rate}")
        elif message.text == 'CNY':
            logger.info("bot got CNY")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            cny_rate = data['Valute']['CNY']['Value']
            bot.send_message(message.chat.id, text=f"Курс юаня к российскому рублю: {cny_rate}")
        elif message.text == 'AMD':
            logger.info("bot got AMD")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            amd_rate = data['Valute']['AMD']['Value']
            bot.send_message(message.chat.id, text=f"Курс армянского драма к российскому рублю: {amd_rate}")
        elif message.text == 'KZT':
            logger.info("bot got KZT")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            kzt_rate = data['Valute']['KZT']['Value']
            bot.send_message(message.chat.id, text=f"Курс казахстанского тенге к российскому рублю: {kzt_rate}")
        elif message.text == 'KGS':
            logger.info("bot got KGS")
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            kgs_rate = data['Valute']['KGS']['Value']
            bot.send_message(message.chat.id, text=f"Курс кыргызского сома к российскому рублю: {kgs_rate}")
        else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
            logger.error("got something wrong")
            bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return

# главная функция программы
def main():
    logger.trace("tracing...")
    logger.debug("debugging...")
    logger.success("bot started")
    # запускаем нашего бота
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
