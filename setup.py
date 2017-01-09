from setuptools import setup, find_packages
from nhentai import __version__, __author__, __email__

setup(
    name='nhentai',
    version=__version__,
    description='nhentai.net downloader',
    long_description=open('README.md', 'r').read(),
    author=__author__,
    author_email=__email__,
    url='https://github.com/4cat/nhentai/',
    license='MIT',
    platforms='linux',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=open("requirements.txt").readlines(),
    keywords=['nhentai', 'downloader'],
    entry_points='''
        [console_scripts]
        nhentai=nhentai.commander:cli
    ''',
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
