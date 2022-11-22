from creates_list_of_movie_web_links import Web_link_scraper
from scrapes_data import Data_scraper


if __name__ == '__main__':
    year_list = ['2017', '2018']
    imdb = Data_scraper()
    imdb._click_monthly_button()
    imdb._create_list_of_movie_links(year_list)
    print('list of movie web links has been created.')
    imdb.create_movie_dictionary()
    imdb.create_directories()