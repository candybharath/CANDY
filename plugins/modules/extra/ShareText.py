import os
from pyrogram import Client, filters
from urllib.parse import quote
# from info import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def share_link(text: str) -> str:
    return "**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(text)

@Client.on_message(filters.command(["share", "sharetext", "st", "stxt", "shtxt", "shtext"]))
async def share_text(client, message):
    text = message.text
    id = message.message_id
    reply = message.reply_to_message.message.text
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif text and (message.text or id.caption):
        input_text = message.text or id.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**")
            
            return
            await message.reply_text(share_link(input_text), reply_to_message_id=reply_id)
        
