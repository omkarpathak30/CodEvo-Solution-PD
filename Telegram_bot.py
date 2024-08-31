from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with the token you got from BotFather
TOKEN = 'YOUR_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    update.message.reply_text('Hello! I am your bot. Type /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    """Handle the /help command."""
    update.message.reply_text('Here is how you can use me:\n/start - Start the bot\n/help - Get help')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Register handlers for commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
