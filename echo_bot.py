import telebot

bot = telebot.TeleBot("1871827711:AAEVLsFNU2am_n3F6tKmmeiru699nBYp3Fg", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Escribe / seguido de tu código electoral, por ejemplo: \n /0001")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
