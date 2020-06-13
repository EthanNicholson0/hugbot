import discord
from discord.ext import commands
from . import config

import random

prefixGlobal = "!"
bot = commands.Bot(command_prefix=prefixGlobal)

def main():
    bot.run(config.creds['discord_token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(description = "Hugs the target, or yourself if left blank")
async def hug(ctx):
    if ctx.message.mentions == []:
        await ctx.channel.send("You gave yourself a big hug. :)")
    else:
        huggee = ctx.message.mentions[0]
        await ctx.channel.send("{0}, {1} gave you a hug!".format(huggee.mention,ctx.author.mention))

@bot.command(description = "Makes the bot say you want a hug")
async def request(ctx):
    await ctx.channel.send("{0} wants a hug".format(ctx.author.mention))

@bot.command(description = "Reacts with :hugging:")
async def lonely(ctx):
    await ctx.channel.send(":hugging:")




#@bot.command(description="Spawns villager")
#async def spawn(ctx):
#    newVillager = villager.newVillager()
#    embed = discord.Embed()
#    embed.title = ("A villager has arrived in the campsite!")
#    embed.description = "Type ac!invite <name> to invite them to your island!"
#    embed.set_image(url = villager.getVillagerImage(newVillager))
#    return await ctx.channel.send(embed = embed)

#@bot.command(description = "Use prefix to change the bot prefix to suit your needs")
#async def prefix(ctx, *, message:str):
#    global prefixGlobal
#    prefixGlobal = message
#    await ctx.channel.send("Set bot prefix to: " + prefixGlobal)
