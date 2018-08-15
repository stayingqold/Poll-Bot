import discord
from discord.ext import commands

class Meta:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll {title} [Option1] [Option2] [Option 3]', with up to 30 options.\n\n**Other Commands**\n+updates, +invite, +donate\n\n**Still Have Questions?**\nJoin our official discord server: <https://discord.gg/FhT6nUn>" + "\n" + "Ask us on twitter: <https://twitter.com/DiscordPollBot>", colour=0x83bae3)
        try:
            await ctx.author.send(embed=emb1)
            await ctx.message.channel.send('Check your DMs!')
        except discord.HTTPException:
            await ctx.message.channel.send(embed=emb1)

    @commands.command(name="invite")
    async def invite(self, ctx):
        emb1 = discord.Embed(description="Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>", colour=0x83bae3)
        await ctx.message.channel.send(embed=emb1)

    @commands.command(name="updates")
    async def updates(self, ctx):
        emb1 = discord.Embed(description="**Please join the Poll Bot server and see #announcements to see the latest updates! <https://discord.gg/FhT6nUn>**")
        await ctx.message.channel.send(embed=emb1)

    @commands.command(name="donate")
    async def donate(self, ctx):
        emb1 = discord.Embed(title='Donate', description="If you would like to support the development of Poll Bot you can donate via Patreon here: <https://patreon.com/pollbot>. Your donation will help pay the monthly server bill.\nCan't donate? Upvote Poll Bot here: https://discordbots.org/bot/298673420181438465/vote", color=0x83bae3)
        await ctx.message.channel.send(embed=emb1)

def setup(bot):
    bot.add_cog(Meta(bot))
