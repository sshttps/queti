from pyrogram.types import Message, InlineKeyboardButton
from pyrogram import enums
from typing import Union
from datetime import datetime
import time
from datetime import datetime

spam_times = {}


def anti_spam(message, time_limit):
    chat_id = message.chat.id
    message_id = message.message_id
    if chat_id in spam_times:
        elapsed_time = time.time() - spam_times[chat_id]["time"]
        if elapsed_time < time_limit:
            return False
    spam_times[chat_id] = {
        "message_id": message_id,
        "time": time.time()
    }
    return True