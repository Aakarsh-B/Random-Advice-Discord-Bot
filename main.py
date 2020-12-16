import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def getquote():
  response = requests.get("https://api.adviceslip.com/advice")
  json_data = json.loads(response.text)
  quote = json_data['slip']['advice']
  return (quote)

  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg=message.content

  if msg.startswith('!advice'):
    quote = getquote()
    await message.channel.send(quote)

keep_alive()
client.run(os.getenv('TOKEN'))