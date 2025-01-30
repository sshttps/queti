from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import random


def generate_key(length):
    key = f"TeamPlusChk-{random.randint(10000000, 99999999)}-PREMIUM"
    return key


@Client.on_message(filters.command("key1", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def generatekey(client, message):
    try:   
        conn = connect_to_db()
        cursor = conn.cursor()
        
        user_id = message.from_user.id
        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
       
        if "Owner" not in result:
            message.reply(f"<b>El chat no está autorizado para usar este comando. ❌</b>")
            return
        
        
        
        days = int(message.command[1])
        
  
        key = generate_key(16)
  
        generate_by = message.from_user.id

        cursor.execute("INSERT INTO keys (key, status, user_claim, days, generate_by) VALUES (?, ?, ?, ?, ?)",
            (key, "LIVE", None, days, generate_by))
        conn.commit()
        
        username = message.from_user.username
        
        message.reply(f"""
───────────────────
あ KEY GENERADA CORRECTAMENTE あ
───────────────────
[<code>あ</code>] KEY: <code>{key}</code>
[<code>あ</code>] TIPO: <code>Premium</code>
[<code>あ</code>] DIAS: <code>{days}</code>
[<code>あ</code>] GENERADO POR: @{username} 
───────────────────""")
        
    except Exception as e:
        message.reply("Error al generar la clave.")
        print(e)
        
        
    admin_first_name = message.from_user.first_name
    admin_last_name = message.from_user.last_name
    username = message.from_user.username
    admin_name = f"{admin_first_name} {admin_last_name}"
        
    message_text = f"🔑 El administrador {admin_name} - @{username} ha generado una clave con {days} días:\n\n<code>{key}</code> 🔑"
 
  
    client.send_message("6132879706", message_text)
        
        
@Client.on_message(filters.command("claim", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def claimkey(client, message):
    conn = connect_to_db()
    user_id = message.from_user.id
    cursor = conn.cursor()

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    username = message.from_user.username

    if not result:
        return message.reply(f"<b>No estás registrado. Por favor, utiliza /register para registrarte.</b>")
  
    

    # Verifica si el usuario ya es Premium
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    
    datos = message.text.split(" ")
    
    if len(datos) < 2:
        message.reply(f"<b>Key incorrecta.")
        return
    
    
    key = datos[1].strip()
    

    
    if result[0] in ["Baneado", "baneado"]:
             return message.reply(f"<b>No tienes permitido usar el bot❌\nReson: Baneado.")
            
 
    if result and "Premium" in result[0]:
            message.reply(f"Ya eres un usuario Premium. Esta clave no es redimible para ti.")
            return


    if result and ("Owner" in result[0] or "Seller" in result[0]):
            message.reply(f"Eres parte del personal, no puedes canjear Keys.")
            return
        
    cursor.execute('SELECT status FROM keys WHERE key = ?', (key,))    
    key_status = cursor.fetchone()
    print(key_status)
    if not key_status:
        message.reply(f"La clave no existe.")
        return
    elif key_status[0] != 'LIVE':
        message.reply(f"<b>La clave ya ha sido canjeada.</b>")
        return
  
    cursor.execute('SELECT days FROM keys WHERE key = ?', (key,))
    days = cursor.fetchone()[0]
    
    current_time = datetime.datetime.now().timestamp()
    
    cursor.execute('UPDATE users SET rango = ?, creditos = ?, antispam = ?, dias = ?, fecha_registro = ? WHERE user_id = ?',
                    ('Premium', 0, 15, days, current_time, user_id))
    conn.commit()


    cursor.execute('UPDATE keys SET status = ?, user_claim = ?, days = ? WHERE key = ?',
        ('DEAD', user_id, days, key))
    conn.commit()
        
        
    username = message.from_user.username
    
    message.reply(f"""
───────────────────
 CANJEO EXITOSO
───────────────────
[<code>あ</code>] KEY: <code>{key}</code>
[<code>あ</code>] TIPO: <code>Premium</code>
[<code>あ</code>] DIAS: <code>{days}</code>
[<code>あ</code>] NUEVO ESTATUS: @{username} <code>[Premium]</code>
───────────────────""")
        
    admin_first_name = message.from_user.first_name
    admin_last_name = message.from_user.last_name
    admin_name = f"{admin_first_name} {admin_last_name}"
    username = message.from_user.username

    message_text = f"🔑 El usuario {admin_name} - @{username} ha canjeado una clave con éxito:\n\n<code>{key}</code> 🔑"
 
  
    client.send_message("6132879706", message_text)
 