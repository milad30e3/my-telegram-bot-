import os
from pyrogram import Client, filters

# Your credentials
API_ID = 35535532
API_HASH = "92c8572a7c99fdf8a2585d4f7d49b875"
BOT_TOKEN = "8730894921:AAEEGan3lr3m-WA0bfJ5blGPZ7qt15kG62o"

# Initialize the Bot Client
app = Client(
    "restricted_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "Welcome! Send me a Telegram post link from a public or private group "
        "(where I am a member) to download the content."
    )

@app.on_message(filters.text & filters.private)
async def download_handler(client, message):
    link = message.text
    
    if "t.me/" not in link:
        await message.reply_text("Invalid link! Please provide a valid Telegram link.")
        return

    try:
        status_msg = await message.reply_text("Processing... Please wait.")
        
        # Extract Chat ID and Message ID from the link
        parts = link.split("/")
        message_id = int(parts[-1])
        chat_id = parts[-2]

        # Download the media
        file_path = await client.download_media(f"{chat_id}/{message_id}")
        
        if file_path:
            await client.send_document(
                message.chat.id, 
                document=file_path, 
                caption="Here is your file!"
            )
            # Delete temporary file from server after sending
            if os.path.exists(file_path):
                os.remove(file_path)
            await status_msg.delete()
        else:
            await status_msg.edit_text("Failed to download! File not found or restricted.")

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}\n\nMake sure I am a member of that group/channel.")

print("Bot is running...")
app.run()
