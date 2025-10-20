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

# Run bot in a separate thread so Flask can also run
def run_bot():
    print("🤖 Bot is running...")
    app_bot.run_polling()

threading.Thread(target=run_bot).start()

# =========================
# Dummy Flask Webserver for Render Port Binding
# =========================
flask_app = Flask(__name__)
PORT = int(os.environ.get("PORT", 10000))  # Render automatically assigns this

@flask_app.route("/")
def home():
    return "Bot is alive!"

if __name__ == "__main__":
    # Bind to all interfaces
    flask_app.run(host="0.0.0.0", port=PORT)

