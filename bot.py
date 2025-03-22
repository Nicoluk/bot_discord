import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@bot.command()
async def repeat(ctx, times: int,*, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$repeat'):
        # $repeat: Repite un mensaje varias veces.
        try:
            parts = message.content.split(' ', 2)
            times = int(parts[1])
            content = parts[2]
            for i in range(times):
                await message.channel.send(content)
        except Exception as e:
            await message.channel.send('Uso correcto: $repeat <veces> <mensaje>')
    else:
        await message.channel.send(message.content)

client.run("MTM1MDI1NjgzNjcwMzQyNDUyMg.GR3Gky.2srZ5AM4OYDGofW8YeA1ZLPvA6pezUJIqmfx_E")
