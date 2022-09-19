"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)


def greet_user(update, context):
    print(text)
    update.message.reply_text('Hello, user!')
    print(update)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def get_info_planets(update, context):
    now = datetime.datetime.now()
    dt_now = now.strftime('%d.%m.%Y %H:%M')
    planets = update.message.text.split()[1]
    planets_os = getattr(ephem, planets)
    update.message.reply_text(f'{planets} сегодня ({dt_now}) находится в созвездии {ephem.constellation(planets_os(dt_now))}')


def main():
    mybot = Updater(settings.KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_info_planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
