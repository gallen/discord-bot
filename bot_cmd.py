import discord
from dotenv import load_dotenv
import os
from math import *
from discord.ext import commands

# create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.command(help="Says hello world")
async def test(ctx):
    await ctx.send("Hello World!")
    
@bot.command(help="Echoes the message you send")
async def echo(ctx, *, arg):
    await ctx.send("Echo: " + arg)
    
@bot.command(help="Solves math problems")
async def math(ctx, *, arg):
    await ctx.send(":smile: " + str(eval(arg)) + " :smile:")

bot.run(token)

