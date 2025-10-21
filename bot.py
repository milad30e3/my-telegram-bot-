from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
import os
import threading
import asyncio 

# =========================
# Bot Configuration
# =========================
BOT_TOKEN = os.environ["BOT_TOKEN"]   # <- Set this in Render Environment
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"

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
        "👋 Welcome to Deshi Viral Bot!\nSubscribe first 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "done":
        await query.edit_message_text("✅ Thanks for subscribing!")

# =========================
# Run Telegram Bot (Error Fixed)
# =========================
def run_bot():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button))
    
    print("🤖 Bot is running...")
    
    # Fix: Run polling inside a new asyncio event loop
    try:
        asyncio.run(app_bot.run_polling())
    except RuntimeError as e:
        print(f"Error running bot: {e}")

# =========================
# Flask Webserver for uptime
# =========================
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Bot is alive!"

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    # Start bot in background
    threading.Thread(target=run_bot, daemon=True).start()

    # Start Flask webserver for Render port binding
    PORT = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=PORT)
