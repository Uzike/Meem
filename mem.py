import discord
from discord.ext import commands 
from my_token import my_token
import os
from random import randint, choice 
import requests
from fayl import get_redd_mem

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print("All good.")

@bot.command('mem')
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.sent(file=picture)
    
@bot.command('random_mem')
asynd def random_mem(ctx):
    mems = os.listdir('images')
    meem = choice(mems)
    with open(f'images/{meem}', rb) as f:
                picture = discord.File(f)
    await ctx.send(file=picture)           

@bot.command('redd')
async def redd(ctx):
    image_url = get_redd_mem()
    await ctx.send(image_url)
              
bot.run("...")
