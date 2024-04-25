#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/K55DD   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/K55DD ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
import os
import requests
import aiohttp
import aiofiles

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from ZelzalMusic import app
from ZelzalMusic.plugins.play.filters import command

@app.on_message(command(["/tok", "تيك", "/tik"]))
async def tiktok_video(client, message):
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ التحميـل مـن تيـك تـوك . . .</b>")
    idd = message.from_user.id
    mc = message.chat.id
    url = "https://www.tikwm.com/api/?url={}".format(query)
    res = requests.get(url).json()
    video = res['data']['play']
    title = res['data']['title']
    share = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("- مشاركه .", url='https://t.me/share/url?url={}'.format(query))
        ],[
                    InlineKeyboardButton(
                        " 𝐋𝐎𝐋 𝐒𝐎𝐔𝐑𝐂𝐄🧚‍♀ ", url="https://t.me/K55DD"),
    ])
    await message.reply_video(
        video=video,
        caption='- {} .'.format(title),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• مشـاركـة •", url='https://t.me/share/url?url={}'.format(query))
                ],
            ]
        ),
    )
 
