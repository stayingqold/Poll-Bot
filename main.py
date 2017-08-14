import discord
from discord.ext import commands
import discord
from discord.ext import commands
import strawpoll
import asyncio
import time
import inflect
import json
import requests
import config

description = '''A bot that creates polls or strawpolls using discord'''

bot = commands.Bot(command_prefix='+')

#Removes default help command
bot.remove_command("help")

#Log in
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='+help'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    if hasattr(bot, 'app'):
        return
    bot.app = await bot.application_info()
    bot.owner = bot.app.owner
    while True:
        servers = 'servers: ' + str(len(bot.servers))
        users = 'users: ' + str(len(list(bot.get_all_members())))
        uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
        await bot.send_message(bot.owner, servers)
        await bot.send_message(bot.owner, users)
        await bot.send_message(bot.owner, uniques)
        r = requests.post("https://bots.discord.pw/api/bots/{}/stats".format(bot.user.id), json={"server_count":len(bot.servers)}, headers={"Authorization":config.pwtoken})
        print('wow it actually worked lmao')
        await asyncio.sleep(86400)


#Sends a message to the bot owner saying how many servers and people are using Poll Bot
@bot.command(name='!analytics', pass_context=True)
async def srvrs(ctx):
        servers = 'servers: ' + str(len(bot.servers))
        users = 'users: ' + str(len(list(bot.get_all_members())))
        uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
        sender = 'sender: ' + str(ctx.message.author)
        await bot.send_message(bot.owner, servers)
        await bot.send_message(bot.owner, users)
        await bot.send_message(bot.owner, uniques)
        await bot.send_message(bot.owner, sender)
        r = requests.post("https://bots.discord.pw/api/bots/{}/stats".format(bot.user.id), json={"server_count":len(bot.servers)}, headers={"Authorization":config.pwtoken})
        print('wow it actually worked lmao')


#"Legacy" help command
@bot.command(name='pollbothelp', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+updates, +devinfo, +twitter, +pollbotinfo, +invite, +support, +server, +contact\n\nStill Have Questions?**\nJoin our official discord server: <http://tinyurl.com/averagelyserver>" + "\n" + "Ask us on twitter: <https://twitter.com/averagely>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await bot.whisper(embed=emb1)
    await bot.say('Check your DMs!')

#Help Command
@bot.command(name='help', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+updates, +devinfo, +twitter, +pollbotinfo, +invite, +support, +server\n\n**Still Have Questions?**\nJoin our official discord server: <http://tinyurl.com/averagelyserver>" + "\n" + "Ask us on twitter: <https://twitter.com/pollbotapp>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await bot.whisper(embed=emb1)
    await bot.say('Check your DMs!')

#Link to the Poll Bot discord server
@bot.command(name='server', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can join the Poll Bot server here: <http://tinyurl.com/averagelyserver>')
    await bot.say(embed=emb1)

#For advertisements
@bot.command(name='support', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(title='Support', description="*this is how we pay for Poll Bot's hosting!*\n\n**Support Averagely Bots on Patreon for some sweet rewards! https://www.patreon.com/averagely**", color=0x83bae3)
    await bot.say(embed=emb1)

#Hidden command #1 - oceanman
@bot.command(name="oceanman", pass_context=True)
async def scrt(ctx):
    await bot.say("OCEAN MAN 🌊 😍 Take me by the hand ✋ lead me to the land that you understand 🙌 🌊 OCEAN MAN 🌊 😍 The voyage 🚲 to the corner of the 🌎 globe is a real trip 👌 🌊 OCEAN MAN 🌊 😍 The crust of a tan man 👳 imbibed by the sand 👍 Soaking up the 💦 thirst of the land 💯")

#Hidden command #2 - Clap This (taken from my other discord bot: https://github.com/finnreid19/Clap-Bot)
@bot.command(name='clapthis', pass_context=True)
async def scrt(ctx):
    content = ctx.message.content[10:] + ' '
    clapped = content.replace(" ", "👏")
    await bot.say(clapped)

#If people need to contact me
@bot.command(name='devinfo', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='This bot was created by @finn#1327\nEmail him: finn@freid.co\nTroll him at <https://twitter.com/finnreid19>\nHe can make you custom bots that do what you want. Email him for pricing.', colour=0x83bae3)
    await bot.say(embed=emb1)

#Contact
@bot.command(name='contact', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Email: contact@average.ly\nTwitter: <https://twitter.com/averagely> (DMs are open)\nDiscord server: <http://tinyurl.com/averagelyserver>', colour=0x83bae3)
    await bot.say(embed=emb1)

#Invite link (if people want to add Poll Bot to their own server)
@bot.command(name='invite', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>', colour=0x83bae3)
    await bot.say(embed=emb1)

#Poll Bot's twitter info
@bot.command(name='twitter', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can follow Averagely Bots on twitter here: <https://twitter.com/averagely>', colour=0x83bae3)
    await bot.say(embed=emb1)


#Info about Poll Bot
@bot.command(name='pollbotinfo', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description="This bot was created on 04/03/2017 by @finn#1327 (+devinfo)\nJoin the official discord server of Poll Bot: <http://tinyurl.com/averagelyserver>\nFollow Poll Bot on twitter: <https://twitter.com/averagely>\n**To help Poll Bot stay alive type '+donate'**", colour=0x83bae3)
    await bot.say(embed=emb1)

@bot.command(name='strawpoll', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="Please add a number the # of choices you would like to have at the end of +strawpoll. eg. +strawpoll2", colour=0x83bae3)
    await bot.say(embed=emb1)

#Where the latest updates get put
@bot.command(name='updates', pass_context=True)
async def updts(ctx):
    emb1 = discord.Embed(description="**Added +support to pay for hosting for Poll Bot. Fixed the bug that made it so Poll Bot took answers from different channels**\n\n_**Don't forget you can use all of Poll Bot's features within direct messages. Just open a direct message with Poll Bot and use it like you would normally.**_")
    await bot.say(embed=emb1)

#Reaction Poll
@bot.command(name="poll", pass_context=True)
async def poll(ctx):
    await bot.add_reaction(ctx.message, '👍')
    await bot.add_reaction(ctx.message, '👎')
    await bot.add_reaction(ctx.message, '🤷')

#Reaction Poll with 2 options
@bot.command(name="poll2", pass_context=True)
async def poll(ctx):
    await bot.add_reaction(ctx.message, '👍')
    await bot.add_reaction(ctx.message, '👎')

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
        await bot.send_message(message.channel, 'Please use only an integer number of options.')
        return

    if num_options not in range(2, 31):
        await bot.send_message(message.channel, 'Your poll must have between 2 and 30 options.')
        return

    api = strawpoll.API()
    await bot.send_message(message.channel, 'What would you like the title to be?')
    title = await bot.wait_for_message(channel=message.channel, author=message.author)

    options = await ask_for_options(num_options, message)

    poll = strawpoll.Poll(title.content, options)
    poll = await api.submit_poll(poll)

    await bot.send_message(message.channel, poll.url)


async def ask_for_options(num_options, message):
    p = inflect.engine()
    options = []

    for option_no in range(1, num_options + 1):
        await bot.send_message(message.channel, 'What would you like the {} choice to be?'.format(p.ordinal(option_no)))
        reply = await bot.wait_for_message(author=message.author)
        options.append(reply.content)

    return options

if __name__ == '__main__':
    bot.run(config.discordToken)
