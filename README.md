# Data_Collection_Project 
An implementation of an industry grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control your browser, extract information from a website, and store it on the cloud in a data warehouses and data lake. The system conforms to industry best practices such as being containerised in Docker and running automated tests.

## Milestone 1: Set up the environment
- Source code built using Visual Studio Code.
- GitHub respository created for version control and to track lineage of code over time.
- Virtual environment created and third-party package called 'Selenium' installed. Creating a virtual environment ensures that the project will always run with the version of any third-party packages that were installed and tested with my code. 
- Selenium is a tool for programmatically controlling a browser and can drive a web browser once a webdriver is installed.
- Installed Chromedriver: a webdriver used for Google Chrome Version 105.0.5195.125.

## Milestone 2: Selecting website

- Website selected: https://www.boxofficemojo.com/

Being a movie lover my curiosity led me to investigate the impact of the covid-19 pandemic on the movie box office revenue from years 2017 to 2022. For this project, I chose to explore the international market. While scoping the imdb website I navigated to its affiliate website: box office mojo an American website that tracks box-office revenue and I chose this website to scrape because the data necessary for this project is presented in a systematic fashion.

## Milestone 3: Prototype finding links
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
- Imported the 'unittest' module to form the basis of my test suite. It was essential to build an integration test to ensure that both classes are concurrent.
- Restructured project directories and files for the purpose of testing, designing, developing and mantaining the program. 






## Milestone 7: Retrieve data from details page.







For further details about my code please refer to file: 'Scraper.py' located in this respository. 








