import click
from nhentai.downloader import PictureDownloader
from nhentai.parser import get_pictures_info
from nhentai.utils import get_save_path, make_pdf


@click.command()
@click.option('--id', '-i', type=int, prompt='nhentai id',
              help='if the link is https://nhentai.net/g/90074/, then the id is 90074')
@click.option('--needpdf', '-n', is_flag=True, help='Do you need to pack these pictures into a pdf file?')
@click.option('--path', '-p',
              help="Where do you want to keep it? If you do not specify a location, it will create a new folder in the current folder, and save the files in it.")
@click.option('--threads', '-t', default=5, type=click.IntRange(1, 20))
def main(id, threads, path, needpdf):
    """nhentai downloader"""
    pictures_id, total_pages, pictures_name = get_pictures_info(id)
    path = get_save_path(path, id)
    task = PictureDownloader(pictures_id, total_pages,
                             threads, path)
    task.run()
    if needpdf:
        make_pdf(path, total_pages, pictures_name)


if __name__ == '__main__':
    main()
