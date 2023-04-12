import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
import requests
from dotenv import load_dotenv
from requests.utils import requote_uri
from pyrogram import Client, filters, enums
from pyrogram.types import *

Bot = Client(
    "Google-Search-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Made By ✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""

@Client.on_message(filters.command(["app", "apps"]))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    r = requests.get(f"https://api.abirhasan.wtf/google?query={un}&page=2&limit=2").json()
    
    request = r.get(URL)
    result = r.json()
    username = result['login']
    url = result['html_url']
    name = result['name']
    company = result['company']
    bio = result['bio']
    created_at = result['created_at']
    avatar_url = result['avatar_url']
    blog = result['blog']
    location = result['location']
    repositories = result['public_repos']
    followers = result['followers']
    following = result['following']

    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
#   album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp3", "mp4")
    os.rename(file, ffile)
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
    ]]                           
    await message.reply_text(
    text=f"[{sname}]({r['data']['results'][0]['url']}) - from @nasrani_update ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
)
