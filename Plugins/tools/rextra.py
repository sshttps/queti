import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
from pyrogram.types import CallbackQuery
from datetime import datetime
import random
import requests


@Client.on_message(filters.command("rextra", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text & ~filters.regex(r'^/gen regen$'))
def gen_handler(client, message):
    tiempo = time.time()
    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    yo = BIN[0:9]
    que = yo

    global input
    

    req = requests.get(
                    f"https://bins.antipublic.cc/bins/{BIN}").json()
                # capturas
    brand = req['brand']
    country = req['country']
    country_name = req['country_name']
    country_flag = req['country_flag']
    country_currencies = req['country_currencies']
    bank = req['bank']
    level = req['level']
    typea = req['type']
    que = BIN   
    #-----------FUNCION GNERADOR----------#
    hola0 = (random.randint(2024, 2030))
    hola1 = (random.randint(2024, 2030))
    hola2 = (random.randint(2024, 2030))
    hola3 = (random.randint(2024, 2030))
    hola4 = (random.randint(2024, 2030))
    hola5 = (random.randint(2024, 2030))
    hola6 = (random.randint(2024, 2030))
    hola7 = (random.randint(2024, 2030))
    hola8 = (random.randint(2024, 2030))
    hola9 = (random.randint(2024, 2030))
    si0 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si1 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si2 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si3 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si4 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si5 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si6 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si7 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si8 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si9 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    
    

    extra0 = (random.randrange(100000, 950000, 3))
    extra9 = (random.randrange(100000, 950000, 3))
    extra1 = (random.randrange(100000, 950000, 3))
    extra2 = (random.randrange(100000, 950000, 3))
    extra3 = (random.randrange(100000, 950000, 3))
    extra4 = (random.randrange(100000, 950000, 3))
    extra5 = (random.randrange(100000, 950000, 3))
    extra6 = (random.randrange(100000, 950000, 3))
    extra7 = (random.randrange(100000, 950000, 3))
    extra8 = (random.randrange(100000, 950000, 3))
    #--------PLANTILLA--------#

    message.reply(f"""<b>
あ GENERADOR DE EXTRA あ
[<code>あ</code>] BIn: <code>{BIN}</code>               
[<code>あ</code>] Banco: <code>{bank}</code> 
[<code>あ</code>] Pais: <code>{country_name}</code>
[<code>あ</code>] Datos: <code>{brand}-{typea}-{level}</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] <code>{que}{extra0}xxxx|{si0}|{hola0}|rnd</code>
[<code>あ</code>] <code>{que}{extra9}xxxx|{si1}|{hola1}|rnd</code>
[<code>あ</code>] <code>{que}{extra1}xxxx|{si2}|{hola2}|rnd</code>
[<code>あ</code>] <code>{que}{extra2}xxxx|{si3}|{hola3}|rnd</code>
[<code>あ</code>] <code>{que}{extra3}xxxx|{si4}|{hola4}|rnd</code>
[<code>あ</code>] <code>{que}{extra4}xxxx|{si5}|{hola5}|rnd</code>
[<code>あ</code>] <code>{que}{extra5}xxxx|{si6}|{hola6}|rnd</code>
[<code>あ</code>] <code>{que}{extra6}xxxx|{si7}|{hola7}|rnd</code>
[<code>あ</code>] <code>{que}{extra7}xxxx|{si8}|{hola8}|rnd</code>
[<code>あ</code>] <code>{que}{extra8}xxxx|{si9}|{hola9}|rnd</code>
- - - - - - - - - - - - - - - - - 
""")
   















