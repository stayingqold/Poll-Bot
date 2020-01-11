import discord
from discord.ext import commands
import asyncio

class BackgroundTasks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.update_server_count())

    @commands.Cog.listener(name='on_ready')
    async def update_server_count(self):
        while not self.bot.is_closed():
            headers = {"Authorization": self.bot.config["discordbotsorg_token"]}
            payload = {
                "Content-Type": "application/json",
                "server_count": len(self.bot.guilds),
            }
            await self.bot.http_session.post(
                    f"https://discordbots.org/api/bots/298673420181438465/stats", json=payload, headers=headers
            )
            await asyncio.sleep(3570)

            


def setup(bot):
    bot.add_cog(BackgroundTasks(bot))
