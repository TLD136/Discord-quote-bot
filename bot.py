# By TLD136
# 25-2-2021
########################


import discord
from discord.ext import commands
import os
from time import sleep
import json

def get_prefix(client, message):       #somehow did not work
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('I am a stupid bot'))
    print("Ready")


# code for per server prefixes
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f , indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json' , 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f , indent=4)


#load and unload the cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


f = open('token.txt','rt')
token = f.read(59)
f.close

client.run(token)