import discord
from discord.ext import commands
import strawpoll
import asyncio
import time
import inflect

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

#"Legacy" help command
@bot.command(name='pollbothelp', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+updates, +devinfo, +twitter, +pollbotinfo, +invite, +donate, +server, +contact\n\nStill Have Questions?**\nJoin our official discord server: <http://tinyurl.com/pollbotserver>" + "\n" + "Ask us on twitter: <https://twitter.com/pollbotapp>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await bot.whisper(embed=emb1)
    await bot.say('Check your DMs!')

#Help Command
@bot.command(name='help', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+strawpoll*#*', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+updates, +devinfo, +twitter, +pollbotinfo, +invite, +donate, +server\n\n**Still Have Questions?**\nJoin our official discord server: <http://tinyurl.com/pollbotserver>" + "\n" + "Ask us on twitter: <https://twitter.com/pollbotapp>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await bot.whisper(embed=emb1)
    await bot.say('Check your DMs!')

#Link to the Poll Bot discord server
@bot.command(name='server', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can join the Poll Bot server here: <http://tinyurl.com/pollbotserver>')
    await bot.say(embed=emb1)

#How people can donate to the bot
@bot.command(name='donate', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(title='Interested in donating?', description='If you would like to donate to help Poll Bot stay alive, click here: <https://cash.me/$q0w> or send money via PayPal to contact@average.ly, color=0x83bae3)
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
    emb1 = discord.Embed(description='Email: contact@average.ly\nTwitter: <https://twitter.com/pollbotapp> (DMs are open)\nDiscord server: <http://tinyurl.com/pollbotserver>', colour=0x83bae3)
    await bot.say(embed=emb1)

#Invite link (if people want to add Poll Bot to their own server)
@bot.command(name='invite', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>', colour=0x83bae3)
    await bot.say(embed=emb1)

#Poll Bot's twitter info
@bot.command(name='twitter', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can follow Poll Bot on twitter here: <https://twitter.com/PollBotApp>', colour=0x83bae3)
    await bot.say(embed=emb1)


#Info about Poll Bot
@bot.command(name='pollbotinfo', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description="This bot was created on 04/03/2017 by @finn#1327 (+devinfo)\nJoin the official discord server of Poll Bot: <http://tinyurl.com/pollbotserver>\nFollow Poll Bot on twitter: <https://twitter.com/PollBotApp>\n**To help Poll Bot stay alive type '+donate'**", colour=0x83bae3)
    await bot.say(embed=emb1)

@bot.command(name='strawpoll', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="Please add a number the # of choices you would like to have at the end of +strawpoll. eg. +strawpoll2", colour=0x83bae3)
    await bot.say(embed=emb1)

#Where the latest updates get put
@bot.command(name='updates', pass_context=True)
async def updts(ctx):
    emb1 = discord.Embed(description="**Added +help to help people who need help (+pollbothelp still works)\nAdded +donate, +rewards, and +donations so people can support Poll Bot\nAdded +devinfo so that people can contact the dev easier\nAdded +twitter so people can find Poll Bot's twitter\nAdded +pollbotinfo so people can see info about Poll Bot\nAdded +invite so that people can invite Poll Bot to their server\nAdded +server so people can more easily find the official Poll Bot server**\n\n_**Don't forget you can use all of Poll Bot's features within direct messages. Just open a direct message with Poll Bot and use it like you would normally.**_")
    await bot.say(embed=emb1)

#Sends a message to the bot owner saying how many servers and people are using Poll Bot
@bot.command(name='!servers', pass_context=True)
async def srvrs(ctx):
    await bot.send_message(bot.owner, len(bot.servers))
    await bot.send_message(bot.owner, len(bot.servers.members))

#Reaction Poll
@bot.command(name="poll", pass_context=True)
async def poll(ctx):
    await bot.add_reaction(ctx.message, '👍')
    await bot.add_reaction(ctx.message, '👎')
    await bot.add_reaction(ctx.message, '🤷')

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
    title = await bot.wait_for_message(author=message.author)

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

bot.run('Mjk3ODc3NTU0Nzk3MzQ2ODE2.DFe8EA.nHxmYOY81mxZ6UmZHvmicGLF1yU')
