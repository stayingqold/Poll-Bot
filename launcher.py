# usage: python launcher.py num_shards first_shard_id:last_shard_id

import discord
from bot import PollBot
import sys
try:
	num_shards = int(sys.argv[1])

	# In the format first_id:last_id
	shard_id_range = sys.argv[2]
	beginning = int(shard_id_range[0:shard_id_range.find(":")])
	end = int(shard_id_range[shard_id_range.find(":")+1:len(shard_id_range)])

	shard_ids_list = []
	shard_ids = []
	# create list of shard ids
	for i in range(beginning, end+1):
		shard_ids_list.append(i)

	# convert list to tuple
	shard_ids = tuple(shard_ids_list)

except:
	print("Add arguments for number of shards and the shard ID range\nEx: python3 launcher.py 10 0:9")
	exit()

bot = PollBot(num_shards, shard_ids)
bot.run()