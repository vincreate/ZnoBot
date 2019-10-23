from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from config import TOKEN, idConfig, Object, al
from AdditionalFunctions import normalization
from DBController import addQuestion, getQuestion

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


def do_Question(bot, update):
	message = update.message
	user = message.from_user.username
	name = message.from_user.first_name
	idd = message.chat_id


	ob = normalization(update.message.text[13:]) 
	data = getQuestion()

	for x in range(len(data)):
		if data[x]["Question"] == ob["Question"]:
			ms = bot.sendMessage(chat_id = idd, text = "Данный вопрос уже есть в базе!")
			return
		
	if ob != None:
		addQuestion(ob)
		ms = bot.sendMessage(chat_id = idd, text = "Вопрос добавлен!")
	else:
		ms = bot.sendMessage(chat_id = idd, text = "Неверный формат!")

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
	q_handler = CommandHandler("getQ", do_Q)


	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)
	updater.dispatcher.add_handler(question_handler)
	updater.dispatcher.add_handler(q_handler)

	updater.dispatcher.add_handler(CallbackQueryHandler(button))
	
	updater.start_polling()
	updater.idle()