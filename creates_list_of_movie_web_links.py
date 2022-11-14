
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from typing import Any
import time
import datetime
import json
import os
import requests


class Web_link_scraper:    
    def __init__(self, url: str="https://www.boxofficemojo.com/", driverpath: str='/Applications/chromedriver'):     
        self.service = Service(driverpath)
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options, service=self.service) 
        self.driver.get(url)
        self.movie_link_list = []
        self.category_heading_list = []
        self.category_value_list = []
        time.sleep(3)

    def click_monthly_button(self):
        domestic_container = self.driver.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div') 
        monthly_button = domestic_container.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div/a[4]') 
        monthly_button.click()
        time.sleep(3)

    def select_year_from_scroll_down_menu(self):
        drop_down_list = self.driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
        select = Select(drop_down_list)
        select.select_by_visible_text('By year')
        time.sleep(3)

    def create_list_of_movie_links(self, year_list):    
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
        # print(self.movie_link_list)
        # print(len(self.movie_link_list))
        return self.movie_link_list  


if __name__ == '__main__':
    year_list = ['2017', '2018']