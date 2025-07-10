from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "anon")

client = TelegramClient(session_name, api_id, api_hash)

SOURCE_CHAT = "source_channel_or_bot_username"  # без @
DEST_CHAT = "me"  # або айді чату / username

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    msg = event.message.message
    print(f"New message: {msg}")

    # Відправка в інший чат (опційно)
    await client.send_message(DEST_CHAT, msg)

client.start()
print("Bot is running...")
client.run_until_disconnected()

