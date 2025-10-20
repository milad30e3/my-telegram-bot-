import os
import asyncio
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# =========================
# Configuration
# =========================
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Must be set in Render Environment Variables

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
            "✅ Thanks for subscribing!\nYou now have full access to the bot 🎉"
        )

# =========================
# Run Telegram Bot
# =========================
async def run_bot():
    app_bot = Application.builder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button))
    print("🤖 Bot is running...")
    await app_bot.start()
    await app_bot.updater.start_polling()
    await app_bot.updater.idle()

# =========================
# Flask Web Server (uptime)
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Deshi Viral Bot is alive and running!"

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    # Start bot in background asyncio task
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())
    
    # Start Flask web server
    PORT = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=PORT)
