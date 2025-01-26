import logging
import os
from flask import Flask, request, jsonify
from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.ext import Dispatcher

# Initialize Flask app
app = Flask(__name__)

# Retrieve the token from environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')  # Make sure the token is set in your environment variables
bot = Bot(TOKEN)

# Your webhook URL (ensure it is set correctly)
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # Example: 'https://your-vercel-app.vercel.app/webhook'

# Configure logging to monitor the bot's activity
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Set the webhook for the bot
def set_webhook():
    bot.set_webhook(url=WEBHOOK_URL)

# Function to handle incoming webhook messages
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, bot)

    # Process the update using Application's dispatcher
    dispatcher = Dispatcher(bot, None)
    dispatcher.process_update(update)

    return jsonify({'status': 'ok'}), 200  # Confirmation de réception

# /info command
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "💎 Welcome to the official Trumpee bot 💎\n\n"
        "🔥 Trumpee is a decentralized token designed to unite meme enthusiasts while offering unique opportunities in the crypto market.\n\n"
        "📊 **Information**:\n"
        "- **Symbol**: TMP\n"
        "- **Contract**: 0x438f3e402Cd1eEe3d2Fb4Fb79f7900e8DAFCbFdf\n"
        "- **Total Supply**: 1,000,000,000 TMP\n"
        "- **Official Website**: [https://trumpee.io](https://trumpee.io)\n"
        "- **Twitter**: [@tmptokens](https://x.com/TmpTokens)",
        parse_mode="Markdown"
    )

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton("/info"), KeyboardButton("/wallet")],
                  [KeyboardButton("/news"), KeyboardButton("/faq")]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await update.message.reply_text(
        "👋 Welcome! Here are the available commands:\n"
        "- /info: Information about the project\n"
        "- /news: Latest news\n"
        "- /faq: Access the FAQ\n\n"
        "- /ico: Information about our ICO\n\n"
        "Click on a command or type it directly to get started.",
        reply_markup=reply_markup
    )

# Handle new members in the group
async def handle_Message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_member = update.message.new_chat_member
    if chat_member and chat_member.status == "member":
        user_name = chat_member.user.first_name
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(f"👋 Welcome {user_name} to the Trumpee group!\n\n"
                  "Here are some useful commands you can use:\n"
                  "/info - Information about our project\n"
                  "/news - Latest news\n"
                  "/faq - Frequently Asked Questions\n"
                  "/ico - Information about our ICO\n\n"
                  "Enjoy your stay! 🚀"))

# /news command
async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📰 **Latest Trumpee News** 📰\n\n"
        "🚀 *January 31, 2025*: Official ICO Launch\n\n"
        "Stay tuned by visiting our official website: [https://trumpee.io](https://trumpee.io)\n"
        "Don't forget to follow us on [Twitter](https://x.com/TmpTokens).",
        parse_mode="Markdown"
    )

# Flask entry point to start the server
@app.route('/')
def index():
    return 'Bot is running!'

# Main function to configure and run the bot
def main():
    set_webhook()  # Set the webhook for Telegram bot

    # Initialize the bot application
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("news", news_command))

    # Run the Flask server
    app.run(debug=True, host="0.0.0.0", port=5000)  # For local testing (you can change the port)

if __name__ == "__main__":
    main()


# Exécuter le script
if __name__ == "__main__":
    main()
