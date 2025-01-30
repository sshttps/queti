from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram



    #---------------ADD SELLER USER---------------#    
@Client.on_message(filters.command("admin", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def admin_handler(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()[0]
    
    
    if "Owner" not in result:
        message.reply(f"<b>El chat no está autorizado para usar este comando. ❌</b>")
        return
    
    else:   

        cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
        existing_role = cursor.fetchone()
        if existing_role and ("Seller" in existing_role[0]):
            message.reply(f"<b>El usuario ya seller.</b>")
            return

   
        args = message.text.split(' ')[1].split('/')
      
        try:
            user_id = args[0]
            print(user_id)
        except ValueError:
            message.reply(f"<b>Los valores proporcionados no son válidos.</b>")
            return
        
      
        current_time = datetime.datetime.now().timestamp()

        cursor.execute('SELECT rango, fecha_registro, dias FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            role, registration_date, existing_days = user_data
            if role:

                existing_days = int(existing_days) 
                cursor.execute('UPDATE users SET rango = ?, creditos = ?, antispam = ?, dias = ?, fecha_registro = ? WHERE user_id = ?', ("Seller", 999999, 0, 999999, current_time, user_id))
                conn.commit()
                admin_first_name = message.from_user.first_name
                admin_last_name = message.from_user.last_name
                admin_name = f"{admin_first_name} {admin_last_name}"
                username = message.from_user.username
                message.reply(f"<b>Se añadio como Seller  al Usuario con ID {user_id}</b>")
                message_text = f"☁️El Owner {admin_name} - @{username} adañdio como Seller al usuario con ID {user_id}☁️"
                client.send_message("6132879706", message_text)
                client.send_message("6132879706", message_text)

                message.reply(f"El usuario {user_id} ya está registrado como {role}.</b>")
        else:

            cursor.execute('INSERT INTO users (user_id, rango, creditos, antispam, dias, fecha_registro) VALUES (?, ?, ?, ?, ?, ?)',
                (user_id, 'Seller', 999999, 0, 999999, current_time))

            conn.commit()
            message.reply(f"<b>Usuario {user_id} registrado como Seller.</b>")
 
            username = message.from_user.username
 
            admin_first_name = message.from_user.first_name
            admin_last_name = message.from_user.last_name
            admin_name = f"{admin_first_name} {admin_last_name}"

          




#---------------REMOVE PREMIUM USER---------------#    
@Client.on_message(filters.command("deldb", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def removepremium_command(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    user_id = message.from_user.id
    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()[0]
    
    if "Owner" not in result and "Seller" not in result:
        message.reply(f"<b>El chat no está autorizado para usar este comando. ❌</b>")
        return
    
    else:
        args = message.text.split(' ')[1]
        try:
            user_id = int(args)
        except ValueError:
            message.reply(f"<b>El valor proporcionado no es un ID de usuario válido.</b>")
            return

        cursor.execute('SELECT user_id, rango FROM users WHERE user_id = ?', (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            user_id, user_role = user_data
            if "Owner" in user_role or "Seller" in user_role:
                message.reply(f"<b>El usuario es parte del personal no puedes eliminarlo.</b>")
                return

            cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
            conn.commit()
            admin_first_name = message.from_user.first_name
            admin_last_name = message.from_user.last_name
            admin_name = f"{admin_first_name} {admin_last_name}"
            username = message.from_user.username
            message.reply(f"<b>Usuario {user_id} eliminado de la base de datos.</b>")
            message_text = f"❌ El administrador {admin_name} - @{username} eliminó al usuario Premium con ID {user_id} de la base de datos ❌"
            seller_chat_id = 6132879706 
            seller_name = message.from_user.first_name
            client.send_message(seller_chat_id, f"<b>El Seller <code>{seller_name}</code> elimino del los premium al usuario/Grupo con ID {user_id}.</b>")

            client.send_message("6132879706", message_text)
     
        else:
            message.reply(f"<b>El usuario/Grupo con ID {user_id} no existe en la base de datos.</b>")
