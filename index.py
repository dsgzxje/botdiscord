
import discord
from discord.ext.commands import *

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("hello discord")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! My latency is **{0}**".format(round(bot.latency * 1000)))

@bot.command(aliases=['tx'])
async def taixiu



bot.run("OTk3Nzc2NzAzMDcxOTc3NTA0.GU1iNK.cnRJaLDIpAxX6rfKST0FUbTFXqNX9icD8gh_vA")