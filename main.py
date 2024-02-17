import discord
import asyncio
from discord import app_commands
from discord.ext import commands
import requests

# secret token
BOT_TOKEN = 'MTIwNjAxNDA2MTAxMjA1ODEyNw.Gi31oN.g9aEsaGoarlcnRE7hheujNj3bGAExJvYKWXJ7w'
GUILD_ID = 1206018127285067789

# innitialize the bot
class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix= commands.when_mentioned ,intents= discord.Intents.default())
        self.cog_list = ['cogs.PingCommand', 'cogs.ReactionCommand', 'cogs.SetURLCommand', 'cogs.CreateNewUser','cogs.TestScraping']

    async def setup_hook(self):
        for ext in self.cog_list:
            await self.load_extension(ext)

    async def on_ready(self):
        synced = await self.tree.sync()
        print('Bot is ready')


# set up client and command tree
client = Client()

# run the bots
client.run(BOT_TOKEN)
