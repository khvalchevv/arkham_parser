from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "anon")

client = TelegramClient(session_name, api_id, api_hash)

SOURCE_CHAT = "ArkhamAlertBot"  # без @
TARGET_CHAT_ID = -1002604238211  # 🔁 Група, куди шлеш
TARGET_THREAD_ID = 820  # 🔁 Конкретна гілка в чаті

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_message(event):
    try:
        print(f"🔁 Пересилаю в гілку {TARGET_THREAD_ID}")
        await client.send_message(
            entity=TARGET_CHAT_ID,
            message=event.message,
            reply_to=TARGET_THREAD_ID
        )
    except Exception as e:
        print(f"❌ Error: {e}")

client.start()
print("✅ Слухаю повідомлення й пересилаю в гілку...")
client.run_until_disconnected()
