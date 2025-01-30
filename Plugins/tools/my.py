from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
from asyncio import sleep


foto = "https://i.imgur.com/Z9YqxRO.jpg"

def calculate_remaining_days(fecha_registro, dias):
    current_time = datetime.datetime.now().timestamp()

    remaining_seconds = (fecha_registro + (dias * 24 * 60 * 60)) - current_time

    remaining_days = remaining_seconds / (24 * 60 * 60)
    return remaining_days

@Client.on_message(filters.command("my", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def start_handler_traditional(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    userid = message.from_user.id
    username = message.from_user.username
    cursor.execute('SELECT rango, creditos, dias, fecha_registro FROM users WHERE user_id = ?', (userid,))
    user_data = cursor.fetchone()
   
 
    if user_data:
            rango = user_data[0]
            creditos = user_data[1]
            dias = user_data[2] 
            fecha_registro = str(user_data[3])

            dias = int(dias)
            fecha_registro = float(fecha_registro)
            remaining_days = calculate_remaining_days(fecha_registro, dias)
            remaining_days_int = int(remaining_days)

            if remaining_days_int <= 0:
                remaining_days_int = 0
                    
         
                
    
    texto = f"""
<b>あ INFORMACION DEL USUARIO {username} あ
[あ] Rango:  <code>{rango}</code>
[あ] Creditos: <code>{creditos}</code>
[あ] Dias restante: <code>{remaining_days_int}</code></b> """


    client.send_photo(message.chat.id, photo=foto, caption=texto)
