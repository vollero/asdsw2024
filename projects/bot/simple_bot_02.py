from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a bot.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
    bot_token = ''
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add message handler for echo functionality
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

