from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
import time


class Scraper:
    def load_webpage():
        URL = "https://www.boxofficemojo.com/"
        driverpath = '/Users/apple/Documents/GitHub/DC_Zoopla/chromedriver 5'
        service = Service(driverpath)
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options, service=service) 
        driver.get(URL)
        time.sleep(3)

        tab_container = driver.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div') 
        monthly_button = tab_container.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[4]/div/a[4]') 
        monthly_button.click()
        time.sleep(3)
        
        drop_down_by_year = driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
        select = Select(drop_down_by_year)

        select.select_by_visible_text('By year')
        time.sleep(3)

        drop_down_by_month = driver.find_element(by=By.XPATH, value='//select[@id="by-year-navSelector"]')
        select = Select(drop_down_by_month)

        select.select_by_visible_text('2017')
        time.sleep(5)


        
Scraper.load_webpage()



        





   




