
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

    def _click_monthly_button(self, xpath_button='//*[@id="a-page"]/div[2]/div[4]/div/a[4]' ):
        '''
        The function clicks the monthly button on the web home page.

        '''
        monthly_button = self.driver.find_element(by=By.XPATH, value=xpath_button) 
        monthly_button.click()
        time.sleep(3)

    def _select_year_from_scroll_down_menu(self):
        '''
        The function selects the year from the drop down menu.
        
        '''
        drop_down_list = self.driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
        select = Select(drop_down_list)
        select.select_by_visible_text('By year')
        time.sleep(3)

    def _create_list_of_movie_links(self, year_list):
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
        self._select_year_from_scroll_down_menu()
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
        # print(self.movie_link_list)
        # print(len(self.movie_link_list))
        return self.movie_link_list  


if __name__ == '__main__':
    year_list = ['2017', '2018']