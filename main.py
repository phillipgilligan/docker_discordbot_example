#Needed imports
import discord
from discord.ext import commands
import random
import asyncio
import os

#Bot Prefix
bot = commands.Bot(command_prefix="!")

#Token location
TOKEN = open("TOKEN.txt", "r").read()

#init message when bot is launched
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print ("---------------")

#Bot status swapper, picks a random status every 15 seconds    
async def chng_pr():
    await bot.wait_until_ready()
    statuses = ["Docker Example", "Discord Bot Example", "With Code"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))      
        await asyncio.sleep(15)
 
#Code required to load and reload Cogs       
@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"{cog} reloaded")
    except Exception as e:
        print(f"{cog} failed to reload.")
        raise e

#Some error catching to prevent fatal crashes
for cog in os.listdir("cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

#Runnin our status loop
bot.loop.create_task(chng_pr())

#Passing in our tokken and bringing our bot online   
bot.run(TOKEN)

