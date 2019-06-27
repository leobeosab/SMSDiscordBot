import discord, os
from discord.ext import commands
from discord.utils import get
from discord import Client

# Creates bot object, with command prefix to use like : $testCommand arg0 arg1 arg2
BOT = commands.Bot(command_prefix ='$')

@BOT.event
async def on_ready():
    print("Logged in User: {0.user} | {0.user.id}".format(BOT))

@BOT.event
async def on_message(message):
    #prevents bot from responding to self
    if message.author.id == BOT.user.id:
        return
    
    if message.content.lower().startswith("hello <@{0}>".format(BOT.user.id)):
        await message.channel.send('Hi {0.author.mention}'.format(message))
    
    if message.content.lower().startswith('list roles'):
        roles = ['']
        
        for member in message.server.members:
            for role in member.roles:
                    if not role in roles:
                        roles += role
        
        await message.channel.send('%d' %roles)

BOT.run(os.environ['TEXTEEBOTTOKEN'])