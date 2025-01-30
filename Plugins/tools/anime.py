import openai
from pyrogram import Client, filters
from pyrogram.types import Message

# Configura tu clave de API de OpenAI aquí
openai.api_key = "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"

@Client.on_message(filters.command(["ai"], ["/", "."]))
async def chat_with_gpt(_, message: Message):
    if message.reply_to_message and message.reply_to_message.text:
        # Obtiene el texto del mensaje al que se responde
        user_input = message.reply_to_message.text

        # Personaliza la solicitud para que GPT tenga una personalidad "kwai"
        prompt = f"Kwai GPT: {user_input}"

        # Realiza la solicitud a la API de OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Puedes cambiar el motor según tus necesidades
            prompt=prompt,
            temperature=0.7,  # Ajusta la temperatura para controlar la aleatoriedad de las respuestas
            max_tokens=150  # Ajusta el número máximo de tokens en la respuesta
        )

        # Extrae la respuesta generada por GPT
        gpt_response = response.choices[0].text.strip()

        # Agrega caritas de texto "kwai" a la respuesta
        kwai_response = f"{gpt_response} ( ˘ ³˘)♥"

        # Envía la respuesta al chat de Telegram
        await message.reply_text(kwai_response)
    else:
        await message.reply_text("Por favor, responde a un mensaje para que pueda generar una respuesta.")

# Puedes personalizar y expandir este código según tus necesidades.
