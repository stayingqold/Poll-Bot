[![Discord Bots](https://discordbots.org/api/widget/298673420181438465.svg)](https://discordbots.org/bot/298673420181438465)

A Discord bot that lets you create strawpolls and reaction polls

Add Poll Bot to your server here: https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0

## How to use Poll Bot
Create a strawpoll by typing '+strawpoll {title} [Option1] [Option2] [Option 3]', with up to 26 options.


Create a reaction poll by typing '+poll _____’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷

Create a multi reaction poll type poll: {title} [option 1] [option 2] [option 3]
Add '+duration {hours}:{minutes}' to the message if you want the poll to end automatically (with*out* the {}). When the poll ends, the bot will send a message with a pie plot with the answers given in the channel of the poll.

## Requirements

- Python 3.5.2+
- `aiohttp` library
- `discord.py rewrite` library
- `matplotlib` library
- `numpy` library

Usually `pip` will work for these
