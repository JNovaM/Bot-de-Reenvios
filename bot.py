import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "" #aqui el token
hashtag = '' #aqui el hastag Ejemplo: #compartir
channel = '' #aqui el canal


def start(update, context):
    update.message.reply_text("Bot funcionando")


def scan(update, context):
    if not update.effective_user['first_name'] == 'Telegram':

        if str(update.message.caption).startswith(hashtag):
            context.bot.forward_message(
                chat_id=channel, from_chat_id=update.message.chat.id, message_id=update.message.message_id)

        if str(update.message.text).startswith(hashtag):
            context.bot.forward_message(
                chat_id=channel, from_chat_id=update.message.chat.id, message_id=update.message.message_id)


if __name__ == "__main__":
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(bot.token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        filters=Filters.all, callback=scan))
    updater.start_polling()
    updater.idle
