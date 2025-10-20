# bot.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 Subscribe", url=YOUTUBE_CHANNEL)],
        [InlineKeyboardButton("✅ I Subscribed", callback_data="done")]
    ]
    await update.message.reply_text(
        "👋 Welcome!\nSubscribe first 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "done":
        await query.edit_message_text("✅ Thanks!")

# Main
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🤖 Bot is running...")
app.run_polling()
