# Copyright (c) 2025 Aadish Ranjan <Aadishranjan>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Aadish Ranjan.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User

from ShrutiMusic import app


async def extract_user(m: Message) -> User:
    if m.reply_to_message:
        return m.reply_to_message.from_user
    msg_entities = m.entities[1] if m.text.startswith("/") else m.entities[0]
    return await app.get_users(
        msg_entities.user.id
        if msg_entities.type == MessageEntityType.TEXT_MENTION
        else int(m.command[1])
        if m.command[1].isdecimal()
        else m.command[1]
    )


# ©️ Copyright Reserved - @Aadishranjan  Aadish Ranjan

# ===========================================
# ©️ 2025 Aadish Ranjan (aka @Aadishranjan)
# 🔗 GitHub : https://github.com/Aadishranjan/BhumiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From BhumiMusic 
