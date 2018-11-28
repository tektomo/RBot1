import discord
import os
import re
from natto import MeCab
import random

client = discord.Client()
token = os.environ["RBOT1_TOKEN"]
m = MeCab()

def check_msg(sentence):
    me = m.parse(sentence)
    list1 = re.findall(".*名詞.*\n", me)
    list2 = []
    for word in list1:
        list2.append(word.split("\t"))
    list3 = []
    for i,word in enumerate(list2):
        list3.append(list2[i][0])
    
    result = list3[-1]
    
    print(list1)
    print(list2)
    print(list3)

    return result
    
@client.event
async def on_ready():
    print("Login successfull!")
    
@client.event
async def on_message(message):
    if client.user != message.author:
        print (message.content)
        result = check_msg(message.content)
        #result = m.parse(message.content)
        result = "今の話のテーマは" + result + "です"
        await client.send_message(message.channel, result)

client.run(token)
