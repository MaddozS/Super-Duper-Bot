import discord, random, aiohttp, asyncio, modules
from utils.image_search import img
from config.config import cfg
from utils import searches
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Todo funcionando! ;)")

@client.command(aliases=['chemopelon','pelon'])
async def chemo(ctx):
    async with ctx.channel.typing():
        # Search from one of the possible options
        query = random.choice(searches.bald_search)

        # getting the title and the link of the image
        imgTitle, imgLink = img.rand_image(query)
        
        print(f"{imgTitle}:\n\t{imgLink}")

        embed = discord.Embed(title="Chemo Pelon")
        embed.set_image(url=imgLink)
        embed.set_footer(text="Para todos su primera paja, para mi la de todos los días ❤")

        await asyncio.sleep(1)

        await ctx.send(embed = embed)


client.run(cfg.discord_api_key)
