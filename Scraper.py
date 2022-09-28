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



        