import os

class Config():
    def __init__(self):
        # print(os.environ)
        self.google_dev_api  = os.environ["GOOGLE_DEV_API"]
        self.google_cse      = os.environ["GOOGLE_CSE"]
        self.discord_api_key = os.environ["DISCORD_API_KEY"]

cfg = Config()
