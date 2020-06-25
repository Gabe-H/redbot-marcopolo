from redbot.core import commands
import discord

class marco(commands.Cog):
    """Alternative to [p]ping"""

    @commands.command()
    async def marco(self, ctx): 
        await ctx.send('Polo!')