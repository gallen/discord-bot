from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key


messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you help me with some middle school homework question?"},
        {"role": "assistant", "content": "Sure. I would like!"},        
    ]

def chat(inp):
  messages.append({"role": "user", "content": inp})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )
  messages.append(response.choices[0].message)
  return response.choices[0].message.content

print(chat("What's the meaning of life?"))
print(chat("What's the meaning of your life?"))