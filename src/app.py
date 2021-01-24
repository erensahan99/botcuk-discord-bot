import os

import discord
from discord.ext import commands

# from dotenv import load_dotenv

# load_dotenv()

token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("I'm ready!!!")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Naparsınız uşaklar😋"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command(name="ping")
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

client.run(token)