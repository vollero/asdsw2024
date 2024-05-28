from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from typing import Set
import os
import json

USERS_FILE = 'users.json'

def load_users() -> Set[int]:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return set(json.load(f))
    return set()

def save_users(users: Set[int]) -> None:
    with open(USERS_FILE, 'w') as f:
        json.dump(list(users), f)

users = load_users()

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    users.add(chat_id)
    save_users(users)
    update.message.reply_text('Hello! I am a bot.')

def echo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    users.add(chat_id)
    save_users(users)
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

def broadcast(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Usage: /broadcast <message>')
        return

    message = ' '.join(context.args)
    failed_chats = []

    for user_id in users:
        try:
            context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")
            failed_chats.append(user_id)

    for user_id in failed_chats:
        users.remove(user_id)
    save_users(users)

    update.message.reply_text('Broadcast message sent!')


def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
    bot_token = ''
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    # Add command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add message handler for echo functionality
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Add command handler for the /settimer command
    dp.add_handler(CommandHandler("settimer", settimer))

    dp.add_handler(CommandHandler("broadcast", broadcast))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

