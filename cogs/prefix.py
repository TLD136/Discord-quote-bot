# By TLD136
# 25-2-2021
########################


import discord
from discord.ext import commands
import os
from time import sleep
import json


class prefix(commands.Cog):

    def __init__(self,client):
        self.client = client


    def get_prefix(self, client, message):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    

    @commands.command()
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix is verandert naar: {prefix}')


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '!'

        with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f , indent=4)



    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json' , 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f , indent=4)


def setup(client):
    client.add_cog(prefix(client))