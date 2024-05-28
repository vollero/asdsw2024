import json
import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = '7191173703:AAHWJ2hXTdwfVdQUM7JvWQuoMcPFddC06Dw'
#os.getenv('BOT_TOKEN')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load questions from JSON file
with open('questions.json', 'r') as f:
    questions = json.load(f)

# State definitions for ConversationHandler
ASKING_QUESTION, CHECKING_ANSWER = range(2)

# User states
user_states = {}

# Start command handler
def start(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    user_states[chat_id] = {
        'current_question_index': 0,
        'score': 0
    }
    update.message.reply_text('Benvenuto al Quiz Bot! Iniziamo il quiz.')
    return ask_question(update, context)

# Function to ask a question
def ask_question(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    user_state = user_states[chat_id]
    current_question = questions[user_state['current_question_index']]
    update.message.reply_text(current_question['question'])
    return CHECKING_ANSWER

# Function to check the answer
def check_answer(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    user_state = user_states[chat_id]
    current_question = questions[user_state['current_question_index']]
    
    if update.message.text.strip().lower() == current_question['answer'].strip().lower():
        user_state['score'] += 1
        update.message.reply_text(f"Corretto! Il tuo punteggio è ora {user_state['score']}.")
    else:
        update.message.reply_text(f"Sbagliato! La risposta corretta era {current_question['answer']}.")

    user_state['current_question_index'] += 1

    if user_state['current_question_index'] < len(questions):
        return ask_question(update, context)
    else:
        update.message.reply_text(f"Quiz terminato! Il tuo punteggio finale è {user_state['score']}.")
        return ConversationHandler.END

# Function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

# Main function to start the bot
def main() -> None:
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ASKING_QUESTION: [MessageHandler(Filters.text & ~Filters.command, ask_question)],
            CHECKING_ANSWER: [MessageHandler(Filters.text & ~Filters.command, check_answer)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

