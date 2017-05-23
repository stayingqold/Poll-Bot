import discord
from discord.ext import commands
import strawpoll
import asyncio

description = '''A bot that creates polls or strawpolls using discord'''

bot = commands.Bot(command_prefix='+')

#Log in
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

#Reaction Poll
@bot.command(name="poll", pass_context=True)
async def poll(ctx):
        await bot.add_reaction(ctx.message, '👍')
        await bot.add_reaction(ctx.message, '👎')
        await bot.add_reaction(ctx.message, '🤷')

#StrawPoll with 2 options
@bot.command(name="strawpoll2", pass_context=True)
async def poll(ctx):
    api = strawpoll.API()
    await bot.say('What would you like the title to be?')
    title = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the first choice to be?')
    choice1 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the second choice to be?')
    choice2 = await bot.wait_for_message(author=ctx.message.author)
    p2 = strawpoll.Poll(title.content, [choice1.content, choice2.content])
    print(p2.id)
    print(p2.url)

    p2 = await api.submit_poll(p2)
    print(p2.id)
    print(p2.url)

    await bot.say(p2.url)

#StrawPoll with 3 options
@bot.command(name="strawpoll3", pass_context=True)
async def poll(ctx):
    api = strawpoll.API()
    await bot.say('What would you like the title to be?')
    title = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the first choice to be?')
    choice1 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the second choice to be?')
    choice2 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the third choice to be?')
    choice3 = await bot.wait_for_message(author=ctx.message.author)
    p2 = strawpoll.Poll(title.content, [choice1.content, choice2.content, choice3.content])
    print(p2.id)
    print(p2.url)

    p2 = await api.submit_poll(p2)
    print(p2.id)
    print(p2.url)

    await bot.say(p2.url)

#StrawPoll with 4 options
@bot.command(name="strawpoll4", pass_context=True)
async def poll(ctx):
    api = strawpoll.API()
    await bot.say('What would you like the title to be?')
    title = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the first choice to be?')
    choice1 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the second choice to be?')
    choice2 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the third choice to be?')
    choice3 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the fourth choice to be?')
    choice4 = await bot.wait_for_message(author=ctx.message.author)
    p2 = strawpoll.Poll(title.content, [choice1.content, choice2.content, choice3.content, choice4.content])
    print(p2.id)
    print(p2.url)

    p2 = await api.submit_poll(p2)
    print(p2.id)
    print(p2.url)

    await bot.say(p2.url)

#StrawPoll with 5 options
@bot.command(name="strawpoll5", pass_context=True)
async def poll(ctx):
    api = strawpoll.API()
    await bot.say('What would you like the title to be?')
    title = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the first choice to be?')
    choice1 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the second choice to be?')
    choice2 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the third choice to be?')
    choice3 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the fourth choice to be?')
    choice4 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the fifth choice to be?')
    choice5 = await bot.wait_for_message(author=ctx.message.author)
    p2 = strawpoll.Poll(title.content, [choice1.content, choice2.content, choice3.content, choice4.content, choice5.content])
    print(p2.id)
    print(p2.url)

    p2 = await api.submit_poll(p2)
    print(p2.id)
    print(p2.url)

    await bot.say(p2.url)

#StrawPoll with 6 options
@bot.command(name="strawpoll6", pass_context=True)
async def poll(ctx):
    api = strawpoll.API()
    await bot.say('What would you like the title to be?')
    title = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the first choice to be?')
    choice1 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the second choice to be?')
    choice2 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the third choice to be?')
    choice3 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the fourth choice to be?')
    choice4 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the fifth choice to be?')
    choice5 = await bot.wait_for_message(author=ctx.message.author)
    await bot.say('What would you like the sixth choice to be?')
    choice6 = await bot.wait_for_message(author=ctx.message.author)
    p2 = strawpoll.Poll(title.content, [choice1.content, choice2.content, choice3.content, choice4.content, choice5.content, choice6.content])
    print(p2.id)
    print(p2.url)

    p2 = await api.submit_poll(p2)
    print(p2.id)
    print(p2.url)

    await bot.say(p2.url)

bot.run('token')
