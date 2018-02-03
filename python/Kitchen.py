from random import *
from bs4 import BeautifulSoup
import requests

def getRecipe():
    res = requests.get('http://www.carrefour.com.tw/recipes')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    menu = soup.find_all("ul","sidebar_menu_breadcrumb")[0]
    tmp = menu.find_all("li","last-child");
    tmp = tmp[randint(0,len(tmp)-1)]
    #print(tmp)
    res2 = 'http://www.carrefour.com.tw'+tmp.find("a")['href']
    # res2.endcoding = 'utf-8'
    # recipe = BeautifulSoup(res2.text,'html.parser')
    # recipe = recipe.find_all('div','tip-recipe-item')
    # ret = []
    # for dish in recipe:
    #     ret.append(str(dish))
    return res2
if __name__ == "__main__":
    print(getRecipe())
