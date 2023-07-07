import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(message.content)
  if message.content.startswith("$poke"):
    await message.channel.send("What is my purpose?")

client.run(os.getenv("TOKEN"))