import os
import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)

admin_id = 505814544002842644
prefix = "+"
client = commands.Bot(command_prefix=commands.when_mentioned_or("+"),intents=intents)

@client.command()
async def load(ctx, extension):
  if ctx.author.id == admin_id:
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"**Successfully loaded:** `{extension}` !")
  else:
    await ctx.send("**Error**: Only bot admins can use this command.")

@client.command()
async def unload(ctx, extension):
  if ctx.author.id == admin_id:
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"**Successfully unloaded:** `{extension}` !")
  else:
    await ctx.send("**Error**: Only bot admins can use this command.")

@client.command()
async def reload(ctx, extension):
  if ctx.author.id == admin_id:
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"**Successfully reloaded:** `{extension}` !")
  else:
    await ctx.send("**Error**: Only bot admins can use this command.")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f"cogs.{filename[:-3]}")
    print(f"Successfully loaded {filename}\n")

client.run("<your bot token here>")
