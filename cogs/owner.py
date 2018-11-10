#thanks to evieepy on github https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be

from discord.ext import commands


class Owner:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "load", hidden = True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**")

    @commands.command(name = "unload", hidden = True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

def setup(bot):
    bot.add_cog(Owner(bot))
