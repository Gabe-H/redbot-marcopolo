from .marco import marco


def setup(bot):
    n = marco(bot)
    bot.add_cog(n)