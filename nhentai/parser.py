from urllib.request import Request, urlopen
from lxml import etree

nhentai_url = 'https://nhentai.net/g/{}/'


def get_pictures_info(id):
    print("Getting the necessary information...")
    page = urlopen(Request(nhentai_url.format(id), headers={
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}))
    selector = etree.HTML(page.read().decode('utf-8'))
    title1 = selector.xpath('//*[@id="info"]/h1/text()')[0]
    title2 = selector.xpath('//*[@id="info"]/h2/text()')[0]
    pictures_id = int(selector.xpath(
        '//*[@id="cover"]/a/@href')[0].split('/')[2])
    total_pages = selector.xpath(
        '//*[@id="info"]/div[1]/text()')[0].split(' ')[0]
    print("Title:\n" + title1 + "\n" + title2)
    print("Total pages:", total_pages)
    print("Pictures id:", pictures_id)
    info = {
        "pictures_id": pictures_id,
        "total_pages": total_pages
    }
    return info

if __name__ == '__main__':
    get_pictures_info(90074)
