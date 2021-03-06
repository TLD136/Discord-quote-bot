import discord
from discord.ext import commands
import os
from time import sleep
import json


class command(commands.Cog):

    def __init__(self,client):
        self.client = client



    @commands.command()
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix is verandert naar: {prefix}')



    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong!")


def setup(client):
    client.add_cog(command(client))