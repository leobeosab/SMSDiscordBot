import discord, os
from discord.ext import commands
from discord.utils import get
from discord import member



bot = commands.Bot(command_prefix ='.')

class MyClient(discord.Client):


    
    async def on_ready(self):

        print('ready')
    
    
    async def on_message(self, message):
        
        

        #prevents bot from responding to self
        if message.author.id == self.user.id:
            return
        
        if message.content.lower().startswith("hello <@592914379964678155>"):
            await message.channel.send('Hi {0.author.mention}'.format(message))
        
        if message.content.lower().startswith('list roles'):
            roles = ['']
            
            for member in message.server.members:
                for role in member.roles:
                        if not role in roles:
                            roles += role
            
            await message.channel.send('%d' %roles)


client = MyClient()
client.run(os.environ['TEXTEEBOTTOKEN'])