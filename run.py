import discord
from discord.ext import commands
import logging
import config
import aiohttp

logging.basicConfig(level=logging.INFO)

bot = commands.AutoShardedBot(command_prefix="+", status=discord.Status.online, activity=discord.Game(name='+help'))

extensions = (
                'cogs.poll',
                'cogs.strawpoll'
            )


@bot.event
async def on_ready():
    bot.http_session = aiohttp.ClientSession()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

def main():
    for extension in extensions:
        bot.load_extension(extension)
    bot.run(config.discordToken)
main()
