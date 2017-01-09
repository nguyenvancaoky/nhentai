import click
from nhentai.downloader import PictureDownloader
from nhentai.parser import get_pictures_info, get_save_path


@click.command()
@click.option('--path', help='PATH')
@click.option('--threads', default=5, help='THREADS')
@click.option('--id', type=int, prompt='nhentai id',
              help='ID')
def main(id, threads, path):
    """nhentai downloader"""
    pictures_id, total_pages = get_pictures_info(id)
    path = get_save_path(path, id)
    task = PictureDownloader(pictures_id, total_pages,
                             threads, path)
    task.run()
if __name__ == '__main__':
    main()
