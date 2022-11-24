# Data_Collection_Project 
An implementation of an industry grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control the browser, extract information from a website, and store it on the cloud in a data warehouses and data lake. The system conforms to industry best practices such as being containerised in Docker and running automated tests.

## Milestone 1: Set up the environment
- Source code built using Visual Studio Code.
- GitHub respository created for version control and to track lineage of code over time.
- Virtual environment created and third-party package called 'Selenium' installed. Creating a virtual environment ensures that the project will always run with the version of any third-party packages that were installed and tested with my code. 
- Selenium is a tool for programmatically controlling a browser and can drive a web browser once a webdriver is installed.
- Installed Chromedriver: a webdriver used for Google Chrome Version 105.0.5195.125.

## Milestone 2 & 3: Selecting website and build prototype finding links
The focus of this milestone was to find links of the web pages on the https://www.boxofficemojo.com/ website that contain data to be scraped.

Key developments included:
- Building a class called Web_Scraper that includes all the methods used for scraping box_office_mojo. 
- Creating a driverpath to store the latest chromedriver locally.
- Webdriving by importing'Services' and 'Option' classes from the selenium.webdriver.common. module and using these to create a   driver object to manipulate the url.
- Using XPath to navigate through elements and attributes. The dropdown menus of this website required using the 'Select' class of Selenium. The snippet of code below demonstrates how to use the 'select_by_visible_text' method to handle such drop downs:

```ruby
drop_down_list = self.driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
select = Select(drop_down_list)
select.select_by_visible_text('By year')
time.sleep(3)
```   
- The code is built to that the user chooses which years they want to scrape and pass these as an instance of the class in the form of a list.
- Seperate method created that takes a list of years as as an arguement and then iterates through each year to return a list of web links corresponding to each movie. 

Ideally, methods should avoid nested loops however in this isolated situation it was unavoidable as a result of the HTML script for this website.

## Milestone 4: Retrieve data from details page.
- Building on the previous milestone, using XPath expressions to select relevant data and images for each movie listed in the list of web links.
- Used print statements to ensure that data being collected was in the desired format and not web elements.
- The datetime module was used to create a timestamp for the webscrape of each movie. Data for each movie was stored in a dictionary object and then updated to a main dictionary (movie.dictionary). Each movie dictionary is identifiable by means of a unique ID, in this case the movie title.
- Imported the os module to programatically create a folder to store all data scraped; written text stored in JSON format and images downloaded in jpg format.
- Images were downloaded by importing the 'requests' library as good practise in case the website changes the URL at which these images are stored. I learnt how to utilise the enumerate method to create filenames for each image.


## Milestone 5: Documentation and testing.
- Refactored code to incorporate class inheritance and privatised methods that were called within the same class. Added additional return statements for the purpose of testing. 
- Imported the 'unittest' module to form the basis of my test suite. It was essential to build an integration test to ensure that both classes run concurrently. The following snippet of code shows one of the integration tests I incorporated: 
```ruby
def test_first_link_of_list(self):
        data_scraper = Data_scraper()
        data_scraper._click_monthly_button()
        link_list = data_scraper._create_list_of_movie_links(self.year_list)
        self.assertEqual(link_list[0], 'https://www.boxofficemojo.com/release/rl2708702721/?ref_=bo_my_table_1')
```   
(Logic: The parent class creates a list object with index [0] being the first box office movie in 2017. If the code is running correctly then the child class will inherit the list object and return the same link).
- Restructured project directories and files for the purpose of testing, designing, developing and mantaining the program.


## Milestone 6 & 7: Setting up a CI/CD pipeline for your Docker image.
- Refactored the __init__ method of the parent class to run the scrapers in headless mode, this is required for the program to run within a Docker container and can be achieved using the 'Option' class of Selenium. I found this youtube tutorial helpful: https://www.youtube.com/watch?v=LN1a0JoKlX8. All credit goes to Rajsuthan Official. Note that some of the code has deprecated so I include mine here for anyone that may find it useful:

```ruby
def __init__(self, url: str="https://www.boxofficemojo.com/", driverpath: str='/Applications/chromedriver'):   
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

        self.service = Service(driverpath)
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.headless = True
        self.options.headless = True
        self.options.headless = True
        self.options.headless = True
        self.options.headless = True
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=self.options, service=self.service) 
        self.driver.get(url)
``` 
- Created a dockerhub account and integrated Dockerfile and docker-compose.yaml files into my root directory to build an image that runs the program. 
- Set up a workflow to create a CI/CD pipeline using GitHub Actions. The workflow builds a Docker image and pushes it to my Dockerhub account when triggered on a push to the main branch of this github repository. 


For further details about my code please refer to file: 'Scraper.py' located in this respository. 








