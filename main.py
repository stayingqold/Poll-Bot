import asyncio
from collections import Counter
import json
import logging

import aiohttp
import discord
from discord.ext import commands
import inflect
import strawpoll

import config


#prints out some useful info
#logging.basicConfig(level=logging.INFO)

bot = commands.AutoShardedBot(command_prefix='+/')

#Removes default help command
bot.remove_command("help")
c = Counter()

async def send_stats():
    tokens = (
        ('https://discordbots.org/api/bots/%s/stats', config.orgtoken),
        ('https://bots.discord.pw/api/bots/%s/stats', config.pwtoken),
    )
    payload = {'server_count': len(bot.guilds)}
    for url, token in tokens:
        headers = {'Authorization': token}
        await bot.session.post(url % bot.user.id, json=payload, headers=headers)

#Log in
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='+/help', type=0))
    bot.http_session = aiohttp.ClientSession()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    bot.app = await bot.application_info()
    owner = bot.app.owner
    while True:
        guilds = 'guilds: ' + str(len(bot.guilds))
        users = 'users: ' + str(len(list(bot.get_all_members())))
        uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
        await owner.send(guilds)
        await owner.send(users)
        await owner.send(uniques)
        await owner.send('type +/!more for deeper analytics')
        await send_stats()
        print(owner)
        await asyncio.sleep(86400)

@bot.event
async def on_guild_join(guild):
    print("New guild!")
    await send_stats()
    print("Stats updated.")

@bot.event
async def on_guild_remove(guild):
    print("Guild left :(")
    await send_stats()
    print("Stats updated.")

@bot.command(name="!upvoters", pass_context=True)
async def upv(ctx):
    chnl = bot.get_channel(396182828422922241)
    print(ctx.message.channel.id)
    await chnl.send("worked")
    r = requests.get("https://discordbots.org/api/bots/{}".format(bot.user.id), headers={"Authorization": config.orgtoken})
    numUps = r.json()['points']
    r = requests.get("https://discordbots.org/api/bots/{}/votes".format(bot.user.id), headers={"Authorization": config.orgtoken})
    upvoter = r.json()
    a = "upvoters: "
    for x in range(0, numUps):
        a += upvoter[x]['username'] + ", "
    await chnl.send(a)

#Sends a message to the bot owner saying how many servers and people are using Poll Bot
@bot.command(name='!stats', pass_context=True)
async def srvrs(ctx):
    chnl = bot.get_channel(396183943910522880)
    srvr = bot.get_guild(300487910619217921)
    bot.app = await bot.application_info()
    guilds = 'guilds: ' + str(len(bot.guilds))
    users = 'users: ' + str(len(list(bot.get_all_members())))
    uniques = 'unique users: ' + str(len(discord.utils._unique(bot.get_all_members())))
    await chnl.send(guilds)
    await chnl.send(users)
    await chnl.send(uniques)
    await chnl.send("server members: " + str(srvr.member_count))
    await chnl.send('type +/!mas for deeper analytics')

#more anayltics
@bot.command(name='!mas', pass_context=True)
async def srvrs(ctx):
    chnl = bot.get_channel(396183943910522880)
    pollUses = "'+/poll' uses this week: " + str(c['pollUses'])
    supportUses = "'+/donate' uses this week: " + str(c['supportUses'])
    await chnl.send(pollUses)
    await chnl.send(supportUses)

#Help Command
@bot.command(name='help', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="**Reaction Poll**\nCreate a reaction poll by typing '+/poll *your message*’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\n\n**Strawpoll**\nCreate a strawpoll by typing '+/strawpoll #', where # is the number of choices you want your strawpoll to have (between 2-30) and answer Poll Bot's questions.\n\n**Other Commands**\n+/updates, +/twitter, +/invite, +/donate\n\n**Still Have Questions?**\nJoin our official discord server: <https://discord.gg/FhT6nUn>" + "\n" + "Ask us on twitter: <https://twitter.com/DiscordPollBot>\n\n_**Don't forget you can use all of Poll Bot's commands inside this direct message.**_", colour=0x83bae3)
    await ctx.author.send(embed=emb1)
    await ctx.message.channel.send('Check your DMs!')

#For advertisements
@bot.command(name='donate', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(title='Support', description="Thanks for considering donating to Poll Bot! By donating, you would help pay for Poll Bot's monthly hosting bill.\n-\nYou can donate by sendng money here: https://cash.me/$finnreid19\n-\nIf you have any suggestions for rewards, join the Poll Bot discord server (https://discord.gg/FhT6nUn)\n-\nLove Poll Bot but don't want to donate?  Upvote it here: https://discordbots.org/bot/298673420181438465 (and get the upvoter role on the Poll Bot discord server: https://discord.gg/FhT6nUn)", color=0x83bae3)
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

#Invite link (if people want to add Poll Bot to their own server)
@bot.command(name='invite', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>', colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

#Poll Bot's twitter info
@bot.command(name='twitter', pass_context=True)
async def info(ctx):
    emb1 = discord.Embed(description='You can follow Poll Bot on twitter here: <https://twitter.com/DiscordPollBot>', colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

@bot.command(name='strawpoll', pass_context=True)
async def hlp(ctx):
    emb1 = discord.Embed(description="Please add a number the # of choices you would like to have at the end of +strawpoll. eg. +strawpoll2", colour=0x83bae3)
    await ctx.message.channel.send(embed=emb1)

#Where the latest updates get put
@bot.command(name='updates', pass_context=True)
async def updts(ctx):
    emb1 = discord.Embed(description="**Please join the Poll Bot server and see #change_log to see the latest updates! <https://discord.gg/FhT6nUn>**\n\n_**Don't forget you can use all of Poll Bot's features within direct messages. Just open a direct message with Poll Bot and use it like you would normally.**_")
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
