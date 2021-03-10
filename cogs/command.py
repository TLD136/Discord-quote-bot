# By TLD136
# 25-2-2021
########################


import discord
from discord.ext import commands
import os
from time import sleep
import json


class command(commands.Cog):

    def __init__(self,client):
        self.client = client



    @commands.command()         # this and the who am i command does not work yet
    async def quote(self, ctx, user):
        oldestMessage = None
        for channel in ctx.guild.text_channels:
            fetchMessage = await channel.history().find(lambda m: m.author.id == user.id)
            if fetchMessage == None:
                continue


            if oldestMessage != None:
                oldestMessage = fetchMessage
            else:
                if fetchMessage.created_at > oldestMessage.created_at:
                    oldestMessage = fetchMessage

        if (oldestMessage is not None):
            await ctx.send(f"Oldest message is {oldestMessage.content}")
        else:
            await ctx.send("No message found.")

    @commands.command()
    async def whoami(self, ctx, user):
        ctx.send(f'name: {user.name()}\n id: {user.id()}\n discriminator: {user.discriminator()}')



    @commands.command()
    async def clear(self, ctx, amount : int):
        amount = amount + 1
        await ctx.channel.purge(limit=amount)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong! {round(self.client.latency * 1000)} ms")


def setup(client):
    client.add_cog(command(client))