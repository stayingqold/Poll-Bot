import discord
from discord.ext import commands


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        emb1 = discord.Embed(
            description="**Reaction Poll**\nCreate a reaction poll by typing `+poll *your message*`. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\nCreate a reaction poll with multiple options by typing `+poll {title} [Option1] [Option2] [Option3]`.\n\n**Strawpoll**\nCreate a strawpoll by typing `+strawpoll {title} [Option1] [Option2] [Option 3]`, with up to 30 options.\n\n**Other Commands**\n+invite, +donate, +partners\n\n**Still Have Questions?**\nJoin our Discord server: <https://discord.gg/FhT6nUn>"
            + "\n"
            + "Ask us on Twitter: <https://twitter.com/DiscordPollBot>",
            colour=0x83BAE3,
        )
        await ctx.message.channel.send(embed=emb1)

    @commands.command(name="donate")
    async def donate(self, ctx):
        emb1 = discord.Embed(
            description="**Donate**\nThank you for considering donating to Poll Bot. Your donation will help pay for the monthly server costs.\n\n"
                        + "Donation Platforms:\n"
                        + "Patreon: https://www.patreon.com/pollbot\n"
                        + "Ko-Fi (one-time paypal donations): https://ko-fi.com/pollbot\n"
                        + "Bitcoin Address: 3EPBikSQ9MTsHrnowLvPfe83uYZ4bFvohM\n"
                        + "Bitcoin (via Lightning Network): https://tippin.me/@stayingqold\n"
                        + "Ether: 0x00C78c405B21c120c921991906A61A52A1D1DC71",
            colour=0x83BAE3,
        )
        await ctx.message.channel.send(embed=emb1)

    @commands.command(name="partners")
    async def partners(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0x83bae3))

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/603292716691881988/603302880115687445/image0.jpg")
        embed.set_author(name="Poll Bot Partners", icon_url="https://pbs.twimg.com/profile_images/946629893458034688/os3gCiru_400x400.jpg")

        embed.add_field(name="Deployments.pro", value="We’re Deployments.pro! We offer inexpensive hosting services! Great uptime, lower cost. What have you got to lose?")
        embed.add_field(name="Links", value="Website: https://deployments.pro\nDiscord: https://discord.gg/7aVwdCN\nTwitter: https://twitter.com/deploymentsp")
        await ctx.message.channel.send(embed=embed)

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
