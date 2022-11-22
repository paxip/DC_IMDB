from setuptools import setup
from setuptools import find_packages

setup(
    name='imdb_scraper', 
    version='0.0.1', 
    description='Package allows you to find box office movies for each month of the years selected by the user',
    url='https://github.com/paxip/DC_IMDB', 
                                                                
    author='Isha Paik', 
    license='MIT',
    packages=find_packages(), 
    install_requires=['requests', 'selenium', 'typing' ], 
)