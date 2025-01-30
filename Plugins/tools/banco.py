from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Plugins.Func import connect_to_db
import datetime
from asyncio import sleep





keyboard = InlineKeyboardMarkup(

    [
        [
            InlineKeyboardButton("あ SIGUIENTE あ", callback_data="banco2"),
            
        ]
        
    ]
    )


messages = {
    
"banco2": """
BIN ➜ ϟ  435546
BANCO ➜ ϟ REGIONS BANK 
🇺🇸 | ONLYFANS  10 o 20
🇺🇸 | TWITCH BITS
━━━━━━━━━  
BIN ➜ ϟ 417903
BANCO ➜ ϟ LEESPORT BANK
🇺🇸 | WEBS STRIPE 
🇺🇸 | INSTAGRAM SEGUIDORES 
🇺🇸 | TWITCH BITS
━━━━━━━━━  
BIN ➜ ϟ 415277
BANCO ➜ ϟ BANCO DE COSTA RICA
🇨🇷 | PRIME VIDEO
🇺🇸 | ACORNTV
🇨🇷 | ALIEXPRESS APP (-5$)
🇨🇷 | AMAZON MUSIC
🇺🇸 | WALMART PLUS 
🇨🇷 | AMAZON GAMING + FREE TWICH SUB
🇨🇷 | SKILLSHARE 2M
━━━━━━━━━  
BIN ➜ 515942
BANCO ➜ ϟ WEBBANK
 | PARAMOUNT PLUS 
🇺🇸 | ADOBE CREATIVE CLOUD
🇺🇸 | RAKUTEN VIKIPASS
🇺🇸 | ICONFINDER PRO
🇺🇸 | PRIME VIDEO ANUAL
🇺🇸 | TIDAL HI-FI PLUS 
 | DUOLINGO SUPER
🇺🇸 | DESIGNS AI
🇺🇸 | MAYBE AUTOPAY
━━━━━━━━━  
BIN ➜ 448421
BANCO ➜ ϟ BANK OF NOVA SCOTIA
🇨🇦 | SKILLSHARE
 | AMAZON PRIME 
🇨🇦 | CANVA PRO YEARLY
🇨🇦 | ADOBE TRIAL
🇨🇦 | RIVER TV CANADA
 | SCRIBD
🇨🇦 | DEEZER PREMIUM
🇨🇦 | AMAZON WEB SERVICES (AWS)
🇨🇦 | SOUNDCLOUD+GO
🇺🇸 | FLIXOLÉ
🇨🇦 | TIDAL HI-FI PLUS
🇨🇦 | AUDIOMACK PREMIUM
🇨🇦 | IDAGIO PREMIUM
🇺🇸 | DROPBOX 
🇨🇦 | HAYU 6 MONTHS PLAN
🇨🇦 | NAPSTER 3 MONTHS
🇨🇦 | ICONFINDER
━━━━━━━━━  
BIN ➜ 551507
BANCO ➜ ϟ BANCO DEL AHORRO NACIONAL Y SERVICIOS FINANCIEROS, S.N.C.
🇲🇽 | PICSART GOLD
🇲🇽 | ICONFINDER
🇲🇽 | CLEARVPN
🇲🇽 | TIDAL HI-FI PLUS
🇲🇽 | ATRESPLAYER SERIES
🇲🇽 | FLIXOLE
🇲🇽 | PARAMOUNTPLUS (codigo: PINKLADIES)
🇲🇽 | DUOLINGO SUPER
🇲🇽 | CANVA PRO
🇲🇽 | BLITZ PASE PRO
🇲🇽 | DESIGNS AI
🇲🇽 | AUDIOMACK MUSIC
🇲🇽 | ACORN TV
🇲🇽 | UMBRA STREAM
🇲🇽 | STORYTEL BOOKS
━━━━━━━━━  
BIN ➜ 448421
BANCO ➜ ϟ BANK OF NOVA SCOTIA
🇨🇦 SKILLSHARE
 | AMAZON PRIME 
🇨🇦 | CANVA PRO YEARLY
🇨🇦 | ADOBE TRIAL
🇨🇦 | RIVER TV CANADA
 | SCRIBD
🇨🇦 | DEEZER PREMIUM
🇨🇦 | AMAZON WEB SERVICES (AWS)
🇨🇦 | SOUNDCLOUD+GO
🇺🇸 | FLIXOLÉ
🇨🇦 | TIDAL HI-FI PLUS
🇨🇦 | AUDIOMACK PREMIUM
🇨🇦 | IDAGIO PREMIUM
🇺🇸 | DROPBOX 
🇨🇦 | HAYU 6 MONTHS PLAN
🇨🇦 | NAPSTER 3 MONTHS
🇨🇦 | ICONFINDER
━━━━━━━━━  
BIN ➜ 521309
BANCO ➜ ϟ BANCO DE LA PRODUCCION S.A. (PRODUBANCO)
🇪🇨 | APPLE MÚSIC [cambia a ecuador alregistrarte]
🇪🇨 | APPLETV 
🇪🇨 | SPOTIFY PREMIUM(ACTUALIZA Y RENUEVA) 
🇪🇨 | CRUNCHYROLL [CVV:0000 & ZIP CODE: 00000]
🇪🇨 | TIDAL [zip 10010]
🇪🇨 | SCRIBD 
🇪🇨 | CANVA PRO
🇪🇨 | YO USICIAN 
🇪🇨 | AMAZONMUSIC 
🇪🇨 | PRIMEVIDEO
━━━━━━━━━  
BIN ➜ 420849
BANCO ➜ ϟ CAPITAL BANK, INC.
🇵🇦 | PARAMOUNT
🇵🇦 | AMAZON MUSIC
🇵🇦 | CANVA
🇵🇦 | SPOTIFY PREMIUM
🇵🇦 | PRIME GAMING
🇵🇦 | PRIME VIDEO
━━━━━━━━━ 
BIN ➜ 537970
BANCO ➜ ϟ PT. BANK CIMB NIAGA TBK.
🇺🇸 | RAKUTEN VIKI PASS
🇺🇸 | ADOBE CREATIVE CLOUD 
🇺🇸 | WALMART+ (sirve para activar paramount)
🇺🇸 | DESIGNS
🇺🇸 | DUOLINGO
🇺🇸 | BES BUY FREE CODES 
🇺🇸 | RATUKEN KOBO BOOKS 
🇺🇸 | CANVA PRO 
🇺🇸 | AMAZON PRIME VIDEO/GAMING
🇺🇸 | ATRES PLAYER
🇺🇸 | ACORN TV 
 | DUOLINGO PREMIUM
🇺🇸 | TIDAL
🇺🇸 | LIONSGATE+
🇺🇸 | PUREFLIX
━━━━━━━━━ 
BIN ➜ 551507
BANCO ➜ ϟ BANCO DEL AHORRO NACIONAL Y SERVICIOS FINANCIEROS, S.N.C.
🇲🇽 | CLEAR VPN 
🇲🇽 | TILDAL 
🇲🇽 | PARAMOUNT PLUS
🇲🇽 | CANVA PRO 
🇲🇽 | ACORTN TV 
🇲🇽 | DOULINGO SUPER 
🇲🇽 | ATRESPLAYER SERIES 
🇲🇽 | PICSART GOLD
🇲🇽 | APPLE TV
🇲🇽 | MICROSOFT 365 TRIAL 
🇺🇸 | YOUTUBE PREMIUM
🇲🇽 | APPLE MUSIC
━━━━━━━━━
BIN ➜ ϟ 524175
BANCO ➜ ϟ ARAB BANK PLC
🇦🇪 | DEEZER PREMIUM 
🇦🇪 | MICROSOFT 365 TRIAL
🇺🇸 | YOUTUBE PREMIUM
🇦🇪 | APPLE TV
🇦🇷 | LIONSGATE PLUS (zip: 2345)
🇦🇪 | APPLE MUSIC 
━━━━━━━━━     
BIN ➜ ϟ 414962
BANCO ➜ ϟ CB PRIVATBANK
🇺🇦 | Crunchyrol 
 | ONLYFANS
━━━━━━━━━      
BIN ➜ ϟ 530079
BANCO ➜ ϟ WELLS FARGO BANK, N.A.
 | PARAMOUNT PLUS 
🇺🇸 | ADOBE CREATIVE CLOUD
🇺🇸 | RAKUTEN VIKI
🇺🇸 | ICONFINDER PRO
🇺🇸 | PRIME VIDEO 
🇺🇸 | TIDAL HI-FI PLUS 
 | DUOLINGO SUPER
🇺🇸 | DESIGNS AI   
━━━━━━━━━  
BIN ➜ ϟ 450553
BANCO ➜ ϟ CANADIAN IMPERIAL BANK OF COMMERCE
🇨🇦 | SKILLSHARE
 | AMAZON PRIME 
🇨🇦 | CANVA PRO YEARLY
🇨🇦 | ADOBE TRIAL
🇨🇦 | DEEZER PREMIUM
🇨🇦 | AMAZON WEB SERVICES (AWS)
🇨🇦 | SOUNDCLOUD+GO
🇨🇦 | TIDAL HI-FI PLUS
🇨🇦 | NAPSTER 1 MONTH
🇨🇦 | ICONFINDER       
━━━━━━━━━  
BIN ➜ ϟ  519311
BANCO ➜ ϟ PT BANK UOB INDONESIA
🇺🇸 | RAKUTEN VIKI PASS
🇺🇸 | ADOBE CREATIVE CLOUD 
🇺🇸 | WALMART+ (sirve para activar paramount)
🇺🇸 | DESIGNS
🇺🇸 | DUOLINGO
🇺🇸 | BES BUY FREE CODES 
🇺🇸 | RATUKEN KOBO BOOKS 
🇺🇸 | CANVA PRO 
🇺🇸 | AMAZON PRIME VIDEO/GAMING
 | ATRES PLAYER
🇺🇸 | ACORN TV 
🇺🇸 | DUOLINGO PREMIUM
🇺🇸 | TIDAL
🇺🇸 | LIONGASTE+
🇺🇸 | PUREFLIX
🇨🇦 | ICONFINDER   
━━━━━━━━━   
""",
}

