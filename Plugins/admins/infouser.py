from pyrogram import Client, filters
from Plugins.Func import connect_to_db
import sqlite3

def obtener_informacion_usuario(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    usuario = cursor.fetchone()
    conn.close()  # Cerrar la conexión después de su uso
    return usuario

@Client.on_message(filters.command(["info"], ["/", "."]))
async def mostrar_informacion_usuario(client, message):
    try:
        command = message.text.split(" ")

        if len(command) < 2:
            await message.reply("Debes proporcionar un ID de usuario.")
            return

        user_id = int(command[1])

        usuario = obtener_informacion_usuario(user_id)

        if usuario:
            user_id, rango, creditos, dias, fecha_registro = usuario
            respuesta = f"**Información del usuario**\n\n"
            respuesta += f"User ID: {user_id}\n"
            respuesta += f"Rango: {rango}\n"
            respuesta += f"Créditos: {creditos}\n"
            respuesta += f"Días de acceso restantes: {dias}\n"
            respuesta += f"Fecha de registro: {fecha_registro}"

            await message.reply(respuesta)
        else:
            await message.reply("Usuario no encontrado en la base de datos.")

    except ValueError:
        await message.reply("El ID de usuario debe ser un número.")
    except sqlite3.Error as e:
        await message.reply(f"Error de base de datos: {str(e)}")
    except Exception as e:
        await message.reply(f"Ocurrió un error: {str(e)}")
