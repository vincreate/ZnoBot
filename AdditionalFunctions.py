Object = {
	"index": "0",
	"Question": "Default Question",
	"Answers": ["aa", "bb", "cc"],
	"CorrectAnswer": "bb"
}

def normalization(st):
	words = st.split("*") 
	res = Object
	res["Answers"] = []
	res["Question"] = words[0]

	if "|" in st:
		pass
	else:
		return None

	for x in range(len(words)-1):
		x += 1
		if "|" in words[x]:
			newstr = words[x].replace("|", "")
			res["Answers"].append(newstr)
			res["CorrectAnswer"] = str(x)
		else:
			res["Answers"].append(words[x])
	return res
