import discord
from dotenv import load_dotenv
import os

# create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

# create bot client
client = discord.Client(intents=intents)

def on_ready():
    print(f"{client.user.name} logged in")

# log in
client.run(token)


