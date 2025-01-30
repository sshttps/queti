import os
import requests
import random
from io import BytesIO
import time
from pyrogram import Client, filters
from pyrogram.types import Message

USERS_FOLDER = "DATABASE"
USER_DATA_FILE = "apibin.txt"


@Client.on_message(filters.command("extra", ["/", "."]))
async def iduser(client: Client, message: Message):
    inicio = time.time()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username
    else:
        user_id = message.from_user.id
        username = message.from_user.username
    BIN = message.text[len("/bin "): 11]

    if len(BIN) < 6:
        return await message.reply("<b></b>")
    if not BIN:
        return await message.reply("<b></b>")
    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]

    with open(f"{USERS_FOLDER}/{USER_DATA_FILE}", "r") as f:
        for line in f:
            if line.startswith(BIN):
                # do something with the matching line
                yo = line[0:9]
                que = yo
                await message.reply("<b>bin baneado</b>")

                break  # exits the loop once a match is found
                await message.reply("No esta en mi base de datos xD")

            else:
                # handle the case where the numbers are not found

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

                hola0 = (random.randint(24, 30))
                hola1 = (random.randint(24, 30))
                hola2 = (random.randint(24, 30))
                hola3 = (random.randint(24, 30))
                hola4 = (random.randint(24, 30))
                hola5 = (random.randint(24, 30))
                hola6 = (random.randint(24, 30))
                hola7 = (random.randint(24, 30))
                hola8 = (random.randint(24, 30))
                hola9 = (random.randint(24, 30))
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

                hola = f"""

{que}{extra0}xxxx|{si0}|{hola0}|rnd
{que}{extra9}xxxx|{si1}|{hola1}|rnd
{que}{extra1}xxxx|{si2}|{hola2}|rnd
{que}{extra2}xxxx|{si3}|{hola3}|rnd
{que}{extra3}xxxx|{si4}|{hola4}|rnd
{que}{extra4}xxxx|{si5}|{hola5}|rnd
{que}{extra5}xxxx|{si6}|{hola6}|rnd
{que}{extra6}xxxx|{si7}|{hola7}|rnd
{que}{extra7}xxxx|{si8}|{hola8}|rnd
{que}{extra8}xxxx|{si9}|{hola9}|rnd
-------------------------
あ Bin: {BIN}
あ Datos: {brand}-{typea}-{level} 
あ Banco: {bank} 
あ Pais: {country_name}
-------------------------"""

                with open(file=f'{bank}_Extra_{BIN}.txt', mode='a+', encoding='utf-8') as archivo:
                    x = archivo.readlines()
                    archivo.write('{}\n'.format(hola))

                with open(file=f'{bank}_Extra_{BIN}.txt', mode='r+', encoding='utf-8') as archivo:
                    x = archivo.readlines()

                chats = x

                chatfile = "-------------------------\nあ Research Extras あ\n-------------------------\n-"

                for chat in chats:
                    chatfile += "{}".format(chat)

                with BytesIO(str.encode(chatfile)) as output:

                    fin = time.time()

                    tiempo_transcurrido = fin - inicio
                    text = f"""
- - - - - - - - - - - - - - - - - 
あ EXTRAS RESEARCH あ
[<code>あ</code>] Monto: <code>10</code>
[<code>あ</code>] Bin: <code>{BIN}</code>
[<code>あ</code>] Pais: <code>{country_name} [{country_flag}]</code></b>
- - - - - - - - - - - - - - - - - """
                    output.name = f"{bank}_Extras_{BIN}.txt"
                    await message.reply_document(caption=text, document=output, disable_notification=True)
                    at = f"{bank}_Extra_{BIN}.txt"
                    os.remove(at)

                at = f"{bank}_Extra_{BIN}.txt"
                os.remove(at)
