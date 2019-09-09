import discord
from discord.ext import commands
import asyncio
from cogs.Database import Database

class BackgroundTasks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = Database(self.bot.config)
        self.bg_task = self.bot.loop.create_task(self.update_server_count())

    @commands.Cog.listener(name='on_ready')
    async def update_server_count(self):
        while not self.bot.is_closed():
            await self.db.post_server_stats(self.bot.config["physical_server_name"], len(self.bot.guilds))
            print(len(self.bot.guilds))
            # This sleep makes sure both servers post their stats before we try to retrieve them
            await asyncio.sleep(30)
            num_guilds = await self.db.get_server_stats()
            headers = {"Authorization": self.bot.config["discordbotsorg_token"]}
            payload = {
                "Content-Type": "application/json",
                "server_count": num_guilds,
            }
            print(num_guilds)
            print(self.bot.user.id)
            z = await self.bot.http_session.post(
                    f"https://discordbots.org/api/bots/298673420181438465/stats", json=payload, headers=headers
            )
            print(z)
            print("AA")
            await asyncio.sleep(3570)

            


def setup(bot):
    bot.add_cog(BackgroundTasks(bot))
