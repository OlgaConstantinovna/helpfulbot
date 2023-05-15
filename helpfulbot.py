import random
import telebot
from telebot import types

game_started = False
r_number = None

token = "YOUR token"
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('регистрация')
itembtn2 = types.KeyboardButton('оповещение')
itembtn3 = types.KeyboardButton('играть')
itembtn4 = types.KeyboardButton('вычислить')
itembtn5 = types.KeyboardButton('вопрос')
markup.add(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5)
# bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Привет. Я бот помощник. Введите команду /question, чтобы задать свой вопрос")


@bot.message_handler(func=lambda message: message.text == 'вопрос')
def send_question(message):
    bot.reply_to(message, 'Введите свой вопрос и я передам его оператору')
    bot.register_next_step_handler(message, write_question)


def write_question(message):
	data = open('question.txt', 'a', encoding='utf-8')
	data.write(f'{message.from_user.id}%%{message.from_user.first_name}: {message.text}\n')
	data.close()
	bot.reply_to(message, 'Ваш вопрос отправлен оератору. Среднее время ожидания ответа 2 часа')

@bot.message_handler(commands=['start'])
def send_velcome(message):
	bot.send_message(message.from_user.id, "Привет, это снова бот",reply_markup=markup)


@bot.message_handler(commands=['регистрация'])
def send(message):
	bot.reply_to(message, "Это команда '/регистрация'")

@bot.message_handler(content_types=['text'])
def recod_text_commands(message):
    global game_started
    global r_number
    data = open('messages.txt', 'a', encoding='utf-8')
    text = f'{message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}: {message.text}'
    data.writelines(f'{text}\n')
    # bot.reply_to(message, message.text)
    if game_started:
        if message.text.isdigit():
            number = int(message.text)
            if number > r_number:
                bot.reply_to(message, 'Загаданное число меньше')
            elif number < r_number:
                bot.reply_to(message, 'Я загадал число больше')
            elif number == r_number:
                bot.reply_to(message, 'Поздравляю, ты Угадал')
            else:
              bot.reply_to(message, 'Ничего не понял')
        else:
            bot.reply_to(message, 'Я ожидал число...')
        # return

    if message.text == 'регистрация':
        our_id = str(message.from_user.id)
        data = open('reg.txt','r',encoding='utf-8')
        registration_list = data.readlines()
        data.close()
        result = ''.join(registration_list)
        if our_id in result:
            bot.reply_to(message, 'Вы уже зарегистрированы')
        else:
            data = open('reg.txt','a', encoding= 'utf-8')
            data.writelines(f'{our_id}\n')
            data.close()
            bot.reply_to(message, 'Регистрация прошла успешно')

    elif message.text == 'оповещение':
        print('оповещение работает')
        data = open('reg.txt', 'r', encoding='utf-8')
        registration_list = data.readlines()
        data.close()
        # result = ''.join(registration_list)
        for id in registration_list:
            print(id[:-1])
            bot.send_message(id[:-1], "time break")


    elif message.text == 'играть':
        if not game_started:
            game_started = True
            r_number = random.randint(1,1000)
            bot.reply_to(message, 'Я задумал число от 1 до 1000 Попробуй отгадать')
        else:
            bot.reply_to(message, 'игра уже идет')

    elif message.text == 'вычислить':
        bot.reply_to(message, 'введи выражение')
        bot.register_next_step_handler(message, calculater)

    elif message.text == 'вопрос':
        send_question(message)


def calculater(message):
    try:
        bot.reply_to(message, f'ответ: {eval(message.text)}')
    except NameError:
        bot.reply_to(message, 'вы ввели неверное выражние')


bot.infinity_polling()