import discord
from discord.ext import commands
import config
import asyncio
import aiohttp
import config
import dbl


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dblpy = dbl.Client(self.bot, config.orgtoken)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.dblpy.post_guild_count()
        print("Guild joined")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.dblpy.post_guild_count()
        print("Guild removed")


def setup(bot):
    bot.add_cog(Stats(bot))
