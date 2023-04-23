import discord
from dotenv import load_dotenv
import os
from math import *
from discord.ext import commands
import openai
import time

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you help me with some middle school homework question?"},
        {"role": "assistant", "content": "Sure. I would like!"},        
    ]

# Goal: Reset the conversation after 5 minutes idle

chat_timestamp = time.time() # time of last chat message

def resetConversationIfExpired():
    global chat_timestamp
    global messages
    cur_time = time.time()
    if cur_time - chat_timestamp > 300: # reset history message
        messages = messages[:3]
        print("Resetting conversation history")
    chat_timestamp = cur_time

def chat(inp):
  resetConversationIfExpired()
  messages.append({"role": "user", "content": inp})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )
  messages.append(response.choices[0].message)
  return response.choices[0].message.content

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
    
@bot.command(help="Chatgpt answer")
async def ai(ctx, *, arg):
    await ctx.send(chat(arg))

bot.run(token)

