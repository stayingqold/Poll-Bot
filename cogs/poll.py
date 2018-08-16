import discord
from discord.ext import commands

class Poll:
    def __init__(self, bot):
        self.bot = bot

    #there is probably a better way to do this
    emojiLetters = ["\N{REGIONAL INDICATOR SYMBOL LETTER A}", "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER C}", "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER E}", "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER G}", "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER I}", "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER K}", "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER M}", "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER O}", "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER Q}", "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER S}", "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER U}", "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER W}", "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
                    "\N{REGIONAL INDICATOR SYMBOL LETTER Y}", "\N{REGIONAL INDICATOR SYMBOL LETTER Z}"]

    @commands.command(name="poll")
    async def poll(self, ctx):
        if not ctx.message.author.bot:
            message = ctx.message.content
            if message.find("{") == -1:
                print(message.find("{"))
                await ctx.message.add_reaction('👍')
                await ctx.message.add_reaction('👎')
                await ctx.message.add_reaction('🤷')
            else:
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
                    pollMessage = ""

                    #there is probably a better way to do this
                    i = 0
                    for choice in option:
                        if len(option) > 26:
                            await ctx.message.channel.send("Maximum of 26 options")
                            return
                        elif not i==len(option)-1:
                            pollMessage = pollMessage + "\n\n" + self.emojiLetters[i] + " " + choice
                        i+=1


                    e=discord.Embed(title="**"+title+"**", description=pollMessage + "\n\n[Support the development of Poll Bot](https://patreon.com/pollbot)", colour=0x83bae3)
                    pollMessage = await ctx.message.channel.send(embed = e)
                    i = 0
                    for choice in option:
                        if not i==len(option)-1:
                            await pollMessage.add_reaction(self.emojiLetters[i])
                        i+=1


                #fix the message here
                except KeyError:
                    return "Please make sure you are using the format '+strawpoll {title} [Option1] [Option2] [Option 3]'"

def setup(bot):
    bot.add_cog(Poll(bot))
