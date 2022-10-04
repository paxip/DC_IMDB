
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
import time


class Scraper:

    def __init__(self, url: str = "https://www.boxofficemojo.com/", driverpath: str = '/Users/apple/Documents/GitHub/DC_Zoopla/chromedriver 5' ):     
        self.service = Service(driverpath)
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options, service=self.service) 
        self.driver.get(url)

        time.sleep(3)

    def navigate_to_movie_table(self):
        domestic_container = self.driver.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div') 
        monthly_button = domestic_container.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div/a[4]') 
        monthly_button.click()
        time.sleep(3)

        return self.driver

    def get_movie_links(self):
        for year in ('2017','2018','2019','2020','2021','2022'):
            drop_down_by_year = self.driver.find_element(by=By.XPATH, value='//select[@id="by-year-navSelector"]')
            select = Select(drop_down_by_year)
            select.select_by_visible_text(year)
            time.sleep(5)

            movie_table = self.driver.find_element(by=By.XPATH, value='//*[@id="table"]/div/table[2]/tbody')
            movie_list = movie_table.find_elements(by=By.XPATH, value='//*[@class="a-text-left mojo-field-type-release mojo-cell-wide"]')
            link_list = []

            for movie in movie_list:
                a_tag = movie.find_element(by=By.TAG_NAME, value='a')
                link = a_tag.get_attribute('href')
                link_list.append(link)

            print(f'There are {len(link_list)} movies on this page')
            print(link_list)
            return link_list


if __name__ == '__main__':
    imdb = Scraper()
    imdb.navigate_to_movie_table()
    imdb.get_movie_links()



    


        

    

        


    


        




        





   




