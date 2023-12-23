import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def name(ctx):
    await ctx.send(f'Merhaba {user}! kodlanda hos geldiniz!')

@bot.command()
async def (ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")
