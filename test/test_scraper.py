
from project.creates_list_of_movie_web_links import Web_link_scraper
from project.scrapes_data import Data_scraper
from typing import Any
import json
import unittest

class WebLinkScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.year_list = ['2017', '2018']
               
    def test_create_list_of_movie_links(self):
        web_scraper = Web_link_scraper()
        web_scraper._click_monthly_button()
        link_list = web_scraper._create_list_of_movie_links(self.year_list)
        self.assertIsNotNone(link_list)
    
    def test_length_of_list(self): 
        web_scraper = Web_link_scraper()
        web_scraper._click_monthly_button()
        link_list = web_scraper._create_list_of_movie_links(self.year_list)
        self.assertEqual(len(link_list), 24)

    def test_first_link_of_list(self):
        data_scraper = Data_scraper()
        data_scraper._click_monthly_button()
        link_list = data_scraper._create_list_of_movie_links(self.year_list)
        self.assertEqual(link_list[0], 'https://www.boxofficemojo.com/release/rl2708702721/?ref_=bo_my_table_1')

    def test_last_link_of_list(self):
        data_scraper = Data_scraper()
        data_scraper._click_monthly_button()
        link_list = data_scraper._create_list_of_movie_links(self.year_list)
        self.assertEqual(link_list[23], 'https://www.boxofficemojo.com/release/rl3095234049/?ref_=bo_my_table_12')

    def test_movie_dict(self):
        data_scraper = Data_scraper()
        data_scraper._click_monthly_button()
        link_list = data_scraper._create_list_of_movie_links(self.year_list)
        movie_dict = data_scraper.create_movie_dictionary()
        self.assertIsNotNone(movie_dict)

    def test_json_dump(self):
        data_scraper = Data_scraper()
        data_scraper._click_monthly_button()
        link_list = data_scraper._create_list_of_movie_links(self.year_list)
        movie_dict = data_scraper.create_movie_dictionary()
        data_scraper.create_directories()
        json_file = data_scraper.save_to_json(str, Any, 4)
        self.assertTrue(json_file)
      
        
unittest.main(argv=[''], verbosity=3, exit=False)




    
   

    

    



    

        

