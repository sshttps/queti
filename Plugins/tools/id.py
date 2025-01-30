from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
from asyncio import sleep


foto = "https://i.imgur.com/Z9YqxRO.jpg"


@Client.on_message(filters.command("id", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def start_handler_traditional(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango, creditos, dias, fecha_registro FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()
   
 
    if user_data:

            username = message.from_user.username
           
         
                
    
    texto = f"""
<b>あ ID DEL USUARIO {username} あ
[あ] Id: <code>{user_id}</code></b> """


    client.send_photo(message.chat.id, photo=foto, caption=texto)
