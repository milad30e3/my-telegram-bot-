from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

YOUTUBE_CHANNEL = "https://www.youtube.com/@Deshiviralvideo30"

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

BOT_TOKEN = 8243537528:AAGnVUHi8u1XB11RY9F107ssCAFIpV9FU4I

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🤖 Bot is running...")
app.run_polling()
