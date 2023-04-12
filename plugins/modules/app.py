import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *




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
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
#   album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("apk", "apk")
    os.rename(file, ffile)
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
    ]]                           
    await message.reply_document(
    document=ffile, caption=f"[{sname}]({r['data']['results'][0]['url']}) - from @nasrani_update ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
)
    await message.reply_text(text="download mp3 song @nasrani_batch_store")
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()

    await client.send_message(LOG_CHANNEL, B.format(message.from_user.mention, message.from_user.id))
