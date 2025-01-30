from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
import pyrogram

@Client.on_message(filters.command("premium", prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
def premium_command(client, message):
    conn = connect_to_db()
    cursor = conn.cursor()
    username = message.from_user.username
    user_id = message.from_user.id
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) != 3:
        message.reply("Formato incorrecto. Debes usar el comando de la siguiente manera: /premium user_id días")
        return

    try:
        target_user_id = int(args[1])
        premium_days = int(args[2])
    except ValueError:
        message.reply("Por favor, ingresa un user_id y un número válido de días.")
        return

    cursor.execute('SELECT rango FROM users WHERE user_id = ?', (user_id,))
    user_rank = cursor.fetchone()


    if user_rank and user_rank[0] == 'Owner' or user_rank[0] == 'Seller':
        expiration_date = datetime.datetime.now()
        cursor.execute('UPDATE users SET rango = ?, dias = ?, fecha_registro = ? WHERE user_id = ?',
                       ('Premium', premium_days, expiration_date.timestamp(), target_user_id))
        rango = user_rank[0]
        conn.commit()
        message.reply(f"<b>El Usuario {target_user_id} ha sido actualizado a Premium por {premium_days} días por {username}.</b> ")

        owner_chat_id = target_user_id

        client.send_message(owner_chat_id, f"<b>────────────────\nあ Accendiste a nuevo rango あ\n────────────────\n[<code>あ</code>] UserID: <code>{target_user_id}</code>\n[<code>あ</code>] Dias añadido: <code>{premium_days} Dias</code>\n[<code>あ</code>] Rango: <code>Premium</code>\n[<code>あ</code>] Accendido por: <code>{username} [{rango}]</code>]\n────────────────</b>")
        
    else:
        message.reply("No tienes permiso para ejecutar este comando.")

