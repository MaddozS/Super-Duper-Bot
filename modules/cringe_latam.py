import discord, asyncio, random
from utils import searches
from utils.image_search import img
from discord.ext import commands

class CringeLatam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Module Cringe Latam ready!")
    
    @commands.command(aliases=['chemopelon','pelon'])
    async def chemo(self, ctx):
        async with ctx.channel.typing():
            # Search from one of the possible options
            query = random.choice(searches.bald_search)

            # getting the title and the link of the image
            imgTitle, imgLink = img.search_images_google(query)
            
            print(f"{imgTitle}:\n\t{imgLink}")

            embed = discord.Embed(title="Chemo Pelon")
            embed.set_image(url=imgLink)
            embed.set_footer(text="Para todos su primera paja, para mi la de todos los días ❤")

            await asyncio.sleep(1)

            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(CringeLatam(client))
