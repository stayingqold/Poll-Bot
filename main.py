#!/usr/bin/env python3

import discord
from discord.ext import commands
import strawpoll
import inflect

description = '''A bot that creates polls or strawpolls using discord'''

bot = commands.Bot(command_prefix='+')


# Log in
@bot.event
async def on_ready():
    print('----------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------')


#Reaction Poll
@bot.command(name="poll", pass_context=True)
async def poll(ctx):
        await bot.add_reaction(ctx.message, '👍')
        await bot.add_reaction(ctx.message, '👎')
        await bot.add_reaction(ctx.message, '🤷')


# Strawpoll
@bot.event
async def on_message(message):
    command_name = bot.command_prefix + 'strawpoll'
    
    if not message.content.startswith(command_name):
        return

    # get the stuff between 'strawpoll' and whitespace
    try:
        num_options = int(message.content.split()[0].replace(command_name, ''))
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



if __name__ == '__main__':
    import sys
    bot.run(sys.argv[1])
