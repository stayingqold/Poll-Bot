import discord
from discord.ext import commands
import config
import asyncio
import aiohttp
import config

class Stats:
    def __init__(self, bot):
        self.bot = bot

    async def send_stats(self):
        tokens = (
                    ("https://discordbots.org/api/bots/%s/stats", config.orgtoken),
                    ("https://bots.discord.pw/api/bots/%s/stats", config.pwtoken),
                    ("https://botsfordiscord.com/api/v1/bots/%s", config.botsfordiscordtoken)
                )

        payload = {"Content-Type": "application/json", "server_count": len(self.bot.guilds)}
        for url, token in tokens:
            headers = {"Authorization": token}
            await self.bot.http_session.post(url % self.bot.user.id, json=payload, headers=headers)


    async def on_guild_join(self, guild):
        await self.send_stats()

    async def on_guild_remove(self, guild):
        await self.send_stats()




def setup(bot):
    bot.add_cog(Stats(bot))
