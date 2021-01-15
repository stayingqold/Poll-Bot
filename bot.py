import discord
from discord.ext import commands
import logging
import aiohttp

#logging.basicConfig(level=logging.INFO)

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
        self.shard_count = self.config["shards"]["count"]
        shard_ids_list = []
        shard_ids = []
        
        # create list of shard ids
        for i in range(self.config["shards"]["first_shard_id"], self.config["shards"]["last_shard_id"]+1):
            shard_ids_list.append(i)
        self.shard_ids = tuple(shard_ids_list)

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