@Client.on_message(filters.command(["banco"], prefixes=['.','/','!'], case_sensitive=False) & filters.text)
def start_handler(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    texto=f"""あ BANCOS - PAISES あ
━━━━━━━━━                    
BIN ➜ ϟ 405060
BANCO ➜ ϟ SOCIETE GENERALE ALGERIE
🇩🇿 | Spotify (NO VPN SITIOS 
🇩🇿 | Xbox game pass 
🇩🇿 | Microsoft AWS 
🇩🇿 | Amazon Azure ALGERIA (🇩🇿
🇩🇿 | DEEZER   
━━━━━━━━━ 
BIN ➜ ϟ 401658
BANCO ➜ ϟ KENTUCKY BANK AND TRUST
🇺🇸 | KOCOWA KOREA CONTENT 
🇺🇸 | STAN TV
🇺🇸 | FIXOLE
🇺🇸 | ASIANCRUSH ANIME
🇺🇸 | YT PREMIUM 
🇺🇸 | PHILO TV
🇺🇸 | DISCOVERY+ (from phone)
🇺🇸 | SHUDDER MONTH  
🇺🇸 | FLIX PREMIERE
🇺🇸 | ACORN TV MONTH 
🇺🇸 | BRITBOX MOVIES
🇺🇸 | LIFETIME MOVIES
🇺🇸 | YOUTUBE TV 
🇺🇸 | FRNDLYTV
🇺🇸 | AMC+
🇺🇸 | FILMBOX+ 
━━━━━━━━━ 
BIN ➜ ϟ 405547
BANCO ➜ ϟ CARDS NZ, LTD.
🇳🇿 | AMAZON PRIME VIDEO
🇳🇿 | MICROSOFT 365
🇳🇿 | SKYPE NUMBER
🇳🇿 | SCRIBD 
━━━━━━━━━    
BIN ➜ ϟ 489504
BANCO ➜ ϟ none
🇵🇭 | YouTube PREMIUM 
🇺🇸 | READING EGGS
🇺🇸 | ICONFINDER
🇺🇸 | EPIDEMIC SOUNDS
🇺🇸 | Spotify premium 
🇺🇸 | CANVA pro
🇺🇸 | VOOKS
🇨🇦 | RIVER TV  
━━━━━━━━━ 
BIN ➜ ϟ 559200
BIN ➜ ϟ 522250
BANCO ➜ ϟ STANDARD BANK OF SOUTH AFRICA, LTD
🇿🇦 | Crunchyrol
🇿🇦 | Amazon prime
━━━━━━━━━ 
BIN ➜ ϟ 532655
BANCO ➜ ϟ COMMONWEALTH BANK OF AUSTRALIA
🇦🇺 | MICROSOFT 365 TRIAL
🇦🇺 | CRUNCHYROLL ANUAL
🇦🇺 | AMAZON PRIME  
🇦🇺 | SKYPE NUMBER 
🇦🇺 | MICROSOFT 365 BUY 
🇦🇺 | GAMEPASS ULTIMATE
━━━━━━━━━                      
BIN ➜ ϟ 541174
BANCO ➜ ϟ BANK OF INDIA
🇮🇹 | BIN DIRECTV GO
🇺🇸 | BIN CLEANUP PRO
🇺🇸 | UMBRA STREAM
🇺🇸 | CLEAR VPN TRIAL
🇺🇸 | DROPBOX PROFESSIONAL
🇺🇸 | INSIGHT TIMER
🇺🇸 | CALM
🇺🇸 | GAIA
🇺🇸 | DUOLINGO
🇺🇸 | STORYTEL
🇺🇸 | EPIDEMIC SOUND 
━━━━━━━━━  
BIN ➜ ϟ 555786
BANCO ➜ ϟ BANCO BS2 S.A.
🇧🇷 | APPLE TV
🇧🇷 | PRIME VIDEO
🇧🇷 | PLAYPLUS (app)
🇧🇷 | PRIME GAMING
🇧🇷 | EUROPA+
🇧🇷 | MICROSOFT 365 TRIAL (cvv 000)
🇧🇷 | APPLE MUSIC
🇧🇷 | CANVA PRO
🇧🇷 | AMAZON MUSIC
🇧🇷 | DUOLINGO
🇧🇷 | UMBRA STREAM
🇧🇷 | TIDAL HI-FI PLUS
🇧🇷 | SPOTIFY PREMIUM
🇧🇷 | YOUTUBE PREMIUM    
━━━━━━━━━
BIN ➜ ϟ 520586
BANCO ➜ ϟ BANCO BS2 S.A.
🇧🇷 | APPLE TV
🇧🇷 | HBOMAX (movil plan)
🇧🇷 | PRIME VIDEO
🇧🇷 | PLAYPLUS (app)
🇧🇷 | PRIME GAMING
🇧🇷 | MICROSOFT 365 TRIAL (cvv 000)
🇧🇷 | APPLE MUSIC
🇧🇷 | CANVA PRO
🇧🇷 | AMAZON MUSIC
🇧🇷 | DUOLINGO
🇧🇷 | TIDAL HI-FI PLUS
🇧🇷 | YOUTUBE PREMIUM  
━━━━━━━━━
BIN ➜ ϟ 4030xx
BANCO ➜ ϟ PNC BANK, N.A.
 | PARAMOUNT PLUS
 | MUBI 3 MONTHS
 | FLIXOLE 
🇺🇸 | ADOBE CC
🇺🇸 | TIDAL HI-FI PLUS 
🇺🇸 | SPOTIFY PREMIUM
🇺🇸 | TWICH BITS
🇺🇸 | ACORN TV
🇺🇸 | AZURE
🇺🇸 | EDUCATIVE IO
🇺🇸 | WALMART+
🇺🇸 | PRIME + AUDIBLE
🇺🇸 | SOUNDCLOUD+ GO
🇺🇸 | BEST BUY FREE CODES   
━━━━━━━━━
BIN ➜ ϟ 461046
BANCO ➜ ϟ JPMORGAN CHASE BANK, N.A
🇺🇸 | PRIME VIDEO (maybe autopay)
🇺🇸 | SCRIBD
🇺🇸 | DEEZER PREMIUM
🇺🇸 | ACORNTV 
🇺🇸 | TWICH BITS      
━━━━━━━━━
BIN ➜ ϟ 542539
BANCO ➜ ϟ MERRICK BANK
🇺🇸 | ADOBE CREATIVE CLOUD
🇺🇸 | CANVA PRO
🇺🇸 | ACORNTV
🇺🇸 | PUREFLIX MOVIES
 | PARAMOUNT
 | SCRIBD 2 MONTHS
🇺🇸 | TIDAL HI-FI PLUS
 | FLIXOLE MOVIES
🇺🇸 | DROPBOX 
🇺🇸 | AMC PLUS   

"""

    client.send_message(message.chat.id, caption=texto, reply_markup=keyboard)
    
@Client.on_callback_query(filters.regex("^banco2$"))
def option_handler(client, query):
    option = query.data

 # Obtener el mensaje específico para cada opción
    message_text = messages.get(option, "Mensaje predeterminado si no se encuentra la opción")

    # Editar el mensaje para mostrar solo el botón "Atrás"
    query.edit_message_text(f"あ Has seleccionado la opción {option.capitalize()} あ: {message_text}", reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("あ ATRÁS あ", callback_data="banco")
        ]]))









