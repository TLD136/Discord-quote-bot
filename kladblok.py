import discord
from discord.ext import commands
from time import sleep

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

    if str("pizza") in message.content.lower():
        await message.channel.send ('did someone say pizza?')
        sleep(1)
        await message.channel.send ('https://tenor.com/view/spider-man-pizza-time-pizza-day-pizza-dinner-gif-16271126')



@client.command()
async def clear(ctx, amount : int):
    await ctx.chanel.purge(limit=amount)


    