from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests

def getRecipe():
    web = webdriver.Chrome()

    recipe_url = 'https://jamesoff.net/fun/random-recipe-generator/'
    web.get(recipe_url)
    time.sleep(1.5)
    pageSource = web.page_source
    web.close()
    soup = BeautifulSoup(pageSource,'lxml')

    rp = soup.find("div",{"id":"recipe"})
    Line = []
    Line.append(rp.find("h2").get_text())
    Line.append(rp.find('div').get_text())
    Line.append("You will need:")
    ul = rp.find("ul")
    for li in ul.find_all("li"):
        Line.append(li.get_text())
    Line.append('Instructions:')
    ol = rp.find("ol")
    for li in ol.find_all("li"):
        Line.append(li.get_text())
    return Line
