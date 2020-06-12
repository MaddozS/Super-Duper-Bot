import discord, asyncio, random
from utils import searches
# from utils.image_search import img
from discord.ext import commands

class JoJo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Module JoJo ready!")

    @commands.command(aliases=['jojostand'])
    async def stand(self, ctx):
        async with ctx.channel.typing():
            stand_result = random.choice(list(searches.stands.keys()))
            img_stand = random.choice(searches.stands[stand_result])
            print(stand_result)
            embed = discord.Embed()
            embed.add_field(name="Your Stand!", value=f"**{ctx.message.author.mention}**, tu Stand es **{stand_result}**", inline=True)
            embed.set_image(url=img_stand)
            # embed.set_footer(text="Para todos su primera paja, para mi la de todos los días ❤")

            await asyncio.sleep(1)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(JoJo(client))