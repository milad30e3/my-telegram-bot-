import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- আপনার দেওয়া তথ্য এখানে যোগ করা হয়েছে ---

# ১. আপনার বোট টোকেন
YOUR_BOT_TOKEN = "8243537528:AAGnVUHi8u1XB11RY9F107ssCAFIpV9FU4I"  

# ২. আপনার ইউটিউব চ্যানেলের লিঙ্ক
YOUR_YOUTUBE_CHANNEL_LINK = "https://www.youtube.com/@Deshiviralvideo30" 

# ৩. আপনার পাবলিক গ্রুপের লিঙ্ক
YOUR_GROUP_LINK = "https://t.me/bangladeshideshivideo"

# --------------------------------------------------
# (নিচের কোডে আর কিছু পরিবর্তন করতে হবে না)
# --------------------------------------------------

# লগিং চালু করা
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start কমান্ড দিলে এই ফাংশনটি কাজ করবে
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    keyboard = [
        [
            InlineKeyboardButton("🔔 Subscribe Now", url=YOUR_YOUTUBE_CHANNEL_LINK),
        ],
        [
            InlineKeyboardButton("✅ Done", callback_data="user_clicked_done"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(
        rf"👋 হাই {user.mention_html()}! অনুগ্রহ করে আমাদের ইউটিউব চ্যানেলে সাবস্ক্রাইব করুন এবং 'Done' বাটনে ক্লিক করুন।",
        reply_markup=reply_markup,
    )

# যখন কোনো বাটনে ক্লিক করা হবে, এই ফাংশনটি কাজ করবে
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "user_clicked_done":
        # ইউজার 'Done' ক্লিক করলেই লিঙ্কটি পেয়ে যাবে
        await query.edit_message_text(
            text=f"ধন্যবাদ! ✅\n\nএই নিন আপনার গ্রুপের লিঙ্ক:\n{YOUR_GROUP_LINK}"
        )

def main() -> None:
    """বোটটি চালু করুন।"""
    application = Application.builder().token(YOUR_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))

    print("বোট চালু হচ্ছে...")
    application.run_polling()

if __name__ == "__main__":

    main()
    from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render expects your app to bind to port 8080
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run).start()
