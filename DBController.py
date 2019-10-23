from pprint import pprint
import os.path

import pickle

Object = {
	"index": "0",
	"Question": "Default Question",
	"Answers": ["aa", "bb", "cc"],
	"CorrectAnswer": "bb"
}
#"Default Question *aa *|bb *cc"


def getQuestion():
	try:
		with open("Database/data.asc", "rb") as file:
			data_array = pickle.load(file)
		return data_array
	except Exception as e:
		print(e)
		return []




def addQuestion(obj):

	try:
		with open("Database/data.asc", "rb") as file:
			data_array = pickle.load(file)


		obj["index"] = str(len(data_array))
		data_array.append(obj)
		with open("Database/data.asc", "wb") as file:
			pickle.dump(data_array, file)

	except Exception as e:
		print(1)
		os.makedirs('Database')
		print(2)
		obj["index"] = "0"
		data_array = []
		data_array.append(obj)

		with open("Database/data.asc", "wb") as file:
			pickle.dump(data_array, file)

	return obj["index"]


