from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

        drop_down_menu = driver.find_element(By.CLASS_NAME, 'a-dropdown-container')
        inner_drop_down_button = drop_down_menu.find_element(By.CLASS_NAME, 'a-button-inner')
        inner_drop_down_button.click()

        
        
        #a_tag = driver.find_element(by=By.TAG_NAME, value='a')
        #by_year_button = drop_down_menu.find_element(By.CLASS_NAME, "a-dropdown-link")
        #by_year_button.click()


        

        

        
Scraper.load_webpage()



        





   




