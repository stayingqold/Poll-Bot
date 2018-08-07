import discord
from discord.ext import commands

class Meta:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        if ctx.author.bot:
            print('bot tried to send message and was denied')
        else:
            emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll {title} [Option1] [Option2] [Option 3]', with up to 30 options.\n\n**Other Commands**\n+updates, +invite, +donate\n\n**Still Have Questions?**\nJoin our official discord server: <https://discord.gg/FhT6nUn>" + "\n" + "Ask us on twitter: <https://twitter.com/DiscordPollBot>", colour=0x83bae3)
            try:
                await ctx.author.send(embed=emb1)
                await ctx.message.channel.send('Check your DMs!')
            except discord.HTTPException:
                await ctx.message.channel.send(embed=emb1)

def setup(bot):
    bot.add_cog(Meta(bot))
