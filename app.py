import discord
from gmail_read import get_latest_code
from os import getenv

DISCORD_BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')

LISTENING_CHANNEL = getenv('LISTENING_CHANNEL')
LISTENING_PREFIX = getenv('LISTENING_PREFIX')
LISTENING_ROLE_NAME = getenv('LISTING_ROLE_NAME')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{LISTENING_PREFIX} help"))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    author_roles = [i.name for i in message.author.roles]
    if message.author == client.user or str(message.channel) != LISTENING_CHANNEL:
        return
    elif message.content.startswith(f"{LISTENING_PREFIX} ping"):
        await message.channel.send("Pong!")
    elif message.content.startswith(f"{LISTENING_PREFIX} help"):
        await message.channel.send("""```How to use:
-sy ping -> Tests bot connectivity. If the bot is OK, it will say Pong!
-sy code -> Sends latest login code to channel.
```
If you have a question or feedback, please contact with admin.""")
    elif not (LISTENING_ROLE_NAME in author_roles):
        await message.channel.send(f"{message.author.mention} your role is not authorized for this operation.")
        return
    elif message.content.startswith(f"{LISTENING_PREFIX} code"):
        data = get_latest_code()
        await message.channel.send(f"{message.author.mention} Latest StreamYard Code: ```{data[0]}``` Time: {data[1]}")

client.run(DISCORD_BOT_TOKEN)
