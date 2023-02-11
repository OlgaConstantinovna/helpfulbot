import telebot

token = "5888104101:AAGJrGV1UH2ky0DmqkxicD-k5lixo8D1FAw"
bot = telebot.TeleBot(token)

data = open('question.txt', 'r', encoding="utf-8")
question_list = data.readlines()
data.close()