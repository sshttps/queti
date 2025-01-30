from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
from asyncio import sleep




foto = "https://i.imgur.com/Z9YqxRO.jpg"

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("あ REFERENCIAS あ", url="https://t.me/ReferenciasTeamPlusBr"),
            InlineKeyboardButton("あ OWNER あ", url="https://t.me/GolDRoyerOP")
        ],
        [
            InlineKeyboardButton("あ GATES | HERRAMIENTA あ", callback_data="cmds")
        ]
         
    ]
)

cmds_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("あ AUTH あ", callback_data="auth"),
            InlineKeyboardButton("あ CHARGED あ", callback_data="charged"),
            InlineKeyboardButton("あ ESPECIAL あ", callback_data="especial"),
            
        ],
        [
            InlineKeyboardButton("あ HERRAMIENTAS あ", callback_data="tools"),
            InlineKeyboardButton("あ ATRÁS あ", callback_data="back")
        ]
        
    ]
    )


messages = {
     "especial": """
<b>あ GATES ESPECIAL | MITSURI CHK あ
[<code>あ</code>] Pasarela: Shopify + Pz 90 USD
[<code>あ</code>] Gateway: KRATOS | <code>/kr</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify + Pz 38.98 USD
[<code>あ</code>] Gateway: ARES | <code>/ar</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify + Pz 34.90 USD
[<code>あ</code>] Gateway: MORFEO | <code>/mo</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - <b>
""",
    "auth": """
<b>あ GATES AUTH | MITSURI CHK あ
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: STRIPE
[<code>あ</code>] Gateway: MIATA | <code>/mi</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - </b>
""",
    "charged": """
<b>あ GATES CHRAGED | MITSURI CHK あ
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify 10 USD
[<code>あ</code>] Gateway: AFRODITA | <code>/af</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify + B3 20 USD
[<code>あ</code>] Gateway: HERCULES | <code>/hr</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify 40.29 USD
[<code>あ</code>] Gateway: HEFESTO | <code>/he</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify Avs 4.36 USD
[<code>あ</code>] Gateway: TERRENEITOR | <code>/te</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] Pasarela: Shopify + B3 281.56 USD
[<code>あ</code>] Gateway: POSEIDON | <code>/po</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - -
[<code>あ</code>] Pasarela: Shopify + Eway 20.98 USD
[<code>あ</code>] Gateway: POSEIDON | <code>/po</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - -
[<code>あ</code>] Pasarela: Shopify + Payflow 15.94 USD
[<code>あ</code>] Gateway: ASCLEPIO | <code>/as</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - -</b>""",
    "tools": """
<b>あ HERRANIENTAS | MITSURI CHK あ
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] BIN - DETALLES DEL BIN あ
[<code>あ</code>] Uso: <code>/bin</code> | ej <code>/bin 376659</code> 
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] GEN - GENERAR TARJETA あ
[<code>あ</code>] Uso: <code>/gen</code> | ej <code>/gen 376659</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] RAND - GENERAR DIRECCIONES あ
[<code>あ</code>] Uso: <code>/rand</code> | ej <code>/rand us</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] EXTRA - BUSCADOR DE EXTRA あ
[<code>あ</code>] Uso: <code>/extra</code> | ej <code>/extra 376659</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - 
[<code>あ</code>] REXTRA - GENERADOR DE EXTRA あ
[<code>あ</code>] Uso: <code>/rextra</code> | ej <code>/rextra 376659</code>
[<code>あ</code>] Estado: <code>On</code> | <code>free</code>
- - - - - - - - - - - - - - - - - </b>"""

}




@Client.on_message(filters.command(["cmds"], prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def start_handler(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    texto=f"""
<b>[<code>あ</code>] CMDS | SELECIONA CUALQUIER MENU [<code>あ</code>]
En este apartado podras seleccionar tu menu de preferecia y visualizar sus gateway o sus herramientas/tools..</b>
"""

    client.send_photo(message.chat.id, photo=foto, caption=texto, reply_markup=cmds_keyboard)

@Client.on_callback_query(filters.regex("^cmds$"))
def cmds_handler(client, query):
    query.edit_message_text("<b>[<code>あ</code>] CMDS | SELECIONA CUALQUIER MENU [<code>あ</code>]\nEn este apartado podras seleccionar tu menu de preferecia y visualizar sus gateway o sus herramientas/tools..</b>", reply_markup=cmds_keyboard)

@Client.on_callback_query(filters.regex("^auth|charged|mass|especial|tools$"))
def option_handler(client, query):
    option = query.data

 # Obtener el mensaje específico para cada opción
    message_text = messages.get(option, "Mensaje predeterminado si no se encuentra la opción")

    # Editar el mensaje para mostrar solo el botón "Atrás"
    query.edit_message_text(f"あ Has seleccionado la opción {option.capitalize()} あ: {message_text}", reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("あ ATRÁS あ", callback_data="cmds")
    ]]))

@Client.on_callback_query(filters.regex("^(back)$"))
def back_handler(client, query):
    query.edit_message_text("</b>[<code>あ</code>] MITSURI CHK | BIENVENIDO [<code>あ</code>]\n Para visualisar nuestros gateway o nuestras herramientas/tools disponibles, escriba /cmds, Esperemos que el chk sea de tu agrado, disfruta esta instancia...</b>", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^(back1)$"))
def back1_handler(client, query):
    query.edit_message_text("<b>[<code>あ</code>] GATES | CHARGED - AUTH [<code>あ</code>]\nPor el momento contamos con <code>7</code> Charged Free - <code>1</code> Charged Premium, Tambien contamos con <code>1</code> auth free../b>", reply_markup=cmds_keyboard)
# Para el manejo del comando /start tradicional, si es necesario
@Client.on_message(filters.command("start", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def start_handler_traditional(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    texto=f"""
</b>[<code>あ</code>] MITSURI CHK | BIENVENIDO @{username} [<code>あ</code>]
Para visualisar nuestros gateway o nuestras herramientas/tools disponibles, escriba /cmds, Esperemos que el chk sea de tu agrado, disfruta esta instancia...</b>"""

    client.send_photo(message.chat.id, photo=foto, caption=texto, reply_markup=keyboard)




