import discord
import os

client = discord.Client()
token = os.environ["RBOT1_TOKEN"]

@client.event
async def on_ready():
    print("I'm here")
    
@client.event
async def on_message(message):
    if message.content.startswith('こんにちは'):
        reply = 'こんにちにゃーん'
        await client.send_message(message.channel, reply)

client.run(token)
