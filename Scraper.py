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
        
        drop_down_menu = driver.find_element(By.XPATH, value='//')
        //*[@id="a-popover-1"]/div

        <span class="a-button-text a-declarative" data-csa-c-func-deps="aui-da-a-dropdown-button" data-csa-c-type="widget" data-csa-interaction-events="click" data-action="a-dropdown-button" aria-hidden="true" data-csa-c-id="632vcy-7gkvzp-terowd-aznnfc" id="a-autoid-0-announce"><span class="a-dropdown-prompt">By Month</span></span>

        print(drop_down_menu)

        
Scraper.load_webpage()



        





   




