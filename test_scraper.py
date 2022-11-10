import unittest
from Scraper import Web_link_scraper

class Web_link_scraperTestCase(unittest.TestCase):
    #def setUp(self):
        

    def test_year_list(self):
        web_scraper = Web_link_scraper()
        year_list = ['2017', '2018']
        web_scraper.create_list_of_movie_links(year_list)
        self.assertListEqual(year_list, ['2017', '2018'] )

