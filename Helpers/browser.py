# Import time module to implement
from selenium import time

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

dirx = "dir"
path = "path"
browser = webdriver.Firefox()

# Define the FireFox driver this time so we use Firefox to run the test
driver = webdriver.Firefox()

driver.manage().timeouts()

def goToURL(driver):
    # Go to google.com
    driver.get('http://www.google.com')


self.driver = webdriver.Firefox()
