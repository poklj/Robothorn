import discord
from discord.ext import commands

class Hawthorn:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hawthorn responsive")


def setup(bot):
    bot.add_cog(Hawthorn(bot))