import time
from pyrogram import Client, filters
from pyrogram.types import Message
from func_bin import get_bin_info

#------COMANDO BIN--------#
@Client.on_message(filters.command("bin", prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def bin_handler(client, message):
    BIN = message.text[len("/bin"):11].strip()
    
    if len(BIN) < 6:
        message.reply("<b>─────────────────\nあ HERRAMIENTA | BIN あ\n─────────────────\nPara solicitar informacion de un bin use /bin 4556747, recordar que tiene que ser los primeros 6 digitos de la tarjeta</b>.")
        return
        
    if not BIN:
        message.reply("<b>─────────────────\nあ HERRAMIENTA | BIN あ\n─────────────────\nPara solicitar informacion de un bin use /bin 4556747, recordar que tiene que ser los primeros 6 digitos de la tarjeta.</b>")
        return
    
    func = get_bin_info(BIN[:6])
    
    message.reply(f"""
<b>あ INFORMACION DEL BIN あ</b>
<b>[<code>あ</code>] BIN:</b> <code>{BIN[:6]}</code> 
<b>[<code>あ</code>] PAIS:</b> <code>{func.get("country")} {func.get("flag")}</code>   
<b>[<code>あ</code>] DETALLES:</b> <code>{func.get("type")} - {func.get("level")} - {func.get("vendor")}</code>  
<b>[<code>あ</code>] BANCO:</b> <code>{func.get("bank_name")}</code>                                  
<b>─────────────────</b>""")