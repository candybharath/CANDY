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
    app = "**Title:** `{}`".format(result["title"])
    results = play_scraper.search(app)
    answers = []
    for result in results:
        details = "**Title:** `{}`".format(result["title"]) + "\n" \
        "**Description:** `{}`".format(result["description"]) + "\n" \
        "**App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**Developer:** `{}`".format(result["developer"]) + "\n" \
        "**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**Score:** `{}`".format(result["score"]) + "\n" \
        "**Price:** `{}`".format(result["price"]) + "\n" \
        "**Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + "Made by @FayasNoushad"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
        ) 
        try:
       
            await message.reply_text(
            text=app,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
        except Exception as error:
            print(error)
    await message.reply_text(
    text=app,
    reply_markup=reply_markup,
    disable_web_page_preview=True,
    quote=True
    )
