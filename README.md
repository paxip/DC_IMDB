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
- Importing'Services' and 'Option' classes from the selenium.webdriver.common. module and using these to create a   driver object to manipulate the url.
- Using the find_element method to locate web elements from the url and navigate through the website. However, the 'Select' class in selenium was required to navigate the dropdown menus. The snippet of code below demonstrates how to use the 'select_by_visible_text' method:

```ruby
drop_down_list = self.driver.find_element(by=By.XPATH, value='//select[@id="view-navSelector"]') 
select = Select(drop_down_list)
select.select_by_visible_text('By year')
time.sleep(3)
```   
- The class is designed for the user to choose which years they want to scrape movie data for as an instance of the class. 
- Seperate method created that takes a list of years as as an arguement and then iterates through each year to return a list of web links corresponding to each box office. 



## Milestone 4: Retrieve data from details page.




## Milestone 7: Retrieve data from details page.







For further details about my code please refer to file: 'Scraper.py' located in this respository. 








