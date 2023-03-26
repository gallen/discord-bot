from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you help me with some middle school homework question?"},
        {"role": "assistant", "content": "Sure. I would like!"},
        {"role": "user", "content": "How DNA works?"}        
    ]
)

print(response.choices[0].message.content)