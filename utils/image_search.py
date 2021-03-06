from apiclient.discovery import build
from config.config import cfg
import random


class ImageSearch():
    def __init__(self):
        self.service = build("customsearch", "v1",
               developerKey=cfg.data["google_api"])

    def search_images_google(self, entry):
        res = self.service.cse().list(
            q=entry,
            cx=cfg.data["google_cse"],
            searchType='image',
            num=10,
            start = random.choice(range(1,10)) * 10,
            safe= 'off'
        ).execute()

        return res

    def rand_search_image_google(self, entry):
        res = self.search_images_google(entry)

        rndImg = random.choice(res['items'])
        imgTitle, imgLink = rndImg['title'], rndImg['link']

        return imgTitle, imgLink

img = ImageSearch()