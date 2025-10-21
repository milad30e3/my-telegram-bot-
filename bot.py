import os
import asyncio
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 Subscribe", url=YOUTUBE_CHANNEL)],
        [InlineKeyboardButton("✅ I Subscribed", callback_data="done")]
    ]
    await update.message.reply_text(
        "👋 Welcome to Deshi Viral Bot!\n\nPlease subscribe first 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "done":
        await query.edit_message_text("✅ Thanks for subscribing! You’re in 🎉")

# Telegram bot async runner
async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("🤖 Bot is running...")
    await app.run_polling()

# Flask app to keep Render alive
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Bot is alive and working perfectly!"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())  # Run bot asynchronously
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
