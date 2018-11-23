import discord
import asyncio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Poll:
    def __init__(self, bot):
        self.bot = bot

    # there is probably a better way to do this
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

    async def on_message(self, message):
        if not message.author.bot:
            if message.content.startswith("+poll") or message.content.startswith("poll:") or message.content.startswith("Poll:") or message.content.startswith("+poll:") or message.content.startswith("+Poll:"):
                messageContent = message.clean_content
                if messageContent.find("{") == -1:
                    await message.add_reaction('👍')
                    await message.add_reaction('👎')
                    await message.add_reaction('🤷')
                else:
                    first = messageContent.find("{") + 1
                    second = messageContent.find("}")
                    title = messageContent[first:second]

                    # gets the # of options and assigns them to an array
                    newMessage = messageContent[second:]
                    loopTime = 0

                    option = []
                    for options in messageContent:
                        # get from } [option 1]
                        # if newThis == -1:
                        stillOptions = newMessage.find("[")
                        if stillOptions != -1:
                            if loopTime == 0:
                                first = newMessage.find("[") + 1
                                second = newMessage.find("]")
                                second1 = second + 1
                                option.append(newMessage[first:second])
                                loopTime += 1
                            else:
                                newMessage = newMessage[second1:]
                                first = newMessage.find("[") + 1
                                second = newMessage.find("]")
                                second1 = second + 1
                                option.append(newMessage[first:second])
                                loopTime += 1

                    try:
                        pollMessage = ""

                        # there is probably a better way to do this
                        i = 0
                        for choice in option:
                            if not option[i] == "":
                                if len(option) > 20:
                                    await message.channel.send("Maximum of 20 options")
                                    return
                                elif not i == len(option) - 1:
                                    pollMessage = pollMessage + "\n\n" + self.emojiLetters[i] + " " + choice
                            i += 1

                        e = discord.Embed(title="**" + title + "**",
                                          description=pollMessage + "\n\n[Support the development of Poll Bot](https://goo.gl/ZgowAJ)",
                                          colour=0x83bae3)
                        pollMessage = await message.channel.send(embed=e)
                        i = 0
                        final_options = []  # There is a better way to do this for sure, but it also works that way
                        for choice in option:
                            if not i == len(option) - 1 and not option[i] == "":
                                final_options.append(choice)
                                await pollMessage.add_reaction(self.emojiLetters[i])
                            i += 1

                        if '+duration' in message.content:
                            messageWords = message.content.split(' ')
                            for i in messageWords:
                                if i == '+duration':
                                    time = messageWords[messageWords.index(i) + 1]
                            time = time.split(':')
                            timeSeconds = int(time[0]) * 60 * 60 + int(time[1]) * 60
                            await asyncio.sleep(timeSeconds)
                            pollMessage = await pollMessage.channel.get_message(pollMessage.id)
                            reactions = []
                            for reaction in pollMessage.reactions:
                                async for user in reaction.users():
                                    if user == self.bot.user:
                                        reactions.append(reaction.count-1) #-1 deletes the bot's reactions
                            #adds up the number of reactions, if the # of reactions is 0 nothing gets sent
                            j = 0
                            for i in range(len(reactions)):
                                j+=reactions[i]

                            if not j == 0: #if only the bot has reactions, nothing gets sent
                                plt.subplots(figsize=(9, 6))
                                plt.bar(final_options, reactions, width=0.8, bottom=0)
                                plt.title(title, fontsize=27)
                                plt.savefig('results.png')
                                print(reactions)
                                print(final_options)
                                await message.channel.send('Results for a passed poll created by: <@' + str(message.author.id) + ">", file=discord.File('results.png'))
                                if '+keep' not in message.content:
                                    await pollMessage.delete()

                    except KeyError:
                        return "Please make sure you are using the format 'poll: {title} [Option1] [Option2] [Option 3]'"
            else:
                return

    def form(self, pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)


def setup(bot):
    bot.add_cog(Poll(bot))
