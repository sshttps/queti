from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram




@Client.on_message(filters.command("addgp", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def add_group_command(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    username = message.from_user.username
    user_id = message.from_user.id
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) != 3:
        message.reply("Formato incorrecto. Debes usar el comando de la siguiente manera: /addgp chat_id días")
        return

    try:
        target_chat_id = int(args[1])
        group_days = int(args[2])
    except ValueError:
        message.reply("Por favor, ingresa un chat_id válido y un número válido de días.")
        return

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()

  
    if user_rank and (user_rank[0] == 'Owner' or user_rank[0] == 'Seller'):
        expiration_date = datetime.datetime.now()
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                       (target_chat_id, 'Grupo', group_days, expiration_date.timestamp()))
        conn.commit()
        message.reply(f"<b>Grupo {target_chat_id} ha sido agregado como 'Grupo' por {group_days} días por {username}.</b> ")

        owner_chat_id = 6132879706
    
        client.send_message(owner_chat_id, f"<b>Nuevo grupo 'Grupo' agregado con {group_days} días: {target_chat_id} por {username} ⭐</b>")
        
    else:
        message.reply("No tienes permiso para ejecutar este comando.")
        
        

@Client.on_message(filters.command("addstaff", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def add_group_commandsaaa(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    username = message.from_user.username
    user_id = message.from_user.id
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) != 3:
        message.reply("Formato incorrecto. Debes usar el comando de la siguiente manera: /addgp chat_id días")
        return

    try:
        target_chat_id = int(args[1])
        group_days = int(args[2])
    except ValueError:
        message.reply("Por favor, ingresa un chat_id válido y un número válido de días.")
        return

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()

    if user_rank and (user_rank[0] == 'Owner' or user_rank[0] == 'Seller'):
        expiration_date = datetime.datetime.now()
        cursor.execute('INSERT INTO users (user_id, rango, dias, fecha_registro) VALUES (?, ?, ?, ?)',
                       (target_chat_id, 'Staff', group_days, expiration_date.timestamp()))
        conn.commit()
        message.reply(f"<b>Grupo {target_chat_id} ha sido agregado como 'Grupo' por {group_days} días por {username}.</b> ")
        owner_chat_id = 6132879706
    
        client.send_message(owner_chat_id, f"<b>Nuevo grupo 'Staff' agregado con {group_days} días: {target_chat_id} por {username} ⭐</b>")
        
    else:
        message.reply("No tienes permiso para ejecutar este comando.")
        
        