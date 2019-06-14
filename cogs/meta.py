import discord
from discord.ext import commands


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        emb1 = discord.Embed(
            description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\nCreate a reaction poll with multiple options by typing `poll: {title} [Option1] [Option2] [Option3]`.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll {title} [Option1] [Option2] [Option 3]', with up to 30 options.\n\n**Other Commands**\n+updates, +invite\n\n**Still Have Questions?**\nJoin our Discord server: <https://discord.gg/FhT6nUn>"
            + "\n"
            + "Ask us on Twitter: <https://twitter.com/DiscordPollBot>",
            colour=0x83BAE3,
        )
        try:
            await ctx.author.send(embed=emb1)
            await ctx.message.channel.send("Check your DMs!")
        except discord.HTTPException:
            await ctx.message.channel.send(embed=emb1)

    @commands.command(name="invite")
    async def invite(self, ctx):
        emb1 = discord.Embed(
            description="Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>",
            colour=0x83BAE3,
        )
        await ctx.message.channel.send(embed=emb1)

    @commands.command(name="updates")
    async def updates(self, ctx):
        emb1 = discord.Embed(
            description="**Please join the Poll Bot server and see #announcements to see the latest updates! <https://discord.gg/FhT6nUn>**"
        )
        await ctx.message.channel.send(embed=emb1)


def setup(bot):
    bot.add_cog(Meta(bot))
