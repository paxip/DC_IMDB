import unittest
from Scraper import Web_link_scraper
from Scraper import Data_scraper
from typing import Any
import json

class WebLinkScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.web_scraper = Web_link_scraper()
        self.data_scraper = Data_scraper()
        self.web_scraper.click_monthly_button()
        self.link_list = self.web_scraper.create_list_of_movie_links(year_list=['2017', '2018'])
       
    def test_create_list_of_movie_links(self):
        self.assertIsNotNone(self.link_list)
    
    def test_length_of_list(self): 
        self.assertEqual(len(self.link_list), 24)

    def test_first_link_of_list(self):
        self.assertEqual(self.link_list[0], 'https://www.boxofficemojo.com/release/rl2708702721/?ref_=bo_my_table_1')

    def test_last_link_of_list(self):
        self.assertEqual(self.link_list[23], 'https://www.boxofficemojo.com/release/rl3095234049/?ref_=bo_my_table_12')

    def test_movie_dict(self):
        movie_dict = self.data_scraper.create_movie_dictionary()
        self.assertIsNotNone(movie_dict)

    def test_json_dump(self):
        movie_dict = self.data_scraper.create_movie_dictionary()
        self.data_scraper.create_directories()
        json_file = self.data_scraper.save_to_json(str, Any, 4)
        self.assertTrue(json_file)

    def tearDown(self):
        del self.web_scraper 
        del self.data_scraper 
        
        
unittest.main(argv=[''], verbosity=3, exit=False)



        





    


    # def test_scrape_text_data_from_movie_links(self):
    #     dict = Data_scraper()
    #     dict.create_text_dictionary()
    #     self.assertIsNotNone(dict)

   

    

    



    

        

