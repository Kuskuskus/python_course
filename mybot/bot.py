from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("1009548683:AAGlZzwxdpoT5Dcjb-_f5OMQ-ZUeB-ik_y0", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

# Вызываем функцию - эта строчка собственно запускает бота
main()