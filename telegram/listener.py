# telegram/listener.py
from telegram import Bot, Update
from telegram.ext import MessageHandler, Filters, CallbackContext, Updater
from config import settings

def handle_new_bet(update: Update, context: CallbackContext) -> None:
    """
    Handle new bet messages from the Telegram group.
    """
    # Assuming the bet details are in the text of the message
    bet_details = update.message.text
    return bet_details

def listen_for_bets():
    """
    Set up and start the Telegram listener.
    """
    # Initialize the Updater with the TELEGRAM_API_KEY
    updater = Updater(token=settings.TELEGRAM_API_KEY)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_new_bet))

    # Start the Bot
    updater.start_polling()
    updater.idle()
