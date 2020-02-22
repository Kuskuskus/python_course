from telegram.ext import Updater, CommandHandler
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("1009548683:AAGlZzwxdpoT5Dcjb-_f5OMQ-ZUeB-ik_y0", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
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

# Вызываем функцию - эта строчка собственно запускает бота
main()