
from creates_list_of_movie_web_links import Web_link_scraper
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from typing import Any
import datetime
import json
import os
import requests
import time


class Data_scraper(Web_link_scraper):
    '''
    This class inherits the Web_link_scraper and iterates through each web link in the movie_link_list 
    scraping relevant data corresponding to each movie.

    Attributes:
    ----------
    
    This is a child class and inherits all attributes in the Web_link scraper class in addition
    to the attributes listed below.
    
    text_data_dictionary : dict
        Dictionary containing text data for each movie.

    movie_dictionary : dict
        Dictionary containing all data corresponding to each movie.

    timestamp : int
        Provides date and time that each movie link is scraped in the format: :%Y-%m-%d %H:%M:%S.  
    '''                                                                           
    def __init__(self):
        '''
        This function initializes the class by creating a dictionary for the text data, a dictionary for
        the movie data, and a timestamp.   
        '''
        super().__init__()
        self.image_and_text_dictionary = {}
        self.movie_dictionary = {}
        self.timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        self.file_path = os.path.join('raw_data', 'box_office_mojo')

    def __scrape_text_data_from_movie_links(self):
        '''
        This function scrapes text data from the table of values presented on each web page (movie_link) 
        and forms two lists; category headings and corresponding values. 
        The zip object passes both lists and yields tuples stored to text_dictionary. 
        
        Returns
        -------
            A dictionary of the movie's text data.
        
        '''
        summary_table = self.driver.find_element(by=By.XPATH, value='//div[@class="a-section a-spacing-none mojo-gutter mojo-summary-table"]')
        summary_values = summary_table.find_element(by=By.XPATH, value='//div[@class="a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile"]')
        div_tags = summary_values.find_elements(by=By.XPATH, value='./div[@class="a-section a-spacing-none"]')
        performance_summary_values = summary_table.find_element(by=By.XPATH, value='//div[@class="a-section a-spacing-none mojo-gutter mojo-summary-table"]')
        worldwide_values = performance_summary_values.find_element(by=By.XPATH, value='//div[3][@class="a-section a-spacing-none"]')
        worldwide_gross = worldwide_values.find_element(by=By.XPATH, value='span[1]/a').text
        self.category_heading_list.append(worldwide_gross)
        international_gross = worldwide_values.find_element(by=By.XPATH, value='span[2]/a/span').text
        self.category_value_list.append(international_gross)        

        for text in div_tags:
            category_heading = text.find_element(by=By.XPATH, value='span[1]').text
            self.category_heading_list.append(category_heading)
            category_value = text.find_element(by=By.XPATH, value='span[2]').text
            self.category_value_list.append(category_value)
              
        text_dictionary = dict(zip(self.category_heading_list, self.category_value_list))
        #print(text_dictionary)
        return text_dictionary
        
    def create_movie_dictionary(self):
        '''
        This function iterates through each web link stored in the movie_link_list, scrapes the movie names
        and calls relevant functions inside the class to:
        (i)     record the timestamp for each scrape,
        (ii)    scrape image data,
        (iii)   scrape all text data.  

        The movie-dictionary is created to organise and store all relevant data according 
        to each movie's name (serving as a unique id).  

        '''
        for link in (self.movie_link_list[0:3]):
            self.driver.get(link)
            time.sleep(4)
            div_tag = self.driver.find_element(by=By.XPATH, value='//div[@class="a-fixed-left-grid-col a-col-right"]')
            movie_name = div_tag.find_element(by=By.XPATH, value='h1[@class="a-size-extra-large"]').text      
            self.__create_timestamp_for_web_scrape()
            image_link = self.__scrape_image_data()
            self.image_and_text_dictionary = self.__scrape_text_data_from_movie_links()
            self.image_and_text_dictionary.update({'image_link':image_link})
            self.movie_dictionary.update({movie_name:self.image_and_text_dictionary})
        return self.movie_dictionary
            
    def __create_timestamp_for_web_scrape(self):   
        '''
        This function creates a timestamp for the web scrape of each movie web link. 

        '''   
        time_key = 'timestamp'
        self.category_heading_list.append(time_key)
        self.category_value_list.append(self.timestamp)

    def __scrape_image_data(self):
        '''
        The function scrapes the image data for each movie web link.
        
        Returns
        -------
            The image source is being returned.
        
        '''
        image_results = self.driver.find_element(By.XPATH, value = '//*[@class="a-section a-spacing-none mojo-posters"]')
        img_tag = image_results.find_element(by=By.TAG_NAME, value='img')
        src = img_tag.get_attribute('src')
        return src   
             
    def create_directories(self):
        '''
        Creates a main directory called 'raw data' before joining with another file path
        to creates a subdirectory called 'box_office_mojo.'

        '''
        if not os.path.exists('raw_data'):
            os.mkdir('raw_data')
            os.mkdir(self.file_path)            
            self.create_image_directory()
            self.save_to_json(str, Any, 4)
            
            
        else:
            print('raw_data directory already exists')
            self.driver.quit
        
    def save_to_json(self, file_path: str, object_to_save: Any, indent: int):
        '''
        Creates a file in the 'box_office_mojo' directory and writes 
        movie_dictionary to it in JSON format. The code is programmed to raise 
        an error if this is not executed.

        '''
        try:
            with open(os.path.join(self.file_path, 'data.json'), "w") as outfile:
                json.dump(self.movie_dictionary, outfile, indent=indent)
            return True
        
        except Exception as e:
            print(e)
            return False
  

    def create_image_directory(self, image_path='raw_data/box_office_mojo/images'):
        '''
        This function creates a directory called 'images' in the 'raw_data/box_office_mojo' directory,
        and then downloads the movie poster image for each movie in the movie dictionary and saves it in
        the 'images' directory
        '''        
        os.mkdir(image_path)
        for n, movie in enumerate(self.movie_dictionary.values(),1):
                timestr = self.timestamp
                self.download_image(movie['image_link'], f'raw_data/box_office_mojo/images/{timestr}_{n}.jpg')     
    
    def download_image(self, image_url: str, fp: str):
        '''
        Downloads the image from the url and saves it to the file path
        
        Parameters
        ----------
        image_url: str
            The URL of the image to download.
        fp: str
            file path
        
        '''
        image_data = requests.get(image_url, fp).content
        with open(fp, 'wb') as handler:
            handler.write(image_data)

        
if __name__ == '__main__':
    year_list = ['2017', '2018']
    imdb = Data_scraper()
    imdb._click_monthly_button()
    imdb._create_list_of_movie_links(year_list)
    imdb.create_movie_dictionary()
    imdb.create_directories()
