import urllib
import requests
import random
import selenium
from selenium import webdriver
import sys
import os
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

    # [knmi, buienradar, accuweather, ...]
    forecasts = []

    # forecast knmi
    forecasts.append(knmi_forecast(driver))

    # forecast buienradar
    forecasts.append(buienradar_forecast(driver))

    # forecast accuweather
    forecasts.append(accuweather_forecast(driver))

    # forecast accuweather
    forecasts.append(bbc_forecast(driver))

    print(forecasts)

    # think about efficient loading strategy (capabilities) (different mode)
    #



def knmi_forecast(driver):
    print('knmi')

    driver.get('https://knmi.nl/nederland-nu/weer/verwachtingen')
    # driver.get('//*[@id="weather"]/div[1]/div/div[2]/div[2]/p[3]/a')

    # get txt in string
    xpath_txt = '//*[@id="weather"]/div[3]/div/div[2]/div/ul/li[1]/span[3]'
    xpath_txt_element = driver.find_element(By.XPATH, xpath_txt)
    weather_string = xpath_txt_element.get_attribute('outerHTML')

    # parse with beautifulsoup
    weather_soup = bs(weather_string, 'html.parser')
    forecast_max_tomorrow = int(weather_soup.text.split()[1][:-1])

    # outer_div = weather_soup.find(class_ = "weather-map__table-cell")

    print(forecast_max_tomorrow)

    return forecast_max_tomorrow


def buienradar_forecast(driver):
    print('buienradar')

    driver.get('https://www.buienradar.nl/weer/amsterdam/nl/2759794/14daagse')

    # click cookies
    xpathname = '/html/body/div/div[5]/form/input[5]'
    xpath_element = driver.find_element(By.XPATH, xpathname)
    xpath_element.click()

    # get txt in string
    xpath_txt = '//*[@id="forecastTable0"]/div/div/div[3]/div[3]'
    xpath_txt_element = driver.find_element(By.XPATH, xpath_txt)
    weather_string = xpath_txt_element.get_attribute('outerHTML')

    weather_soup = bs(weather_string, 'html.parser')
    minmax = str(weather_soup.findAll(text=True)).split('/')

    forecast_max_tomorrow = minmax[1].split('°')[0][1:]

    # parse with beautifulsoup
    # weather_soup = bs(weather_string, 'html.parser')
    # forecast_max_tomorrow = int(weather_soup.text.split()[1][:-1])

    print(forecast_max_tomorrow)

    return forecast_max_tomorrow

def accuweather_forecast(driver):
    print('accuweather')

    driver.get('https://www.accuweather.com/nl/nl/amsterdam/249758/weather-forecast/249758')

    # get txt in string
    xpath_txt = '//*[@id="feed-tabs"]/ul/li[4]/div/div[2]/div/span[1]'
    xpath_txt_element = driver.find_element(By.XPATH, xpath_txt)
    weather_string = xpath_txt_element.get_attribute('outerHTML')

    forecast_max_tomorrow = weather_string.split('°')[0].split('>')[1]

    print(forecast_max_tomorrow)

    return forecast_max_tomorrow

def bbc_forecast(driver):
    print('bbc')

    driver.get('https://www.bbc.com/weather/2759794')

    # get txt in string
    xpath_txt = '//*[@id="daylink-1"]/div[4]/div[1]/div/div[4]/div/div[1]/span[2]/span/span[1]'
    xpath_txt_element = driver.find_element(By.XPATH, xpath_txt)
    weather_string = xpath_txt_element.get_attribute('outerHTML')

    forecast_max_tomorrow = weather_string.split('°')[0].split('>')[1]

    print(forecast_max_tomorrow)

    return forecast_max_tomorrow

if __name__ == '__main__':

  main()
