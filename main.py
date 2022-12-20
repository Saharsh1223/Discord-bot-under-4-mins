import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

token = os.environ['TOKEN']
bot.run(token)
