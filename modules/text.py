import discord, asyncio, random
from discord.ext import commands

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Module Text ready!")

    @commands.command(aliases=['mocking'])
    async def spongebob(self, ctx, *, txt: str):
        async with ctx.channel.typing():
            new_txt = ''.join(map(
                lambda c: c.upper() if random.random() < 0.5 else c.lower(), txt))

            await ctx.message.delete()
            await asyncio.sleep(0.01)

            await ctx.send(new_txt)

    @commands.command()
    async def say(self, ctx, *, txt: str):

        if txt == "":
            await ctx.send(f'{ctx.message.author.mention} ¡PERO PONLE TEXTO PELOTUDO!')
        else:
            await ctx.message.delete()
            await ctx.send(txt)

def setup(client):
    client.add_cog(Text(client))