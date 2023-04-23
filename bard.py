from dotenv import load_dotenv
from Bard import Chatbot
import os

load_dotenv("B_TOKEN")
token = os.getenv("B_TOKEN")

chatbot = Chatbot(token)

resp = chatbot.ask("Hello, how are you?")

i = 1