import logging
import os
import requests
import json
import time
import string
import random
import pyrogram

import colorama
from colorama import Fore
from colorama import Style
from faker import Faker
from bs4 import BeautifulSoup


#from datos import admin, premium

from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)










@Client.on_message(filters.command(["rand"], ["/", "."]))
async def infake(_, m: Message):
    user_id = m.from_user.id
    

    infake = m.text[len("/rand"):]
    if not infake:
        await m.reply("<b>─────────────────\nあ HERRAMIENTA | RAND あ\n─────────────────\nPara generar direcciones usa el comando <code>/paises</code> para ver la lista de los paises. despues usar <code>/rand us</code> o cualquier pais que este en la lista.</b>")
        return
        
    spli = infake.split()
    infake = spli[0]
    
   

    infake_api = requests.get(f'https://randomuser.me/api/?nat={infake}').json()

    name = infake_api["results"][0]["name"]
    gender = infake_api["results"][0]["gender"]
    age = infake_api["results"][0]["dob"]["age"]
    birthdate = infake_api["results"][0]["dob"]["date"]
    street = infake_api["results"][0]["location"]["street"]['number']
    street1 = infake_api["results"][0]["location"]["street"]['name']
        
    city = infake_api["results"][0]["location"]["city"]
    state = infake_api["results"][0]["location"]["state"]
    postal = infake_api["results"][0]["location"]["postcode"]
    email = infake_api["results"][0]["email"]
    country =infake_api["results"][0]["location"]["country"]

    edit1 = await m.reply_text("<b>あ Generando Datos, Espere unos segundo...</b>")
    await sleep(1.5)

    await edit1.edit(f"""
<b>─────────────────
あ DATOS GENERADOS - PREMIUM あ
─────────────────
[<code>あ</code>] NOMBRE: <code>{name["first"]} {name["last"]}</code>
[<code>あ</code>] GENERO: <code>{gender}</code>
[<code>あ</code>] AÑOS: <code>{age}</code>
[<code>あ</code>] PAIS: <code>{country}</code>
[<code>あ</code>] CALLE: <code>{street} {street1}</code>
[<code>あ</code>] CUIDAD: <code>{city}</code>
[<code>あ</code>] ESTADO: <code>{state}</code>
[<code>あ</code>] CODIGO POSTAL: <code>{postal}</code>
[<code>あ</code>] EMAIL: <code>{email}</code>
─────────────────
[<code>あ</code>] GENERADO POR: @{m.from_user.username}</b>""")
    
     
    
#####PAISES DISPONIBLES
@Client.on_message(filters.command(["paises"], ["/", "."]))
async def countrys(_, m: Message):
    
    edit1 = await m.reply_text("<b>あ Obteniendo Lista de Paises...</b>")
    await sleep(1.5)
    
   
    await edit1.edit(f"""
─────────────────
あ CONTAMOS CON UNA LARGA LISTA DE PAISES
─────────────────
[<code>あ</code>] AUSTRALIA: <code>/rand AU </code> 
[<code>あ</code>] BRASIL: <code>/rand BR </code>
[<code>あ</code>] CANADA: <code>/rand CA </code> 
[<code>あ</code>] SUIZA: <code>/rand CH </code>
[<code>あ</code>] ALEMANIA: <code>/rand DE </code>
[<code>あ</code>] DINAMARCA: <code>/rand DK </code>
[<code>あ</code>] ESPAÑA: <code>/rand ES </code> 
[<code>あ</code>] FINDLANDIA: <code>/rand FI </code>
[<code>あ</code>] FRANCIA: <code>/rand FR </code>
[<code>あ</code>] REINO UNIDO: <code>/rand GB </code>
[<code>あ</code>] IRLANDA: <code>/rand IE </code>
[<code>あ</code>] INDIA: <code>/rand IN </code>
[<code>あ</code>] IRAN: <code>/rand IR </code>
[<code>あ</code>] MEXICO: <code>/rand MX </code>
[<code>あ</code>] NETHERLANDS: <code>/rand NL </code>
[<code>あ</code>] NORWAY: <code>/rand NO </code>
[<code>あ</code>] HAMILTON: <code>/rand NZ </code>
[<code>あ</code>] SERVIA: <code>/rand RS </code>
[<code>あ</code>] TURQUIA: <code>/rand TR </code>
[<code>あ</code>] UKRANIA: <code>/rand UA </code>
[<code>あ</code>] ESTADOS UNIDOS: <code>/rand US </code>
─────────────────""")
    