import os
import requests
import weasyprint
import urllib.request
# from presets import Presets
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import BOT_TOKEN, API_HASH, API_ID

# if bool(os.environ.get("ENV", False)):
#     from sample_config import Config
# else:
#     from config import Config

# -------------------------- Bot Configuration ---------------------------------------------- #
# Bot = Client(
#    "link2PdfBot",
#    bot_token=Config.TG_BOT_TOKEN,
#    api_id=Config.API_ID,
#    api_hash=Config.API_HASH,


# ------------------------------ Start Command ---------------------------------------------- #

UP_MESSAGE = """
{} {} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩
"""


# -------------------------------- Main execution fn --------------------------------------- #
@Client.on_message(filters.command("linkpdf") & filters.text)
async def link_extract(self, m: Message):
    if not m.text.startswith("http"):
        await m.reply_text(
            text=(UP_MESSAGE),
            reply_to_message_id=m.message_id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Close", callback_data="close_data")]]
            )
        )
        return
    file_name = str()
    #
    thumb_path = os.path.join(os.getcwd(), "img")
    if not os.path.isdir(thumb_path):
        os.makedirs(thumb_path)
        urllib.request.urlretrieve(https://telegra.ph/file/60706bd59c0829ed2f76f.jpg, os.path.join(thumb_path, "thumbnail.png"))
    else:
        pass
    #
    thumbnail = os.path.join(os.getcwd(), "img", "thumbnail.png")
    #
    await self.send_chat_action(m.chat.id, "typing")
    msg = await m.reply_text(text=(UP_MESSAGE), reply_to_message_id=m.message_id)
    try:
        req = requests.get(m.text)
        # using the BeautifulSoup module
        soup = BeautifulSoup(req.text, 'html.parser')
        # extracting the title frm the link
        for title in soup.find_all('title'):
            file_name = str(title.get_text()) + '.pdf'
        # Creating the pdf file
        weasyprint.HTML(m.text).write_pdf(file_name)
    except Exception:
        await msg.edit_text(
            text=(UP_MESSAGE),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Close", callback_data="close_data")]]
            )
        )
        return
    try:
        await msg.edit(text=(UP_MESSAGE))
    except Exception:
        pass
    await self.send_chat_action(m.chat.id, "upload_document")
    await m.reply_document(
        document=file_name,
        caption=text=(UP_MESSAGE),
        thumb=thumbnail
    )
    print(
        '@' + m.from_user.username if m.from_user.username else m.from_user.first_name,
        "has downloaded the file",
        file_name
    )
    try:
        os.remove(file_name)
    except Exception:
        pass
    await msg.delete()


# --------------------------------- Close Button Call Back --------------------------------- #


