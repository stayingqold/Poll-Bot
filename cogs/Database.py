import asyncpg
import asyncio
#import config

"""
server_stats
 poll_bot_one | poll_bot_two | ts 
--------------+--------------+----
            y |            x |   z
x = # of guilds on poll bot server 1
y = # of guilds on poll bot server 2
z = date and time the value was added

"""
class Database():

	def __init__(self):
		return

	async def get_server_stats(self):
		self.conn = await asyncpg.connect(user = "username", password = "pwd", database = "db", host = "host")
		values = await self.conn.fetch('''SELECT * FROM server_stats''')
		return values[len(values)-1]["poll_bot_one"] + values[len(values)-1]["poll_bot_two"]