from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from db.users import Users
from db.commands import Commands

users_db = Users()
updater = Updater('650043603:AAHZ3l8Nf1gcq5qwD7h6kZlk5zbclt8A6vA')
bot = updater.bot


def send_message(chat_id, msg):
    bot.send_message(chat_id=chat_id, text=msg)


def receive_message(bot, update):
    chat_id = update.message.chat_id
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    user = users_db.findBy_chatId(chat_id)

    if user is None:
        send_message(update.message.chat_id, chat_id)
    else:
        text: str = update.message.text

        if text.startswith("/"):

            if text == "/share":

                output = Commands.share(chat_id)
                send_message(chat_id, output)

            elif text == "/join":

                output = Commands.join(chat_id)
                send_message(chat_id, output)

            elif text == "/end":

                output = Commands.end(chat_id)
                send_message(chat_id, output)

            elif text == "/requestshare":

                users = Users()
                all_users = users.find_all()
                output = Commands.request_share(chat_id)

                for u in all_users:
                    if u["chatId"] == chat_id:

                        # pass
                        new_chat_id = u["chatId"]
                        send_message(new_chat_id, output)

                    else:
                        new_chat_id = u["chatId"]
                        send_message(new_chat_id, output)

            elif text == "/requestjoin":
                users = Users()
                all_users = users.find_all()
                output = Commands.request_join(chat_id)

                for u in all_users:
                    if u["chatId"] == chat_id:

                        # pass
                        new_chat_id = u["chatId"]
                        send_message(new_chat_id, output)

                    else:
                        new_chat_id = u["chatId"]
                        send_message(new_chat_id, output)

            elif text == "/status":
                output = Commands.status()
                send_message(chat_id, output)
            elif text == "/start":
                output = "Persian Pro Club"
                send_message(chat_id, output)
            else:
                send_message(chat_id, "Unrecognized command!!!")
        else:
            send_message(chat_id, "Unrecognized!!!")


receive_handler = MessageHandler(Filters.all, receive_message)
updater.dispatcher.add_handler(receive_handler)

updater.start_polling()
updater.idle()
