import discord
from discord.ext import commands

class Poll:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll")
    async def poll(self, ctx):
        if not ctx.message.author.bot:
            await ctx.message.add_reaction('👍')
            await ctx.message.add_reaction('👎')
            await ctx.message.add_reaction('🤷')

def setup(bot):
    bot.add_cog(Poll(bot))
