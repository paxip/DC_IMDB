from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
import time
import datetime
import json
import os
import requests




# The class creates a list of movie links for a list of years that you specify, scrapes the movie
# links from the IMDB website, scrapes the movie name, image data, and text data from the movie links,
# creates a timestamp for the web scrape, creates a dictionary of the movie name and image and text
# data, creates a directory called 'raw_data' and then creates a subdirectory called 'box_office_mojo'
# inside of it, creates a file called 'data.json' inside of the 'box_office_mojo' directory and writes
# the movie dictionary to it, and finally, creates a directory called 'images' inside of the
# 'box_office_mojo' directory.
# The class creates a list of movie links for a list of years that you specify
class Web_link_scraper:
    '''
    This class scrapes a list of links from the IMDB website for a list of years that you specify and 
    creates a list of movie links.
    
    Attributes:
    ----------
    service : class
        Manages the starting and stopping of the ChromeDriver.
    options : class
        Used to create an instance of the chrome driver.
    driver : object
        Gets the url.
    movie_link_list : list
        Creates a list of web elements corresponding to each movie from the IMDB website.
    category_heading_list : list
        Creates a list of all the column headings from the table of information for each movie link.
    '''        
    def __init__(self, url: str="https://www.boxofficemojo.com/", driverpath: str='/Applications/chromedriver'):     
        '''
        The function initialises the class and takes in a url and a driverpath. 
        The options and service object creates a driver object that is used to get the url.
        The function sleeps for 3 seconds to allow the webpage to fully load.
        
        Parameters
        ----------
        url : str, optional
            The url of the website you want to scrape.
        driverpath : str, optional
            This is the path to the chromedriver executable.
        
        '''
        self.service = Service(driverpath)
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options, service=self.service) 
        self.driver.get(url)
        self.movie_link_list = []
        self.category_heading_list = []
        self.category_value_list = []
        time.sleep(3)

    def click_monthly_button(self):
        '''
        The function clicks the monthly button on the web home page.

        '''
        domestic_container = self.driver.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div') 
        monthly_button = domestic_container.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div/a[4]') 
        monthly_button.click()
        time.sleep(3)

    def select_year_from_scroll_down_menu(self):
        '''
        The function selects the year from the drop down menu.
        
        '''
        drop_down_list = self.driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
        select = Select(drop_down_list)
        select.select_by_visible_text('By year')
        time.sleep(3)

    def create_list_of_movie_links(self, year_list):    
        '''
        This function takes a list of years as an argument, and then loops through each 
        year to get a list of web links corresponding to each movie.
        
        Parameters
        ----------
        year_list
            a list of years that you want to scrape
        
        Returns
        -------
            A list of movie links.
        
        '''
        self.select_year_from_scroll_down_menu()
        for year in (year_list): 
            drop_down_by_year = self.driver.find_element(by=By.XPATH, value='//select[@id="by-year-navSelector"]')
            select = Select(drop_down_by_year)
            select.select_by_visible_text(year)
            time.sleep(3)

            movie_table = self.driver.find_element(by=By.XPATH, value='//*[@id="table"]/div/table[2]/tbody')
            movie_list = movie_table.find_elements(by=By.XPATH, value='//*[@class="a-text-left mojo-field-type-release mojo-cell-wide"]')
            for movie in movie_list:
                a_tag = movie.find_element(by=By.TAG_NAME, value='a')
                link = a_tag.get_attribute('href')
                self.movie_link_list.append(link)
        return(self.movie_link_list)    


