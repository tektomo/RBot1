import discord
import os

client = discord.Client()
token = os.environ["RBOT1_TOKEN"]

@client.event
async def on_ready():
    print("Login successfull!")
    fmsg = "まじめまして！RBOTです！"
    await client.send_message(text_chat, fmsg)
    
@client.event
async def on_message(message):
    if message.content.startswith("にゃーん"):
        reply = "にゃーん"
        await client.send_message(message.channel, reply)

client.run(token)
