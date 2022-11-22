from creates_list_of_movie_web_links import Web_link_scraper
from scrapes_data import Data_scraper
from typing import Any

if __name__ == '__main__':
    year_list = ['2017', '2018']
    imdb = Data_scraper()
    imdb._click_monthly_button()
    imdb._create_list_of_movie_links(year_list)
    imdb.create_movie_dictionary()
    imdb.create_directories()
    imdb.create_image_directory()
    imdb.save_to_json(str, Any, 4)