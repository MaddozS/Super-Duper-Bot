import discord, asyncio, random
from discord.ext import commands
import requests, json

class Memes(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def __check_format(self, filename):
        allowed_format = ('gif', 'jpeg', 'jpg', 'png')
        is_valid = False

        if filename.endswith(allowed_format):
            is_valid = True

        return is_valid 

    @commands.Cog.listener()
    async def on_ready(self):
        print("Module Text ready!")

    @commands.command(aliases=['cursedmeme'])
    async def cursed(self, ctx):
        async with ctx.channel.typing():
            
            r = requests.get("https://www.reddit.com/r/cursedmemes.json?sort=hot&t=week&limit=300", 
                                headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}).json()
            # print(json.dumps(r, indent=2))
            allposts = r["data"]["children"]

            allowed = None
            if not ctx.message.channel.is_nsfw():
                allowed = [ post for post in allposts if not post["data"]["over_18"] and self.__check_format(post["data"]["url"]) ]
            else:
                allowed = [ post for post in allposts if self.__check_format(post["data"]["url"])]

            if allowed:
                pick = random.choice(allowed)

                embed = discord.Embed(title = pick["data"]["title"])
                embed.set_image(url=pick["data"]["url"])
                embed.set_footer(text=f"Pedido por: {ctx.message.author.name}")

                print(pick["data"]["title"], " ", pick["data"]["url"])
                await asyncio.sleep(0.1)

                await ctx.send(embed=embed)
            else:
                await ctx.send("No se pudo encontrar ni una cuserd!")

def setup(client):
    client.add_cog(Memes(client))