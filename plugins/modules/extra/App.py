# (c) @KoshikKumar17
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Made By ✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""

@Client.on_message(filters.command(["app", "apps"]))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    args = message.text.split(None, 1)[1]
    
    URL = f"https://play.google.com/search/{args}"
    results = play_scraper.search(URL)
    for result in results:
        result = URL.json()
        username = result['title']
        url = result['title']
    
        capy = f"""**Info Of {name}**
    **Username:** `{username}`
    **Profile Link:** [Click Here]({url})

    **@kinzanoufal**"""
        await message.reply_photo(photo=avatar_url, caption=capy, reply_markup=BUTTONS)
        await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
        await k.delete()
