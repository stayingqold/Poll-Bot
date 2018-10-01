import discord
from discord.ext import commands

class StrawPoll:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="strawpoll")
    async def strawpoll(self, ctx):
        if not ctx.message.author.bot:
            message = ctx.message.clean_content

            #gets the title of the poll
            first = message.find("{") + 1
            second = message.find("}")
            title = message[first:second]

            #gets the # of options and assigns them to an array
            newMessage = message[second:]
            loopTime = 0

            option = []
            for options in message:
                #get from } [option 1]
                #if newThis == -1:
                stillOptions = newMessage.find("[")
                if stillOptions != -1:
                    if loopTime == 0:
                        first = newMessage.find("[") + 1

                        second = newMessage.find("]")
                        second1 = second + 1
                        option.append(newMessage[first:second])

                        loopTime+=1
                    else:
                        newMessage = newMessage[second1:]
                        first = newMessage.find("[") + 1
                        second = newMessage.find("]")
                        second1 = second + 1
                        option.append(newMessage[first:second])
                        loopTime+=1

            try:
                async with self.bot.http_session.post('https://www.strawpoll.me/api/v2/polls', json = {"title": title, "options": option[:(len(option)-1)], "multi": "false"}, headers={"Content Type": "application/json"}) as resp:
                    json = await resp.json()
                    await ctx.message.channel.send("https://strawpoll.me/" + str(json["id"]))

            except strawpoll.errors.HTTPException:
                return "Please make sure you are using the format '+strawpoll {title} [Option1] [Option2] [Option 3]'"

            except KeyError:
                return "Please make sure you are using the format '+strawpoll {title} [Option1] [Option2] [Option 3]'"

def setup(bot):
    bot.add_cog(StrawPoll(bot))
