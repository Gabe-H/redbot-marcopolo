from redbot.core import commands # pylint: disable=import-error
import random # pylint: disable=import-error
import discord # pylint: disable=import-error
import os.path # pylint: disable=import-error
from redbot.core.utils.menus import start_adding_reactions # pylint: disable=import-error
from redbot.core.utils.predicates import ReactionPredicate # pylint: disable=import-error
import asyncio # pylint: disable=import-error

class marco(commands.Cog):
    """Alternative to [p]ping"""

    @commands.command()
    async def drop(self, ctx): # ?drop command
        ctx.send('Polo!')