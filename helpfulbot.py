import telebot

token = "5888104101:AAGJrGV1UH2ky0DmqkxicD-k5lixo8D1FAw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет. Я бот техподдержки. Введите команду /question, чтобы задать свой вопрос")

@bot.message_handler(commands=['question'])   
def prepare_to_question(message):
    bot.reply_to(message, 'Задайте свой вопрос 1 сообщением я предам его опретору')
    bot.register_next_step_handler(message,write_question)

def write_question(message):
	data = open('question.txt', 'a', encoding='utf-8')
	data.write(f'{message.from_user.id}--{message.from_user.first_name}: {message.text}\n')
	data.close()
	bot.reply_to(message, 'Ваш вопрос отправлен оератору. Среднее время ожидания ответа 2 часа')


bot.infinity_polling()