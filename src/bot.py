import os
from modules import helpers, smsmanager, database 
from discord.ext import commands
from discord.utils import get
from discord import Client

# Creates bot object, with command prefix to use like : $testCommand arg0 arg1 arg2  //"$#5GH{cz4VCfE@B7",
BOT = commands.Bot(command_prefix ='$')

DB = database.DBManager()
SMS = smsmanager.SMS(DB)

@BOT.command(name="authenticate")
async def add_twillio_creds(ctx, sid, token, phonenumber):
    DB.addAuth(ctx.guild.id, sid, token, phonenumber)
    await ctx.send("Twillio credentials + phone number noted!")

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
    
    await BOT.process_commands(message)

BOT.run(helpers.getSecretString("discord", "token"))