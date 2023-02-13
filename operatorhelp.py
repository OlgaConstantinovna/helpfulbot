import telebot

def send_answer(id, question, answer):
    bot.send_message(id, f'{question}\nОтвет: {answer}')

token = "5888104101:AAGJrGV1UH2ky0DmqkxicD-k5lixo8D1FAw"
bot = telebot.TeleBot(token)

data = open('question.txt', mode='r', encoding="utf-8")
question_list = data.readlines()
data.close()

answer_question = []
for row in question_list:
    split_row = row.split('%%')
    id = split_row[0]
    question = split_row[1]
    print(question[:-1])
    answer = input('Введите ответ: ')
    if answer != 'пропустить':
        answer_question.append(row)
        send_answer(id, question, answer)
    print('_________________________________')    

for ans in answer_question:
    question_list.remove(ans)


data = open('question.txt', mode='w', encoding="utf-8")
data.writelines(question_list)
data.close()    