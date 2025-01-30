import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
from pyrogram.types import CallbackQuery
from datetime import datetime
from func_bin import get_bin_info
from func_gen import cc_gen



@Client.on_message(filters.command("gen", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text & ~filters.regex(r'^/gen regen$'))
def gen_handler(client, message):
    tiempo = time.time()

    global input

    if message.reply_to_message:
            input = re.findall(r'[0-9x]+', message.reply_to_message.text)
    else:
            input = re.findall(r'[0-9x]+', message.text)

    if not input:
        message.reply("<b>─────────────────\nあ HERRAMIENTA | GENERAR TARJETA あ\n─────────────────\nPara generar las tarjetas usa /gen mas la extra.</b>")
        return
     

    #-----------FUNCION GNERADOR----------#
    if len(input)==1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input)==2:
        cc = input[0]
        mes = input[1][0:2]
        ano = 'x'
        cvv = 'x'
    elif len(input)==3:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = 'x'
    elif len(input)==4:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]                

    if len(input[0]) < 6: return message.reply('<b>あ BIN INVALIDO あ</b>',quote=True)
            
    
    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10 = cc_gen(cc,mes,ano,cvv)

    
    extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
    if mes == 'x':
        mes_2 = 'rnd'
    else:
        mes_2 = mes
    if ano == 'x':
            ano_2 = 'rnd'
    else:
        ano_2 = ano
    if cvv == 'x':
        cvv_2 = 'rnd'
    else:
        cvv_2 = cvv

    x = get_bin_info(cc[0:6])
    
    #-----------BOTONES----------#

    buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text='REFERENCIAS',url='https://t.me/ReferenciasTeamPlusBr'),
                InlineKeyboardButton(text='OWNER',url='https://t.me/GolDRoyerOP')
                ]
                
                ]
            )

    #--------PLANTILLA--------#

    message.reply(f"""
あ GENERADOR DE TARJETA あ                                     
- - - - - - - - - - - - - - - - - 
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>- - - - - - - - - - - - - - - - - 
<b>[<code>あ</code>] INFO:</b> <code>{x.get("vendor")} - {x.get("type")} - {x.get("level")}</code>
<b>[<code>あ</code>] BANCO:</b> <code>{x.get("bank_name")} {x.get("flag")}</code>
<b>[<code>あ</code>] INPUT:</b> <code>{cc}|{mes}|{ano}|xxx</code> </b>""",reply_markup=buttons)
   















