import click
from nhentai.downloader import PictureDownloader
from nhentai.parser import get_pictures_info
from nhentai.utils import get_save_path, make_pdf
import time


@click.command()
@click.option('--pdf', is_flag=True)
@click.option('--path', help='PATH')
@click.option('--threads', default=5, help='THREADS')
@click.option('--id', type=int, prompt='nhentai id',
              help='ID')
def main(id, threads, path, pdf):
    """nhentai downloader"""
    pictures_id, total_pages, pictures_name = get_pictures_info(id)
    path = get_save_path(path, id)
    task = PictureDownloader(pictures_id, total_pages,
                             threads, path)
    task.run()
    if pdf:
        make_pdf(path, total_pages, pictures_name)

if __name__ == '__main__':
    main()
