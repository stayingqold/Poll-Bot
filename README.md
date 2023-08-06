## Poll Bot [ARCHIVED]
Poll Bot stopped running in July 2022. This repository is archived and will not be updated. If you want to run your own instance of Poll Bot, you can find the source code here, though there have been many breaking changes to the Discord API and discord.py since this repository was archived, so it will take some work to get it running again. Below is the old README.md.

## Poll Bot

Poll Bot is a Discord bot that lets you create strawpolls and reaction polls

Add Poll Bot to your server here: https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0

## How to use Poll Bot
Create a strawpoll by typing '+strawpoll {title} [Option1] [Option2] [Option 3]', with up to 26 options.


Create a reaction poll by typing '+poll _____’. Poll Bot will automatically add the reactions 👍, 👎, and 🤷

Create a multi reaction poll by typing +poll {title} [option 1] [option 2] [option 3]

## Installation
If you are running your own instance of Poll Bot, please 1) change the name and logo and 2) don't post it on bot listing sites unless you've made some changes to it.


### Install Requirements
Install python 3.5.3+

Install discord.py by doing something like this (depends on how you have python set up, but this generally will work):

```bash
python3 -m pip install -U discord.py
```

### Configure config.json
Add your discord token and sharding information to `config.json`. Your discord token can be found from the [applications page on discord.com](https://discord.com/developers/applications). Use 1 shard for every 1000 servers your bot is on (for example, if your bot is on 2,000 servers, `count` should be 2). If you are just running this for your own server, you are probably going to be safe using 1 shard with the id of 0, so your config file would look like this: 

```json
{
	"discord_token" : "your_token_here",
    "shards": {
        "count": 1,
        "first_shard_id": 0,
        "last_shard_id": 0
    }
}
```

Poll Bot is set up for [large bot sharding](https://discord.com/developers/docs/topics/gateway#sharding-for-very-large-bots), so the # of shards must be a multiple of 16. You likely won't have to worry about this.

### Running Poll Bot
Once you have installed the requirements and set up `config.json`, run `python3 launcher.py` to run the bot.


## License
MIT
