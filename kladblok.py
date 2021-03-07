# By TLD136
# 25-2-2021
########################


import discord
from discord.ext import commands
from time import sleep
import json

client = commands.Bot(command_prefix = '!')





@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('ja oke, maar hoeveel?')
    elif isinstance(error, commands.has_permissions):
        await ctx.send('bruh, je hebt geen rechten hiervoor')
    else:
        await ctx.send("er is iets mis gegaan")





@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)} ms")


#pizza time
@client.event
async def on_message(message):
    #to make sure it does not react to itself
    if message.author.id == client.user.id:
        return

    else ("pizza") in message.content.lower():
        await message.channel.send ('did someone say pizza?')
        sleep(1)
        await message.channel.send ('https://tenor.com/view/spider-man-pizza-time-pizza-day-pizza-dinner-gif-16271126')



@client.command()
async def clear(ctx, amount : int):
    await ctx.chanel.purge(limit=amount)






# code for per server prefixes


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]



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