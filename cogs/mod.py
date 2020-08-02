import discord
from discord.ext import commands

#Our class for our commands cog
class Mod (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Bot command that will kick a member of a server if called upon with sufficient rights
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")
        
    #Bot command that will ban a member of a server if called upon with sufficient rights
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")
        
    #Bot command that will clear X amount of messages from a channel where X is an int
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages got deleted")

def setup(bot):
    bot.add_cog(Mod(bot))

