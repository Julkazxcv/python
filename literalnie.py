from queue import Empty
from re import search
import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from selenium.webdriver.common.by import By


chromedriver_path= "C:/Python39/chromedriver.exe"
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
url = "https://literalnie.fun/"
driver.get(url)
time.sleep(3) #if you want to wait 3 seconds for the page to load
page_source = driver.page_source
soup = bs4.BeautifulSoup(page_source, 'html.parser')

element = soup.find("div", class_="letter")
Ł = driver.find_element(by=By.LINK_TEXT, value='Ł')
print(element)
for i in range(5):
    element = element.find_next_sibling()
    print(element)
    Ł.click()
    

