import discord
import random

# Lista de emojis
emojis = ["😀", "😂", "🥳", "😎", "🔥", "❤️", "🚀", "🐱", "👻", "🎮"]

# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True

# Criar o bot
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    elif message.content.startswith('$bye'):
        await message.channel.send("🙂")

    elif message.content.startswith('$emoji'):
        emoji_aleatorio = random.choice(emojis)
        await message.channel.send(emoji_aleatorio)

    else:
        await message.channel.send(message.content)

client.run("SEU TOKEN DO BOT DEVE FICAR AQUI!")
