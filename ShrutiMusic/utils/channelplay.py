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


from ShrutiMusic import app
from ShrutiMusic.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(_["setting_7"], show_alert=True)
            except:
                return
        try:
            channel = (await app.get_chat(chat_id)).title
        except:
            try:
                return await CallbackQuery.answer(_["cplay_4"], show_alert=True)
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel


# ©️ Copyright Reserved - @Aadishranjan  Aadish Ranjan

# ===========================================
# ©️ 2025 Aadish Ranjan (@Aadishranjan)
# 🔗 GitHub : https://github.com/Aadishranjan/BhumiMusic
# 📢 Telegram Channel : https://t.me/YutaxBots
# ===========================================


# ❤️ Love From BhumiMusic 
