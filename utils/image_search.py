from apiclient.discovery import build
from config.config import cfg
import random


class ImageSearch():
    def __init__(self):
        self.service = build("customsearch", "v1",
               developerKey=cfg.google_dev_api)

    def search(self, entry):
        res = self.service.cse().list(
            q=entry,
            cx=cfg.google_cse,
            searchType='image',
            num=10,
            start = random.choice(range(1,10)) * 10,
            safe= 'off'
        ).execute()

        return res

    def rand_image(self, entry):
        res = self.search(entry)

        rndImg = random.choice(res['items'])
        imgTitle, imgLink = rndImg['title'], rndImg['link']

        return imgTitle, imgLink

img = ImageSearch()