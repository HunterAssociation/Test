import TgCrypto
from pyrogram import Client, filters
from pyrogram.types import Message

bot = CLient(
      "Hunter",
      api_id=22056275,
      api_hash=5ef568ff80296900609afecbe697b87c,
      bot_token=5951991193:AAFz1fqy68ThXtiMHIOdOR6DMvWOey_kdJo
)

@Client.on_message(filters.commands("start") & filters.private)
def welcome(client, m:Message):
    m.reply_text("Hi")
    
@Client.on_message(filters.text & filters.private)
def echo(client, m:Message):
    m.reply_text(message.text)
    
bot.start()
