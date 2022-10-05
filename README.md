# Data_Collection_Project 
An implementation of an industry grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control your browser, extract information from a website, and store it on the cloud in a data warehouses and data lake. The system conforms to industry best practices such as being containerised in Docker and running automated tests.

## Milestone 1: Set up the environment
- Source code built using Visual Studio Code.
- GitHub respository created for version control and to track lineage of code over time.
- Virtual environment created and third-party package called 'Selenium' installed. Creating a virtual environment ensures that the project will always run with the version of any third-party packages that were installed and tested with my code. 
- Selinium is a tool for programmatically controlling a browser and can drive a web browser once a webdriver is installed.
- Installed Chromedriver: a webdriver used for Google Chrome Version 105.0.5195.125.

## Milestone 2: Selecting website

- website selected: https://www.boxofficemojo.com/

Being a movie lover my curiosity led me to investigate the impact of the covid-19 pandemic on the movie box office revenue from years 2017 to 2022. For this project, I chose to explore the domestic market only (UK). While scoping the imdb website I navigated to its affiliate website: box office mojo an American website that tracks box-office revenue and I chose this website to scrape because the data necessary for this project is presented in a systematic fashion.

## Milestone 3: Prototype finding links

The focus of this milestone was to find links of the web pages on the https://www.boxofficemojo.com/ website that contain data to be collected for analysis. 
Key developments included:
- Building code using Selenium/chromedriver to get the webpage, navigate to webpage that contains a table organising box office hits for each month of every year from the years 1931 to 2022.
- Collecting the web links to every monthly box office hit from the years 2017 to 2022 and storing these links in a library. 
- Refactoring the code once it was optimised in a class called 'Scraper' and initialising the class using conditional statement if __name == "__main__" so that the code will only run directly.

For further details about my code please refer to file: 'Scraper.py' located in this respository. 








