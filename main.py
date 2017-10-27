import discord
from discord.ext import commands
import strawpoll
import asyncio
import inflect
import json
import requests
import config
import collections

description = '''A bot that creates polls or strawpolls using discord'''

bot = commands.AutoShardedBot(command_prefix='+/')

#Removes default help command

bot.remove_command("help")
c = collections.Counter()

#Log in
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='+/help', type=0))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    if hasattr(bot, 'app'):
        return
    bot.app = await bot.application_info()
    owner = bot.app.owner
    while True:
        guilds = 'guilds: ' + str(len(bot.guilds))
        users = 'users: ' + str(len(list(bot.get_all_members())))
        uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
        await owner.send(guilds)
        await owner.send(users)
        await owner.send(uniques)
        r = requests.post("https://bots.discord.pw/api/bots/{}/stats".format(bot.user.id), json={"server_count":len(bot.guilds)}, headers={"Authorization":config.pwtoken})
        print('wow it actually worked lmao')
        await asyncio.sleep(86400)

@bot.command(name='!start', pass_context=True)
async def start(ctx):
    bot.app = await bot.application_info()
    owner = bot.app.owner
    if ctx.message.author == owner:
        pollUses = "'+/poll' uses this week: " + str(c['pollUses'])
        supportUses = "'+/help' uses this week: " + str(c['supportUses'])
        await owner.send(pollUses)
        await owner.send(supportUses)
        c.clear()
        await asyncio.sleep(604800)
    else:
        return

#Sends a message to the bot owner saying how many servers and people are using Poll Bot
@bot.command(name='!analytics', pass_context=True)
async def srvrs(ctx):
    bot.app = await bot.application_info()
    owner = bot.app.owner
    guilds = 'guilds: ' + str(len(bot.guilds))
    users = 'users: ' + str(len(list(bot.get_all_members())))
    uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
    sender = 'sender: ' + str(ctx.message.author)
    await owner.send(guilds)
    await owner.send(users)
    await owner.send(uniques)
    await owner.send(sender)
    await owner.send('type +/!more for deeper analytics')
    r = requests.post("https://bots.discord.pw/api/bots/{}/stats".format(bot.user.id), json={"server_count":len(bot.guilds)}, headers={"Authorization":config.pwtoken})
    print('wow it actually worked lmao')

#more anayltics
@bot.command(name='!more', pass_context=True)
async def srvrs(ctx):
    bot.app = await bot.application_info()
    owner = bot.app.owner
    pollUses = "'+/poll' uses this week: " + str(c['pollUses'])
    supportUses = "'+/donate' uses this week: " + str(c['supportUses'])
    await owner.send(pollUses)
    await owner.send(supportUses)

