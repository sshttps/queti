from pyrogram import Client, filters
import random
import time

played_users = {}  # dictionary to track users and their last play time
cooldown_time = 60  # cooldown time in seconds (1 minute)
win_prob = 0.2  # probability of winning


@Client.on_message(filters.command("dados", prefixes=["/", "."]))
def play_dice_game(client, message):
    user_id = message.from_user.id

    # Check if the user has played in the cooldown period
    if user_id in played_users:
        cooldown_left = cooldown_time - (time.time() - played_users[user_id])
        return message.reply(f"Ya jugaste hace poco, espera {int(cooldown_left)} segundos.")

    # Get the number to play with from the message text
    try:
        number = int(message.text.split()[1])
    except (ValueError, IndexError):
        return message.reply("Usa /dados [número] para jugar.")

    if not 1 <= number <= 20:
        return message.reply("El número debe estar entre 1 y 20.")

    # Roll the dice
    result = random.randint(1, 20)

    # Check if the user wins
    if result <= number and random.random() < win_prob:
        played_users[user_id] = time.time()  # record the play time
        return message.reply(f"Felicidades! Ganaste, el número era {result}. Vuelve a jugar en {cooldown_time} segundos.")

    # User loses
    return message.reply(f"Lo siento, perdiste. El número era {result}. Vuelve a intentarlo en {cooldown_time} segundos.")


# You can add more features or improvements as needed.
