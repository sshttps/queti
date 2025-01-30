from pyrogram import Client, filters
from Plugins.Func import connect_to_db
import datetime

@Client.on_message(filters.command("register", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def register_handler(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    username = message.from_user.username
    userid = message.from_user.id
    
    
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (userid,))
    
    existing_user = cursor.fetchone()
    
    if existing_user:
        message.reply('Ya te encuentras registrado en nuestra base de datos.')
        return
    
    else:
        registrations_time = datetime.datetime.now().timestamp()
        cursor.execute('INSERT INTO users (user_id, rango, creditos, antispam, dias, fecha_registro) VALUES (?, ?, ?, ?, ?, ?)', (userid, 'Free', 0, 60, 0, registrations_time))
        conn.commit()
        
        message.reply('Te has registrado con éxito.')
        
        owner_id = -1002091335933
        client.send_message(owner_id, f'EL USUARIO {username} con id {userid} se ha registrado con exito en AkatkasiChk')