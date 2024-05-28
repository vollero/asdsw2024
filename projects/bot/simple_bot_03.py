from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a bot.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def timer_callback(context: CallbackContext) -> None:
    job = context.job
    context.bot.send_message(job.context['chat_id'], text=job.context['message'])

def settimer(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id

    try:
        # Parse the timer duration (in seconds) and the message from the command arguments
        due = int(context.args[0])
        message = ' '.join(context.args[1:])

        # Add a new job to the job queue
        context.job_queue.run_once(timer_callback, due, context={'chat_id': chat_id, 'message': message})

        update.message.reply_text(f'Timer set for {due} seconds.')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /settimer <seconds> <message>')


def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
    bot_token = '7191173703:AAHWJ2hXTdwfVdQUM7JvWQuoMcPFddC06Dw'
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add message handler for echo functionality
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Add command handler for the /settimer command
    dp.add_handler(CommandHandler("settimer", settimer))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

