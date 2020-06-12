import discord
from config.config import cfg
from discord.ext import commands
from discord.ext.commands import has_permissions
import os

sdpbot = commands.Bot(command_prefix='!!')

@sdpbot.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
    sdpbot.load_extension(f"modules.{extension.lower()}")
    await ctx.send(f"{ctx.message.author.mention} ha activado el módulo {extension.lower()}")
    print(f"Module {extension} is loaded!")

@sdpbot.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
    sdpbot.unload_extension(f"modules.{extension.lower()}")
    await ctx.send(f"{ctx.message.author.mention} ha desactivado el módulo {extension.lower()}")
    print(f"Module {extension} is unloaded!")

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Oye {ctx.message.author.mention}, no seas pendejo no tienes permisos, ¡no lo intentes de nuevo! <:prianbot:709840223856623646>")
        raise commands.MissingPermissions(["Administrator"])

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Oye {ctx.message.author.mention}, no seas pendejo no tienes permisos, ¡no lo intentes de nuevo! <:prianbot:709840223856623646>")
        raise commands.MissingPermissions(["Administrator"])

for filename in os.listdir('./modules'):
    if filename.endswith('.py') and filename != "__init__.py":
        sdpbot.load_extension(f'modules.{filename[:-3]}')

sdpbot.run(cfg.data["discord_api_key"])
