import os
from modules import helpers, smsmanager, database
from discord.ext import commands
from discord.utils import get
from discord import Client
from discord.abc import GuildChannel
from pprint import pprint

# Creates bot object, with command prefix to use like : $testCommand arg0 arg1 arg2  //"$#5GH{cz4VCfE@B7",
BOT = commands.Bot(command_prefix='$')

DB = database.DBManager()
SMS = smsmanager.SMS(DB)

TWILLIO_ERR_TEXT = "Error sending an SMS message :( \nwere the server's https://twillio.com credentials set with: \n```$authenticate <your sid> <your token> <your twillio_phone_number>``` \nEx: \n```$authenticate 123455 myt0k3n 123456789```"


@BOT.command(name="authenticate")
async def add_twillio_creds(ctx, sid, token, phonenumber):
    if helpers.isAdmin(ctx):
        DB.addAuth(str(ctx.guild.id), sid, token, phonenumber)
        await ctx.send("Twillio credentials + phone number noted!")
    else:
        await ctx.send("Only Admins can do that")


@BOT.command(name="join")
async def opt_in_to_smsing(ctx, phonenumber):
    serverID = str(ctx.guild.id)
    memberID = str(ctx.author.id)
    DB.addUserToOptedIn(serverID, memberID, phonenumber)
    try:
        SMS.send_text_message(serverID, phonenumber,
                              "You have signed up for {0}'s SMS notifcations!".format(ctx.guild.name))
        await ctx.send("Sent a confirmation message!")
    except:
        await ctx.send(TWILLIO_ERR_TEXT)


@BOT.event
async def on_ready():
    print("Logged in User: {0.user} | {0.user.id}".format(BOT))


@BOT.event
async def on_message(message):
    # prevents bot from responding to self
    if message.author.id == BOT.user.id:
        return
    await BOT.process_commands(message)

BOT.run(helpers.getSecretString("discord", "token"))
