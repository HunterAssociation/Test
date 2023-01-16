import TgCrypto
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

bot = CLient(
      "Hunter",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)

@Client.on_message(filters.commands("start") & filters.private)
def welcome(client, m:Message):
    m.reply_text("Hi")
    
@Client.on_message(filters.text & filters.private)
def echo(client, m:Message):
    m.reply_text(message.text)
    
bot.start()
