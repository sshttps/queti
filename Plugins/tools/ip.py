import json
import requests
from luhn import *
import time
import asyncio
import re
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

import random

@Client.on_message(filters.command("genmass",prefixes=['/','.','$','-'],case_sensitive=False))
async def gen(m, Message):
    input = re.findall(r'[0-9]+',Message.text)
    BIN = Message.text[len("/bin"): 11]
    if len(BIN) <6:
        return await Message.reply("<b></b>")
    if not BIN:
        return await Message.reply("<b></b>")
        apibincito = 6
        BIN = inputm[:apibinsito]
   
   
    tiempoinicio = time.perf_counter()


    
    
    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input) ==2:
        cc = input[0]
        mes = input[1]
        ano = 'x'
        cvv = 'x'
    elif len(input) ==3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = 'x'
    elif len(input) ==4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]

    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)

    tiempofinal = time.perf_counter()
    await Message.reply_text(f"""<b>
Gen mass
━━
<code>{cc1}
{cc2}
{cc3}
{cc4}
{cc5}
{cc6}
{cc7}
{cc8}
{cc9}
{cc10}
</code>
━━━ 
<b><i>Time sleep</i></b> : <code>{tiempofinal - tiempoinicio:0.2} seconds</code>
    </b>""",reply_markup=keyboard)

   
buttons = [
    [
        InlineKeyboardButton("ReGen", callback_data="callback_data_1"),
    ],

]

keyboard = InlineKeyboardMarkup(buttons)


def luhn_verification(num):
    num = [int(d) for d in str(num)]
    check_digit = num.pop()
    num.reverse()
    total = 0
    for i,digit in enumerate(num):
        if i % 2 == 0:
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        total += digit
    total = total * 9
    return (total % 10) == check_digit



def cc_gen(cc,mes='x',ano='x',cvv='x'):
    ccs = []
    while len(ccs) < 10:
        card = str(cc)
        digits = '04567896789'
        list_digits = list(digits)
        random.shuffle(list_digits)
        string_digits = ''.join(list_digits)
        card = card + string_digits
        if card[0] == '3':
            card = card[0:15]
        else:
            card = card[0:16]

        if mes == 'x':
            mes_gen = random.randint(1,12)
            if len(str(mes_gen)) == 1:
                mes_gen = '0' + str(mes_gen)
        else:
            mes_gen = mes

        if ano == 'x':
            ano_gen = random.randint(2023,2031)
        else:
            ano_gen = ano
            if len(str(ano_gen)) == 2:
                ano_gen = '20' + str(ano_gen)

        if cvv == 'x':
            if card[0] == '3':
                cvv_gen = random.randint(1000,9999)
            else:
                cvv_gen = random.randint(100,999)
        else:
            cvv_gen = cvv

        x = str(card) + '|' + str(mes_gen) + '|' + str(ano_gen) + '|' + str(cvv_gen)    
        a = luhn_verification(card)
        if a:
            ccs.append(x)
        else:
            continue

    return ccs