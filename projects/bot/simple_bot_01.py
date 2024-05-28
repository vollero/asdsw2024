from telegram import Bot
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Ciao, sono Campus Pizza Bot!')

def ciao(update, context):
    update.message.reply_text('Ciao!')

def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
    bot_token = ''
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ciao", ciao))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

