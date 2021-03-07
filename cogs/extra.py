# By TLD136
# 25-2-2021
########################


import discord
from discord.ext import commands
import os
from time import sleep
import json


class extra(commands.Cog):

    def __init__(self, client):
        self.client = client

    #pizza time
    @commands.Cog.listener()
    async def on_message(self, message):
    #to make sure it does not react to itself
        if message.author.id == self.client.user:
            return

        elif ("pizza") in message.content.lower():
            await message.channel.send ('did someone say pizza?')
            sleep(1)
            await message.channel.send ('https://tenor.com/view/spider-man-pizza-time-pizza-day-pizza-dinner-gif-16271126')

        else:
            return




def setup(client):
    client.add_cog(extra(client))