#"Legacy" help command
@bot.command(name='pollbothelp', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+/poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+/strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+/updates, +/twitter, +/pollbotinfo, +/invite, +/support, +/server, +/contact\n\nStill Have Questions?**\nJoin our official discord server: <http://tinyurl.com/averagelyserver>" + "\n" + "Ask us on twitter: <https://twitter.com/averagely>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await ctx.author.send(embed=emb1)
    await ctx.message.channel.send('Check your DMs!')

#Help Command
@bot.command(name='help', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+/poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+/strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+/updates, +/twitter, +/pollbotinfo, +/invite, +/donate, +/server\n\n**Still Have Questions?**\nJoin our official discord server: <http://tinyurl.com/averagelyserver>" + "\n" + "Ask us on twitter: <https://twitter.com/averagely>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await ctx.author.send(embed=emb1)
    await ctx.message.channel.send('Check your DMs!')

#Link to the Poll Bot discord server
@bot.command(name='server', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can join the Poll Bot server here: <http://tinyurl.com/averagelyserver>')
    await ctx.message.channel.send(embed=emb1)

#For advertisements
@bot.command(name='donate', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(title='Support', description="*this is how we pay for Poll Bot's hosting!*\n\n**Support Averagely Bots on Patreon for some sweet rewards! https://www.patreon.com/averagely**", color=0x83bae3)
    await ctx.message.channel.send(embed=emb1)
    c['supportUses'] += 1

#Hidden command #1 - oceanman
@bot.command(name="oceanman", pass_context=True)
async def scrt(ctx):
    await ctx.message.channel.send("OCEAN MAN 🌊 😍 Take me by the hand ✋ lead me to the land that you understand 🙌 🌊 OCEAN MAN 🌊 😍 The voyage 🚲 to the corner of the 🌎 globe is a real trip 👌 🌊 OCEAN MAN 🌊 😍 The crust of a tan man 👳 imbibed by the sand 👍 Soaking up the 💦 thirst of the land 💯")

#Hidden command #2 - Clap This (taken from my other discord bot: https://github.com/finnreid19/Clap-Bot)
@bot.command(name='clapthis', pass_context=True)
async def scrt(ctx):
    content = ctx.message.content[10:] + ' '
    clapped = content.replace(" ", "👏")
    await ctx.message.channel.send(clapped)

#Contact
@bot.command(name='contact', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Email: contact@average.ly\nTwitter: <https://twitter.com/averagely> (DMs are open)\nDiscord server: <http://tinyurl.com/averagelyserver>', colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

#Invite link (if people want to add Poll Bot to their own server)
@bot.command(name='invite', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>', colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

#Poll Bot's twitter info
@bot.command(name='twitter', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can follow Averagely Bots on twitter here: <https://twitter.com/averagely>', colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)


#Info about Poll Bot
@bot.command(name='pollbotinfo', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description="This bot was created on 04/03/2017\nJoin the official discord server of Poll Bot: <http://tinyurl.com/averagelyserver>\nFollow Poll Bot on twitter: <https://twitter.com/averagely>\n**To help Poll Bot stay alive type '+donate'**", colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

@bot.command(name='strawpoll', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="Please add a number the # of choices you would like to have at the end of +strawpoll. eg. +strawpoll2", colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

#Where the latest updates get put
@bot.command(name='updates', pass_context=True)
async def updts(ctx):
    emb1 = discord.Embed(description="**Added +donate to pay for hosting for Poll Bot. Fixed the bug that made it so Poll Bot took answers from different channels**\n\n_**Don't forget you can use all of Poll Bot's features within direct messages. Just open a direct message with Poll Bot and use it like you would normally.**_")
    await ctx.message.channel.send(embed=emb1)

#Reaction Poll
@bot.command(name="poll", pass_context=True)
async def poll(ctx):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')
    await ctx.message.add_reaction('🤷')
    c['pollUses'] += 1

#Reaction Poll with 2 options
@bot.command(name="poll2", pass_context=True)
async def poll(ctx):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')

#Strawpoll
@bot.event
async def on_message(message):
    command_name = bot.command_prefix + 'strawpoll'

    if message.content.startswith(command_name):
        await process_strawpoll(message.content.split(command_name)[1], message)
    else:
        await bot.process_commands(message)

async def process_strawpoll(num_options: str, message):
    try:
        num_options = int(num_options)
    except ValueError:
        await message.channel.send('Please use only an integer number of options.')
        return

    if num_options not in range(2, 31):
        await message.channel.send('Your poll must have between 2 and 30 options.')
        return

    api = strawpoll.API()
    await message.channel.send('What would you like the title to be?')
    def pred(m):
        return m.author == message.author and m.channel == message.channel
    title = await bot.wait_for('message', check=pred)

    options = await ask_for_options(num_options, message)

    poll = strawpoll.Poll(title.content, options)
    poll = await api.submit_poll(poll)

    await message.channel.send(poll.url)


async def ask_for_options(num_options, message):
    p = inflect.engine()
    options = []

    for option_no in range(1, num_options + 1):
        await message.channel.send('What would you like the {} choice to be?'.format(p.ordinal(option_no)))
        def pred(m):
            return m.author == message.author and m.channel == message.channel
        reply = await bot.wait_for('message', check=pred)
        options.append(reply.content)

    return options

if __name__ == '__main__':
    bot.run(config.discordToken)
