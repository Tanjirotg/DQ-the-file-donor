import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatAction

BOT_NAME = "superman"
OWNER = "elevator"



@Client.on_message(filters.text & filters.reply)
async def chatbot(client, message: Message):
    response = requests.get(f"https://apis-tofu.koyeb.app/api/chatbot/{BOT_NAME}/{OWNER}/{message.text}")
    await message.reply_text(response)           
            
