FROM python:3.8-slim-buster

# Install google chrome.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN `apt-get -y update`
RUN `apt-get install -y google-chrome-stable`

# Install chromedriver.
RUN apt-get install -yqq unzip 
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Copy application in a Docker image
COPY . . 

# Install requirements
RUN pip install -r requirements.txt

# Run application
CMD ["python", "scraper/celebrity_scraper.py"]