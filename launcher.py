# usage: python launcher.py num_shards first_shard_id:last_shard_id

import discord
from bot import PollBot
import sys
import json

with open('config.json') as config_file:
    config = json.load(config_file)

bot = PollBot(config)
bot.run()