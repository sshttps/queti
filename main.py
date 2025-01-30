#----- LIBRERIAS------#
import os
import logging
from pyrogram import Client
from dotenv import load_dotenv 

#---CLIENTE----#
config = load_dotenv(".env")
Akatsuki = Client(
    "Akatsuki_Bot",
    api_id = os.getenv('API_ID'),
    api_hash = os.getenv('API_HASH'),
    bot_token = os.getenv('BOT_TOKEN'),
    plugins = dict(root = 'Plugins')
)

@Akatsuki.on_callback_query()
def callback_privates(client, callback_query):
        reply_message = callback_query.message.reply_to_message
        if reply_message is not None and reply_message.from_user is not None:
            if reply_message.from_user.id != callback_query.from_user.id:
                callback_query.answer("Navega en tu propio Menú ❗")
                return
        else:
            callback_query.answer("❗No se encontró el mensaje de respuesta o el remitente ❗")
            return
        
        callback_query.continue_propagation()

  
config = load_dotenv(".env")
Akatsuki = Client(
    "Akatsuki_Bot",
    api_id = os.getenv('API_ID'),
    api_hash = os.getenv('API_HASH'), 
    bot_token = os.getenv('BOT_TOKEN'),
    plugins = dict(root = 'Plugins')
)

logging.basicConfig(level=logging.INFO)
Akatsuki.run()
