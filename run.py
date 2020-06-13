from bot import SuperDuperBot
from config.config import cfg

if __name__ == "__main__":
    sdpbot = SuperDuperBot(
        token=cfg.data["discord_api_key"],
        command_prefix=cfg.data["command_prefix"])
    sdpbot.run()