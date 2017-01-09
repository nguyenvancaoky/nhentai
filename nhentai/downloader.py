import os
import aiohttp
import asyncio
from tqdm import tqdm


class PictureDownloader(object):
    "Download pictures from nhentai."

    def __init__(self, pictures_id, pictures_num, thread_num, saved_path):
        self.sema = asyncio.Semaphore(thread_num)
        self.pictures_num = pictures_num
        self.URL = 'https://i.nhentai.net/galleries/%d/{}.jpg' % pictures_id
        self.saved_path = saved_path
        self.progress_bar = tqdm(total=pictures_num)

    async def fetch_async(self, picture_id):
        async with aiohttp.get(self.URL.format(picture_id)) as r:
            with open(os.path.join(self.saved_path, str(picture_id) + '.jpg'), 'wb') as fd:
                while True:
                    chunk = await r.content.read(10)
                    if not chunk:
                        break
                    fd.write(chunk)

    async def print_progress(self, picture_id):
        with (await self.sema):
            await self.fetch_async(picture_id)
            self.progress_bar.update(1)

    def run(self):
        loop = asyncio.get_event_loop()
        task = asyncio.wait([self.print_progress(picture_id)
                             for picture_id in range(1, self.pictures_num + 1)])
        loop.run_until_complete(task)

    def __del__(self):
        self.progress_bar.close()
        print("Pictures saved in:", self.saved_path)


if __name__ == '__main__':
    job = PictureDownloader(582776, 26, 10, "/home/overcat/nhentaipic")
    job.run()
