# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "你不在可以使用我的用户的列表中。",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'Hi {m.from_user.mention(style="md")} ，直接发送/转发文件，稍等片刻，机器人将会返回直链。'
    )
