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

- /addQuestion - add a new question in database;
- /rmQuestion - removes the last question;
- /getQ - get amount of questions stored in database;
- /getQuestion - give a link to download the database with questions;
- /sendMessage - send message in a group;
- /starttimer 10 - sets a message distribution timer for every 10 seconds (value can be changed);

Example: /addQuestion:
/addQuestion Do you study English? *|Yes *No - the question will be added to the database;

question: "Do you study English?"
аnswer1: "Yes"
аnswer2: "No"

Correct answer: аnswer1
