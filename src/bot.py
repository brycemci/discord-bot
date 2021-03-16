# https://discordpy.readthedocs.io/en/latest/api.html
# https://realpython.com/how-to-make-a-discord-bot-python/
# https://pythondiscord.com/pages/resources/guides/discordpy/

import os
import discord
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

MY_ID = os.getenv('MY_ID')
ASA_ID = os.getenv('ASA_ID')
ALEX_ID = os.getenv('ALEX_ID')
BIBLE_BOT = os.getenv('BIBLE_BOT')
TAUNT_BOT = os.getenv('TAUNT_BOT')

GENERAL_TEXT = os.getenv('GENERAL_TEXT')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!') and message.channel.id == GENERAL_TEXT:
        await message.delete()

    elif message.author.id == BIBLE_BOT:
        try:
            embed = message.embeds[0]
            field = embed.fields[0]
            await message.channel.send(field.value, tts=True)
        except:
            pass

client.run(TOKEN)
