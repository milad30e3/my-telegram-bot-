from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from flask import Flask
import threading

# =========================
# Bot Configuration
# =========================
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"
BOT_TOKEN = "8243537528:AAGnVUHi8u1XB11RY9F107ssCAFIpV9FU4I"

# =========================
# Telegram Bot Handlers
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 Subscribe on YouTube", url=YOUTUBE_CHANNEL)],
        [InlineKeyboardButton("✅ I Subscribed", callback_data="done")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome to Deshi Viral Bot!\n\n"
        "Before using the bot, please subscribe to our YouTube channel 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "done":
        await query.edit_message_text(
            text="✅ Thanks for subscribing!\nYou now have full access to the bot 🎉"
        )

# =========================
# Start Telegram Bot
# =========================
app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))
app_bot.add_handler(CallbackQueryHandler(button))

def run_bot():
    print("🤖 Bot is running...")
    app_bot.run_polling()

# Run bot in a separate thread
threading.Thread(target=run_bot, daemon=False).start()

# =========================
# Flask app for Render
# =========================
flask_app = Flask(__name__)
PORT = int(os.environ.get("PORT", 10000))

@flask_app.route("/")
def home():
    return "Bot is alive!"

# =========================
# Remove development server warning by not using flask_app.run()
# =========================
# Flask will be served via Gunicorn in Render
# Start command in Render: gunicorn bot:flask_app --bind 0.0.0.0:$PORT


