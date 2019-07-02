import discord
from discord.ext import commands
import logging
import config
import aiohttp

logging.basicConfig(level=logging.INFO)

extensions = (
    "cogs.poll", 
    "cogs.strawpoll", 
    "cogs.meta", 
    "cogs.stats", 
    "cogs.owner"
    )

class PollBot(commands.AutoShardedBot):
    def __init__(self):
        prefixes = ["+", "poll:", "Poll:", "POLL:"]
        super().__init__(
            command_prefix = prefixes,
            status = discord.Status.online,
            activity = discord.Game(name = "+help"))
        self.shard_count = 10
        self.shard_ids = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.remove_command("help")
        
        for extension in extensions:
            self.load_extension(extension)

    async def on_ready(self):
        self.http_session = aiohttp.ClientSession()
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("--------")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

    def run(self):
        super().run(config.discordToken, reconnect=True)
