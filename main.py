import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intent=discord.Intents.default())

@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

token = os.environ['TOKEN']
bot.run(token)
