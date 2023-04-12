import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *

Bot = Client(
    "Play-Store-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)



@Client.on_message(filters.command('app') & filters.text)
async def video(client, message): 
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/svideo requires an argument.")
    if args.startswith(" "):
        await message.reply("/svideo requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://play.google.com?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    r = requests.get(f"https://play.google.com?query={args}&page=2&limit=2").json()
    details = "**Title:** `{}`".format(result["title"]) + "\n" \
    "**App ID:** `{}`".format(result["app_id"]) + "\n" \
    
    "\n" + "Made by @FayasNoushad"
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
    )
    await message.reply_text(text="download mp3 song @nasrani_batch_store")
    
    await pak.delete()

    await client.send_message(LOG_CHANNEL, B.format(message.from_user.mention, message.from_user.id))
