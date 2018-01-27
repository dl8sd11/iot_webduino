from bs4 import BeautifulSoup
import requests
from random import *
def getRecipe():
    res = requests.get('http://www.carrefour.com.tw/recipes')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    menu = soup.find_all("ul","sidebar_menu_breadcrumb")[0]
    tmp = menu.find_all("li","last-child");
    tmp = tmp[randint(0,len(tmp)-1)]
    res2 = requests.get('http://www.carrefour.com.tw'+tmp.find("a")['href'])
    res2.endcoding = 'utf-8'
    recipe = BeautifulSoup(res2.text,'html.parser')
    recipe = recipe.find_all('div','tip-recipe-item')
    return recipe
