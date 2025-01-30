from asyncio import sleep
from pyrogram import Client, filters
import datetime

from Plugins.Func import connect_to_db

def calculate_remaining_days(fecha_registro, dias):
    current_time = datetime.datetime.now().timestamp()

    remaining_seconds = (fecha_registro + (dias * 24 * 60 * 60)) - current_time

    remaining_days = remaining_seconds / (24 * 60 * 60)
    return remaining_days

@Client.on_message(filters.command(["buscar"], ["/", "."]))
def buscarkey(client, message):
        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            user_id = message.text.split()[1]
        except (IndexError, ValueError):
            message.reply(f"<b>Coloca el USER ID</b>")
            return

        cursor.execute('SELECT rango, creditos, dias, fecha_registro FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()
        if not user_data:
            return message.reply(f"<b>El usuario no existe.</b>")
 
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
                    
         
                
    
        mensaje = f"""
<b>───────────────────
あ INFORMACION | USUARIO あ
───────────────────
あ USER ID: <code>{user_id}</code>
あ RANGO: <code>{rango}</code>
あ CREDITOS: <code>{creditos}</code>
あ DIAS RESTANTES: <code>{remaining_days_int}</code>
───────────────────</b> """
 
 
        client.send_message(message.chat.id, mensaje)
    
    