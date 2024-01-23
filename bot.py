import telebot

token = "6916676016:AAH7515gDmUBVoGzOVLpsU0dTKCQkePegro"
bot = telebot.TeleBot(token, parse_mode = None)

def send_convers(mes):
    #bot.send_message('990404868', mes)
    print("Отсчет отправил")


if __name__ == '__main__':
    bot.polling(non_stop=True)
