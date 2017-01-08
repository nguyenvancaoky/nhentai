import aiohttp
import asyncio
from tqdm import tqdm


class Fetch(object):

    def __init__(self, pictures_id, pictures_num, thread_num, saved_path):
        self.sema = asyncio.Semaphore(thread_num)
        self.pictures_num = pictures_num
        self.URL = 'https://i.nhentai.net/galleries/%d/{}.jpg' % pictures_id
        self.progress_bar = tqdm(total=pictures_num)

    async def fetch_async(self, a):
        async with aiohttp.get(self.URL.format(a)) as r:
            with open("{}.jpg".format(a), 'wb') as fd:
                while True:
                    chunk = await r.content.read(10)
                    if not chunk:
                        break
                    fd.write(chunk)

    async def print_progress(self, a):
        with (await self.sema):
            await self.fetch_async(a)
            self.progress_bar.update(1)

    def run(self):
        loop = asyncio.get_event_loop()
        task = asyncio.wait([self.print_progress(num)
                             for num in range(1, self.pictures_num + 1)])
        loop.run_until_complete(task)

    def __del__(self):
        self.progress_bar.close()

if __name__ == '__main__':
    job = Fetch(582776, 26, 5, "")
    job.run()
