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











    @commands.command()
    async def clear(self, ctx, amount : int):
        amount = amount + 1
        await ctx.channel.purge(limit=amount)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong!")


def setup(client):
    client.add_cog(command(client))