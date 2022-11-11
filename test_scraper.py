import unittest
from Scraper import Web_link_scraper
from Scraper import Data_scraper

class WebLinkScraperTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.category_heading_list = []
    #     self.category_value_list = []
    #     self.link_list = Web_link_scraper()

    def test_create_list_of_movie_links(self): #works
        link_list = Web_link_scraper()
        link_list.click_monthly_button()
        link_list.create_list_of_movie_links(year_list=['2017', '2018'])
        self.assertIsNotNone(link_list)
        # Create another test method to check whether the first and last link is equal to what you expect.

        
    def test_scrape_text_data_from_movie_links(self):
        dict = Data_scraper()
        dict.create_text_dictionary()
        self.assertIsNotNone(dict)

   

    

    



    

        

