import discord
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefic='&', intents=intents)

@bot.event
async def on_ready():
    print("All good.")

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.sent(file=picture)

bot.run("...")