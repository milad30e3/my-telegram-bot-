from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
import os
import threading

# =========================
# Bot Configuration
# =========================
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Secure token from Render Environment Variable

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
def run_bot():
    from telegram.ext import ApplicationBuilder
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot is running...")
    app_bot.run_polling()

# =========================
# Flask Web Server (for Render)
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Deshi Viral Bot is alive and running on Render!"

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    # Run Telegram Bot in background
    threading.Thread(target=run_bot, daemon=True).start()

    # Start Flask webserver for Render port binding
    PORT = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=PORT)
