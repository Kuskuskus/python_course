from telegram.ext import Updater, CommandHandler
import ephem
import datetime

PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater('1009548683:AAGlZzwxdpoT5Dcjb-_f5OMQ-ZUeB-ik_y0', request_kwargs=PROXY)
    #mybot = Updater('1009548683:AAGlZzwxdpoT5Dcjb-_f5OMQ-ZUeB-ik_y0')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('full_moon', full_moon))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Привет! Введи планету'
    print(text)
    update.message.reply_text(text)

def planet(bot, update):
    planet = update.message.text.split()[1].capitalize()
    try:
        planet_data = getattr(ephem, planet)('22/02/2020')
        constellation = ephem.constellation(planet_data)
        update.message.reply_text(constellation[1])
    except:
        update.meassge.reply_text('Такой планеты нет')

def wordcount(bot,update):
    words = update.message.text.split()
    if not words:
        update.message.reply_text('Ты ничего не ввёл!')
    else:
        update.message.reply_text(f'{len(words) - 1} слов')

def full_moon(bot, update):
    date = datetime.datetime.today()
    next_moon = ephem.next_full_moon(date.strftime('%Y/%m/%d'))
    update.message.reply_text(f'Следующее полнолуние будет {next_moon}')

# Вызываем функцию - эта строчка собственно запускает бота
main()