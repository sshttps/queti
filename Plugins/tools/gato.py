import json
import requests
import time
import asyncio
import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

import requests
import random

@Client.on_message(filters.command(["gato"], ["/", "."]))
async def myacc(_, m: Message):
    # Obtener una imagen aleatoria de gato
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    cat_url = r.json()[0]["url"]

    # Obtener un mensaje aleatorio sobre gatos
    messages = [
        "Los gatos son los reyes de la casa.",
        "Los gatos son los mejores compañeros de vida.",
        "Los gatos son los protectores de nuestra paz interior.",
        "Los gatos son los amos del universo.",
        "Los gatos son los maestros de la relajación.",
        "Los gatos son los reyes del amor incondicional."
    ]
    cat_message = random.choice(messages)

    # Enviar la foto y el mensaje
    await m.reply_photo(cat_url, cat_message)
