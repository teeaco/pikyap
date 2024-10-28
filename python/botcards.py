import telebot
token="7322283656:AAEMQT40skWKrNKATIR5mMLBiqsM1Bgj3zY"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling()