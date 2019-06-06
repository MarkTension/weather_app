import urllib
import requests
import random
import selenium
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs


#### make array with website xpaths
"""
1. make array with website htmls and xpaths
- weeronline https://www.weeronline.nl/Europa/Nederland/Amsterdam/4058223
- google https://www.google.com/search?q=weer+amsterdam&oq=weer+amsterdam&aqs=chrome..69i57j69i60l2j0l3.2016j0j4&sourceid=chrome&ie=UTF-8
- weerplaza https://www.weerplaza.nl/nederland/amsterdam/5575/
- weer.nl http://www.weer.nl/verwachting/nederland/amsterdam/1812872/
------
2. save in DB 
 - SQLite:
 plek       | tijd  |  site   |   temperatuur
 ---------------------------------------------
 amsterdam  |       |         |
            |       |         |
            |
            |



"""

#



def main():

    driver = webdriver.Chrome('./chromedriver')

    driver.get('https://knmi.nl/nederland-nu/weer/verwachtingen')
    # driver.get('//*[@id="weather"]/div[1]/div/div[2]/div[2]/p[3]/a')


    # get access to full txt
    xpathname = '//*[@id="weather"]/div[1]/div/div[2]/div[2]/p[3]/a'
    xpath_element = driver.find_element(By.XPATH, xpathname)
    xpath_element.click()
    # xpath =
    # class_name =

    # get txt in string
    xpath_txt = '//*[@id="weather"]/div[1]/div/div[2]/div[2]'
    xpath_txt_element = driver.find_element(By.XPATH, xpath_txt)
    weather_string= xpath_txt_element.get_attribute('outerHTML')

    # parse with beautifulsoup
    weather_soup = bs(weather_string, 'html.parser')

    outer_div = weather_soup.find(class_ = "weather__text media__body")
    outer_div.text



    # think about efficient loading strategy (capabilities) (different mode)
    #



    print('hello')






if __name__ == '__main__':

  main()
