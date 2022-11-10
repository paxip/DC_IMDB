import unittest
from Scraper import Web_link_scraper
from Scraper import Data_scraper

class WebLinkScraperTestCase(unittest.TestCase):
    # def setUp(self)

    def test_create_list_of_movie_links(self):
        link_list = Web_link_scraper()
        link_list.click_monthly_button()
        link_list.create_list_of_movie_links(year_list=['2017', '2018'])
        self.assertIsNotNone(link_list)
    
    def test_scrape_text_data_from_movie_links(self):
        text_dict = Data_scraper()
        text_dict.scrape_movie_name_and_create_movie_dict()
        self.assertIsNotNone(text_dict)

    

    



    

        

