from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
# from pyrogram.types import CallbackQuery
import random
import os
from info import SP
from Script import script
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import BR_IMDB_TEMPLATE, LOGIN_CHANNEL, ADMINS, PROTECT_CONTENT, AUTH_CHANNEL, BATCH_LINK, IMDB_TEMPLATE
from utils import extract_user, get_file_id, get_poster, last_online
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.ia_filterdb import Media, get_file_details, get_search_results, get_bad_files
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)


Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ALL_PIC = [
 "https://telegra.ph/file/d6693066f82ed4079c528.jpg",
 "https://telegra.ph/file/65a9972e351b02640d0f4.jpg"
 ]

POST_TEMPLATE_TXT = """
<b>𝐇𝐞𝐲 𝐁𝐫𝐨 {title} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲...
🏷 𝐓𝐢𝐭𝐥𝐞 : {title}
🎭 𝐆𝐞𝐧𝐫𝐞𝐬 : {genres}
🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {rating}
☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {languages}
📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {runtime}
📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {year}
🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {countries}
<i>{title} എന്ന സിനിമ വേണമെങ്കിൽ ഇപ്പോൾ തന്നെ കാണുന്ന ബട്ടൺ ക്ലിക്ക് ചെയ്യുക..</i>
𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ©𝐍𝐚𝐬𝐫𝐚𝐧𝐢 𝐔𝐩𝐝𝐚𝐭𝐞</b>"""


POST_LINK = "http://t.me/nasrani_update"



async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False


@Client.on_message(filters.command(['post', 'channelpost']) & filters.create(allowed))            
async def start_message(client, message):    
    searchh = message.text 
# @Client.on_message(filters.private & filters.forwarded)
# async def start_message(client, message):           
    imdb = await get_poster(searchh) if IMDB else None
    

    if imdb:

        cap = POST_TEMPLATE.format(
        query=searchh,
        title=imdb['title'],
        votes=imdb['votes'],
        aka=imdb["aka"],
        seasons=imdb["seasons"],
        box_office=imdb['box_office'],
        localized_title=imdb['localized_title'],
        kind=imdb['kind'],
        imdb_id=imdb["imdb_id"],
        cast=imdb["cast"],
        runtime=imdb["runtime"],
        countries=imdb["countries"],
        certificates=imdb["certificates"],
        languages=imdb["languages"],
        director=imdb["director"],
        writer=imdb["writer"],
        producer=imdb["producer"],
        composer=imdb["composer"],
        cinematographer=imdb["cinematographer"],
        music_team=imdb["music_team"],
        distributors=imdb["distributors"],
        release_date=imdb['release_date'],
        year=imdb['year'],
        genres=imdb['genres'],
        poster=imdb['poster'],
        plot=imdb['plot'],
        rating=imdb['rating'],
        url=imdb['url'],
        **locals()

    )                           
    if imdb and imdb.get('poster'):
        try:
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('📥𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝📥', url=(POST_LINK))      
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(photo=imdb.get('poster'), caption=cap,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
                                      
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('📥𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝📥', url=(POST_LINK))           
            ]]
            hmm = await message.reply_photo(photo=poster, caption=cap,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
        except Exception as e:
            logger.exception(e)

