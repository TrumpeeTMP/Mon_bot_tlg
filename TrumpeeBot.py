import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os
import requests

# Instancier Flask
app = Flask(__name__)
# Récupérer le token depuis les variables d'environnement
TOKEN = os.getenv('TELEGRAM_TOKEN')


# Gestion des messages dans le groupe
async def group_message(update: Update,
                        context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    if chat_id == GROUP_ID:  # Vérifiez que le message provient du bon groupe
        await context.bot.send_message(
            chat_id=chat_id, text="Merci pour votre message dans le groupe !")


# Configurer les logs pour voir ce que fait le bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


#start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton("/info"),
                   KeyboardButton("/wallet")],
                  [KeyboardButton("/news"),
                   KeyboardButton("/faq")]],
        resize_keyboard=True,
        one_time_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome! Here are the available commands:\n"
        "- /info: Information about the project\n"
        "- /news: Get the latest news\n"
        "- /faq: Access the FAQ\n\n"
        "- /ico: Information about our current ICO\n\n"
        "Click on a command or type it directly to get started.",
        reply_markup=reply_markup)


# Remplacez par votre propre token
TOKEN = os.getenv('TELEGRAM_TOKEN')

# ID de votre groupe Telegram
GROUP_ID = -1001169933388  # Remplacez par l'ID de votre groupe


# Message de bienvenue pour les nouveaux membres
async def handle_Message(update: Update,
                         context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_member = ChatMemberHandler
    if chat_member.new_chat_member and chat_member.new_chat_member.status == "member":
        user_name = chat_member.new_chat_member.user.first_name
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(f"👋 Welcome {user_name} to the Trumpee group!\n\n"
                  "Here are some useful commands you can use:\n"
                  "/info - Information about our project\n"
                  "/news - Latest news\n"
                  "/faq - Frequently Asked Questions\n"
                  "/ico - Information about our current ICO\n\n"
                  "Enjoy your stay! 🚀"))


# Fonction pour afficher les commandes disponibles via /help
async def help_command(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are the available commands:\n"
        "/info - Learn more about our project\n"
        "/news - Latest news\n"
        "/faq - View the FAQ\n"
        "/ico - Information about our current ICO\n\n"
        "Use a command by typing it into the text box! 🚀")


# Commande pour obtenir l'ID du chat
async def get_chat_id(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"L'ID de ce groupe est : {chat_id}")


# Commande /info
async def info_command(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "💎Welcome to the official Trumpee bot💎\n\n"
        "🔥 Trumpee is a decentralized token designed to unite meme enthusiasts while offering unique opportunities in the crypto market.\n\n"
        "📊 **Information**:\n"
        "- **Symbol**: TMP\n"
        "- **Contract**: 0x438f3e402Cd1eEe3d2Fb4Fb79f7900e8DAFCbFdf\n"
        "- **Total Supply**: 1,000,000,000 TMP\n"
        "- **Official Website**: [https://trumpee.io](https://trumpee.io)\n"
        "- **Twitter**: [@tmptokens](https://x.com/TmpTokens)",
        parse_mode="Markdown")


# Commande pour afficher le prix actuel du Bitcoin


# Commande /ico
async def ico_command(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🌟 **Eligibility conditions** 🌟\n\n"
        "✨🛠️ Create your Trumpee, submit it to us. If it scores higher than 7/10, we will publish it on our social media. The reward amount varies depending on the jury's score\n\n"
        "**or**\n"
        "📲 Follow the @Trumpee.io account, comment the... post, and tag two friends in the comment.\n\n"
        "Send us your Trumpees or questions at this  address : trumpee.io@gmail.com \n"
        "We will contact you through this email address for your rewards.\n\n"
        "**The rewards are displayed in the table at the bottom of the page.**\n\n"
        "(End of the I.C.O: October 10, 2025)\n\n",
        parse_mode="Markdown")


# Commande /news
async def news_command(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text((
        "📰 **Latest Trumpee News** 📰\n\n"
        "🚀 *January 31, 2025*: Official ICO Launch\n\n"
        "Stay tuned by visiting our official website: [https://trumpee.io](https://trumpee.io)\n"
        "Don't forget to follow us on [X](https://x.com/TmpTokens)."),
                                    parse_mode="Markdown")


#FAQ
async def faq_command(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📖 **FAQ - Frequently Asked Questions**📖\n\n"
        "1️⃣ **How can I get Trumpee Coins (TMP)?**\n"
        "➡️ You can get TMP during our the ICO on our official website:\n"
        "[https://trumpee.io/i-c-o](https://trumpee.io/i-c-o)\n\n"
        "2️⃣ **How can I add Trumpee to my wallet?**\n"
        "➡️🔑 Log in or create an account on Metamask\n"
        "- **Connect to BaseMainNet\n"
        "- **add the adress of token : 0x438f3e402Cd1eEe3d2Fb4Fb79f7900e8DAFCbFdf \n"
        "- **And you will see your TMP appear! ✨ \n\n"
        "4️⃣ **Where can I find the latest updates?**\n"
        "➡️ Follow us on [Twitter](https://x.com/TmpTokens) and visit our official website: [https://trumpee.io](https://trumpee.io)\n\n"
        "5️⃣ **Need additional help?**\n"
        "➡️ 📧 Contact us at trumpee.io@gmail.com 📧 \n\n"
        "💡 Type /help to see all the available commands! 🚀",
        parse_mode="Markdown")


# Fonction principale pour configurer et lancer le bot
def main():
    print("Démarrage du bot...")
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajout des gestionnaires de commandes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("getid", get_chat_id))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(CommandHandler("ico", ico_command))
    application.add_handler(CommandHandler("faq", faq_command))

    # Gestionnaire pour les nouveaux membres
    application.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_Message))

    # Gestionnaire pour les messages dans le groupe
    application.add_handler(
        MessageHandler(filters.Chat(GROUP_ID), group_message))

    print("Le bot est prêt et fonctionne...")
    application.run_polling()


# Exécuter le script
if __name__ == "__main__":
    main()