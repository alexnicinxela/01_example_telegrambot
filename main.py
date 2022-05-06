import telebot
from telebot import types
import ex_rate
import token

def main():

    bot = telebot.TeleBot(token=token.tg_token())

    @bot.message_handler(commands=['start', 'help'])
    def do_help(message):
        mess = 'Введите команду /rate, чтобы узнать курс валют'
        bot.send_message(message.chat.id, mess)

    @bot.message_handler(commands=['rate'])
    def send_rate(message):
        mess = ex_rate.get_rate()
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Перейти на сайт ЦБ РФ", url="https://cbr.ru/")
        markup.add(button1)
        bot.send_message(message.chat.id, mess, reply_markup=markup)

    @bot.message_handler(commands=['phone'])
    def use_phone(message):
        markup = types.ReplyKeyboardMarkup(row_width=3)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        btn4 = types.KeyboardButton('4')
        btn5 = types.KeyboardButton('5')
        btn6 = types.KeyboardButton('6')
        btn7 = types.KeyboardButton('7')
        btn8 = types.KeyboardButton('8')
        btn9 = types.KeyboardButton('9')
        btn10 = types.KeyboardButton('*')
        btn0 = types.KeyboardButton('0')
        btn11 = types.KeyboardButton('#')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn0, btn11)
        bot.send_message(message.chat.id, 'Введите номер', reply_markup=markup)

    bot.infinity_polling()

if __name__ == '__main__':
    main()