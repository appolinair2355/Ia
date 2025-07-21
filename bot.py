import os
import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)
from dotenv import load_dotenv

# 🔄 Charge les variables du fichier .env
load_dotenv()

# 🔐 Récupère les tokens depuis les variables d’environnement
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Initialise la clé OpenAI
openai.api_key = OPENAI_API_KEY

# 🔰 Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue ! Envoie-moi un message pour parler avec l'IA.")

# 🤖 Fonction de réponse à chaque message utilisateur
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ✅ Modèle utilisé
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']
        await update.message.reply_text(bot_reply)
    except Exception as e:
        # 📛 Gestion d’erreur si l’API OpenAI échoue
        await update.message.reply_text("❌ Erreur : Impossible d'obtenir une réponse de l'IA.")
        print(f"Erreur OpenAI : {e}")

# 🚀 Lancement du bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
