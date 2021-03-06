import discord
from discord.ext import commands
import os
from time import sleep
import json


class extra(commands.Cog):

    def __init__(self,client):
        self.client = client










def setup(client):
    client.add_cog(extra(client))