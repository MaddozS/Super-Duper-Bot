import discord
from config.config import cfg
from discord.ext import commands
from discord.ext.commands import has_permissions
import os

# sdpbot = commands.Bot(command_prefix=cfg.data["command_prefix"])

class SuperDuperBot(commands.Bot):
    def __init__(self, token, command_prefix):
        self.token = token
        super().__init__(command_prefix)

    async def on_ready(self):
        for filename in os.listdir('./modules'):
            if filename.endswith('.py') and filename != "__init__.py":
                try:
                    self.load_extension(f'modules.{filename[:-3]}')
                    print(f"Module {filename} loaded!")
                except Exception as e:
                    print(e)
                    print(f"Module {filename} couldn't load!")
                
        print("-------------------BOT STARTED-------------------")

    def run(self):
        super().run(self.token)
