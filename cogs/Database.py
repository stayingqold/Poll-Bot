import asyncpg
import asyncio
import datetime

"""
TABLES:

poll_bot_one
 guilds |             ts             
--------+----------------------------
      n | timestamp

poll_bot_two
 guilds |             ts             
--------+----------------------------
      n | timestamp

"""

class Database():

	def __init__(self, config):
		self.user = config["db"]["user"]
		self.password = config["db"]["password"]
		self.database = config["db"]["database"]
		self.host = config["db"]["host"]

	async def get_server_stats(self):
		self.conn = await asyncpg.connect(user = self.user, password = self.password, database = self.database, host = self.host)
		print(self.conn)
		poll_bot_one_stats = await self.conn.fetch('''SELECT * FROM poll_bot_one;''')
		poll_bot_two_stats = await self.conn.fetch('''SELECT * FROM poll_bot_two;''')
		await self.conn.close()
		return poll_bot_one_stats[len(poll_bot_one_stats)-1]["guilds"] + poll_bot_two_stats[len(poll_bot_two_stats)-1]["guilds"]

	# server_name is either poll_bot_one or poll_bot_two
	# server_name refers to the physical server, not the guild
	async def post_server_stats(self, server_name, num_guilds):
		self.conn = await asyncpg.connect(user = self.user, password = self.password, database = self.database, host = self.host)
		print(self.conn)
		await self.conn.execute(f"""
								INSERT INTO {server_name} (guilds, ts)
								VALUES ({num_guilds}, now())
								""")
									
		await self.conn.close()