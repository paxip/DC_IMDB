from setuptools import setup
from setuptools import find_packages

setup(
    name='imdb_scraper', ## This will be the name your package will be published with
    version='0.0.1', 
    description='Package allows you to find box office movies for each month of the years selected by the user',
    url='https://github.com/paxip/DC_IMDB', # Add the URL of your github repo if published 
                                                                   # in GitHub
    author='Isha Paik', # Your name
    license='MIT',
    packages=find_packages(), # This one is important to explain. See the notebook for a detailed explanation
    install_requires=['requests', 'selenium'], # For this project we are using two external libraries
                                                     # Make sure to include all external libraries in this argument
)