# This class is a child of the Web_link_scraper class. It takes a list of web links and scrapes the
# data from each link.
# It scrapes the movie links from the IMDB website, scrapes the movie name, image data, and text data
# from the movie links, creates a timestamp for the web scrape, creates a dictionary of the movie name
# and image and text data, creates a directory called 'raw_data' and then creates a subdirectory
# called 'box_office_mojo' inside of it, creates a file called 'data.json' inside of the
# 'box_office_mojo' directory and writes the movie dictionary to it, and finally, creates a directory
# called 'images' inside of the 'box_office_mojo' directory.
class Data_scraper(Web_link_scraper):


    def __init__(self):
        '''
        This class inherits the Web
        
        scrapes a list of links from the IMDB website for a list of years that you specify and 
        creates a list of movie links.
        
        '''
        super().__init__()
        self.text_data_dictionary = {}
        self.movie_dictionary = {}
        self.timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    def scrape_text_data_from_movie_links(self):
        '''This function scrapes the text data from the movie links
        
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
        return text_dictionary
        
    def scrape_movie_name_and_create_movie_dict(self):
        '''This function scrapes the movie name from the movie link, creates a timestamp for the web scrape,
        scrapes the image data, scrapes the text data from the movie links, updates the image and text
        dictionary with the image link, and updates the movie dictionary with the movie name and image and
        text dictionary.
        
        '''
        for link in (self.movie_link_list[0:3]):
            self.driver.get(link)
            time.sleep(2)
            div_tag = self.driver.find_element(by=By.XPATH, value='//div[@class="a-fixed-left-grid-col a-col-right"]')
            movie_name = div_tag.find_element(by=By.XPATH, value='h1[@class="a-size-extra-large"]').text
            self.create_timestamp_for_web_scrape()
            image_link = self.scrape_image_data()
            image_and_text_dictionary = self.scrape_text_data_from_movie_links()
            image_and_text_dictionary.update({'image_link':image_link})
            self.movie_dictionary.update({movie_name:image_and_text_dictionary})  
        self.create_directories_and_download_movie_dict()     

        for n, movie in enumerate(self.movie_dictionary.values(),1):
            timestr = self.timestamp
            self.download_image(movie['image_link'], f'raw_data/box_office_mojo/images/{timestr}_{n}.jpg')   
    
    def create_timestamp_for_web_scrape(self):      
        '''This function creates a timestamp for the web scrape.
        
        '''
        time_key = 'timestamp'
        self.category_heading_list.append(time_key)
        self.category_value_list.append(self.timestamp)

    def scrape_image_data(self):
        '''The function scrapes the image data from the IMDB website.
        
        Returns
        -------
            The image source is being returned.
        
        '''
        image_results = self.driver.find_element(By.XPATH, value = '//*[@class="a-section a-spacing-none mojo-posters"]')
        img_tag = image_results.find_element(by=By.TAG_NAME, value='img')
        src = img_tag.get_attribute('src')
        return src   

    def download_image(self, image_url, fp):
        '''Downloads an image from a URL and saves it to a file path
        
        Parameters
        ----------
        image_url
            The URL of the image you want to download.
        fp
            file path
        
        '''
        image_data = requests.get(image_url, fp).content
        with open(fp, 'wb') as handler:
            handler.write(image_data)

    def create_directories_and_download_movie_dict(self):
        '''It creates a directory called 'raw_data' and then creates a subdirectory called
        'box_office_mojo' inside of it. Then it creates a file called 'data.json' inside of the
        'box_office_mojo' directory and writes the movie dictionary to it. Finally, it creates a
        directory called 'images' inside of the 'box_office_mojo' directory
        
        '''
        os.mkdir('raw_data')
        path = os.path.join('raw_data', 'box_office_mojo')
        os.mkdir(path)
        with open(os.path.join(path, 'data.json'), 'w') as f:
            json.dump(self.movie_dictionary, f)
        image_path = 'raw_data/box_office_mojo/images'
        os.mkdir(image_path)
    
    

if __name__ == '__main__':
    year_list = ['2017', '2018']
    imdb = Data_scraper()
    imdb.click_monthly_button()
    imdb.create_list_of_movie_links(year_list)
    imdb.scrape_movie_name_and_create_movie_dict()
