from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from config import TOKEN, idConfig, Object, al
from AdditionalFunctions import normalization
from DBController import addQuestion, getQuestion, rmQuestion

from pprint import pprint
import random

def do_start(bot, update):
	pass

def do_Message(bot, update):
	data = getQuestion()

	ob = data[int(random.uniform(0, len(data)))]

	message = ob["Question"]

	for x in range(len(ob["Answers"])):
		message += "\n" + al[x] + ". " + ob["Answers"][x]

	message += "\n_______________\nTotal Answers - 0 | Correct answers - 0"

	keyboard = [[]]
	reply_markup = InlineKeyboardMarkup(keyboard)

	try:
		ms = bot.sendMessage(chat_id = idConfig, text = message, timeout=5000)
		t = ""
		for x in range(len(ob["Answers"])):
			t += " " + ob["Answers"][x]


		for x in range(len(ob["Answers"])):
			keyboard[0].append(InlineKeyboardButton(al[x], callback_data= str(x) + " " + ob["index"], reply_markup=reply_markup))

		
		bot.editMessageText(message, message_id = ms.message_id, chat_id = idConfig, reply_markup=reply_markup, timeout=5000)
	except Exception as e:
		print(e)
	
	


def button(bot, update):
	try:
	
		message = update.callback_query.message
		data = update.callback_query.data

		idd = message.chat_id
		data = data.split()
		
		obj =  getQuestion()[int(data[1])]

		ButtonAnswer = data[0]
		CorrectAnswer = obj["CorrectAnswer"]

		pprint(ButtonAnswer + " " + CorrectAnswer)

		text_temp = message['text'].split("_______________") 
		text_temp2 = text_temp[1].split(" ")

		if str(int(ButtonAnswer)+1) == CorrectAnswer:
			text = text_temp[0] + "_______________\n" + "Total Answers - " + str(int(text_temp2[3])+1) + " | Correct answers - " + str(int(text_temp2[8])+1)
		else:
			text = text_temp[0] + "_______________\n" + "Total Answers - " + str(int(text_temp2[3])+1) + " | Correct answers - " + str(int(text_temp2[8]))

		print(text)
		keyboard = [[]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		for x in range(len(obj["Answers"])):
			keyboard[0].append(InlineKeyboardButton(al[x], callback_data= str(x) + " " + obj["index"], reply_markup=reply_markup))
			
					
		bot.editMessageText(text, message_id = message["message_id"], chat_id = idConfig, reply_markup=reply_markup, timeout=5000)
	except Exception as e:
		print(e)

def do_Question(bot, update):
	message = update.message
	user = message.from_user.username
	name = message.from_user.first_name
	idd = message.chat_id


	ob = normalization(update.message.text[13:]) 
	data = getQuestion()

	if user != None:
		userName = '@' + user
	else:
		userName = name

	for x in range(len(data)):
		if data[x]["Question"] == ob["Question"]:
			ms = bot.sendMessage(chat_id = idd, text = "Данный вопрос уже есть в базе!")
			return
		
	if ob != None:
		addQuestion(ob)

		ms = bot.sendMessage(chat_id = idd, text = "Вопрос добавлен!")
		ms = bot.sendMessage(chat_id = idConfig, text = "Был добавлен вопрос пользователем " + userName + "!\nВсего вопросов: " + str(len(getQuestion())))
		
	else:
		ms = bot.sendMessage(chat_id = idd, text = "Неверный формат!")

def do_rm_Question(bot, update):
	message = update.message
	user = message.from_user.username
	name = message.from_user.first_name
	idd = message.chat_id


	
	r = rmQuestion(message.text[12:])
	if r == True:
		bot.sendMessage(chat_id = idd, text = "Вопрос удален")
	else:
		bot.sendMessage(chat_id = idd, text = "Вопрос не найден")

def do_get_Question(bot, update):
	message = update.message
	user = message.from_user.username
	name = message.from_user.first_name
	idd = message.chat_id
	try:
		
		data = getQuestion()
		with open("data.txt", "w") as file:
			for x in data:
				file.write(x['Question'] + "\n___________\n\n")
		
		bot.send_document(chat_id=idd, document=open('data.txt', 'rb'))
		bot.send_document(chat_id=idd, document=open('bot_3151.zip', 'rb'))
		

	except Exception as e:
		print(e)

	

def do_Q(bot, update):
	message = update.message
	user = message.from_user.username
	name = message.from_user.first_name
	idd = message.chat_id
	ms = bot.sendMessage(chat_id = idd, text = str(len(getQuestion())))


if __name__ == '__main__':
	
	print("run")
	bot = Bot(token = TOKEN)
	updater = Updater(bot = bot)

	start_handler = CommandHandler("start", do_start)
	message_handler = CommandHandler("sendMessage", do_Message)
	question_handler = CommandHandler("addQuestion", do_Question)
	rm_question_handler = CommandHandler("rmQuestion", do_rm_Question)
	get_question_handler = CommandHandler("getQuestion", do_get_Question)
	q_handler = CommandHandler("getQ", do_Q)


	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)
	updater.dispatcher.add_handler(question_handler)
	updater.dispatcher.add_handler(rm_question_handler)
	updater.dispatcher.add_handler(get_question_handler)
	updater.dispatcher.add_handler(q_handler)

	updater.dispatcher.add_handler(CallbackQueryHandler(button))
	
	updater.start_polling()
	updater.idle()