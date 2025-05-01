
import os
from telegram.ext import Updater, CommandHandler

# Access the bot token from the environment variable
TOKEN = os.getenv('BOT_TOKEN')  # This is where you access the bot token securely

# Define a start command
def start(update, context):
    update.message.reply_text("Hello! I'm your bot.")

# Set up the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the /start command handler
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
updater.idle()
