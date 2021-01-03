import discord
from discord.ext import commands
import logging
import aiohttp

# logging.basicConfig(level=logging.INFO)

extensions = (
    "cogs.poll", 
    "cogs.strawpoll", 
    "cogs.meta", 
    "cogs.owner"
    )

class PollBot(commands.AutoShardedBot):
    def __init__(self, config):
        prefixes = ["+", "poll:", "Poll:", "POLL:"]
        super().__init__(
            command_prefix = prefixes,
            status = discord.Status.online,
            activity = discord.Game(name = "+help"))
        self.config = config

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

    # @on_message.error
    # async def on_message_error(self, ctx, error):
    #     if isinstance(error, commands.CommandOnCooldown):
    #         await ctx.send('I could not find that member...')

    def run(self):
        super().run(self.config["discord_token"], reconnect=True)
