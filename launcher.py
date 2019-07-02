import discord
from bot import PollBot
import config
bot = PollBot()
bot.run(config.discordToken)