# Python Telegram ZnoBot

We are developing a telegram bot.
The sources that we are using for 
adding new questions: 
https://zno.osvita.ua/english/
This software developed for people
who want to test their skills in
English based on ukrainian educational
system.

Programming language - Python3

Used libraries:
- python-telegram-bot==11.1.0

<b>The following commands are implemented in our software:

- /getQ - получить количество вопросов в БД
- /sendMessage - Отправить сообщение в группу
- /addQuestion - Добавить вопрос в БД

Пример использования команды /addQuestion:
/addQuestion Test Question *Answer1 *|Answer2 *Answer3 - В БД будет добавлена такая запись
Вопрос: "Test Question"
Ответ1: "Answer1"
Ответ2: "Answer2"
Ответ2: "Answer2"
Правильный ответ: Ответ2
