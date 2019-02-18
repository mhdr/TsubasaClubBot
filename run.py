from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram

users = {
    "mahmoodramzani": 86168181
}


def findBy_username(username):
    for u in users:
        if u == username:
            return users[u]

    return None


def findBy_chatId(chatId):
    for u in users:
        chat_id = users[u]

        if chat_id == chatId:
            return u

    return None


def get_message_from_command(command):
    if command == "/startshare":
        return "I want to start sharing matches"
    elif command == "/endshare":
        return "I want to end sharing matches"


def send_message(chat_id, msg):
    bot = telegram.Bot(token="795009386:AAEdLuGrzmGlJE3qdo1nXHlMFojl3mbMQLU")
    bot.send_message(chat_id=chat_id, text=msg)


def receive_message(bot, update):
    chat_id = update.message.chat_id
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    if findBy_chatId(chat_id) is None:
        bot.send_message(chat_id=update.message.chat_id, text=chat_id)
    else:
        text: str = update.message.text

        if text.startswith("/"):
            username = update.message.username
            msg = get_message_from_command(text)

            output = username + " : " + msg

            for u in users:

                if u == username:
                    # pass
                    chat_id = users[u]
                    send_message(chat_id, output)
                else:
                    chat_id = users[u]
                    send_message(chat_id, output)


updater = Updater('650043603:AAHZ3l8Nf1gcq5qwD7h6kZlk5zbclt8A6vA')

receive_handler = MessageHandler(Filters.all, receive_message)
updater.dispatcher.add_handler(receive_handler)

updater.start_polling()
updater.idle()
