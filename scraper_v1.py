import urllib
import requests
import random
import selenium
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs





def main():

    driver = webdriver.Chrome('./chromedriver')

    driver.get('https://knmi.nl/nederland-nu/weer/verwachtingen')
    driver.get('//*[@id="weather"]/div[1]/div/div[2]/div[2]/p[3]/a')

    # get access to full txt
    xpathname = '//*[@id="weather"]/div[1]/div/div[2]/div[2]/p[3]/a'
    xpath_element = driver.find_element(By.XPATH, xpathname)
    xpath_element.click()
    xpath =
    class_name =

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
