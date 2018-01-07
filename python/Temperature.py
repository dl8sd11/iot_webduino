from bs4 import BeautifulSoup
import requests

def getTemperature():
    res = requests.get('http://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    temp = soup.select('.FcstBoxTable01')[0].find('tbody').find_all('tr')[0].find_all('td')[0].get_text()
    return temp
if __name__ == "__main__":
    print (getTemperature())
