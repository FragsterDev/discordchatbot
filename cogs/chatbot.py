import discord
from discord.ext import commands
import requests
import asyncio

class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.channel.id != 946298771325743134:
            return
        if len(message.content) < 0:
            return
        else:
            idd = message.author.id
            msg = message.content
            r = requests.get(url=f"http://api.brainshop.ai/get?bid=161152&key=wLzpiJnuHhBT6J6m&uid={idd}&msg={msg}")
            reply = r.json()['cnt']
            async with message.channel.typing():
                await asyncio.sleep(1)
            await message.reply(f"{reply}")

def setup(client):
    client.add_cog(Chatbot(client))
