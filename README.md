# Python Telegram ZnoBot

We are developing a telegram bot.</br> 
The sources that we are using for
adding new questions:
https://zno.osvita.ua/english/.</br>
This software developed for people
who want to test their skills in
English based on ukrainian
educational system.


Programming language - Python3

Used libraries:
- python-telegram-bot==11.1.0

<b>The following commands are implemented in our software:</b>

- /getQ - get amount of questions stored in database;
- /sendMessage - send message in a group;
- /addQuestion - add a new question in database;

Example: /addQuestion:
/addQuestion A u here? *|Yes *No *Idk - the question will be added to the database;

question: "A u here?"
аnswer1: "Yes"
аnswer2: "No"
аnswer3: "Idk"

Correct answer: аnswer2
