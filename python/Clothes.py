# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:06:25 2017

@author: TommyDong
嘗試從中央氣象局網站取得近時的降雨機率
"""

from bs4 import BeautifulSoup
import requests
import time
def collectClothes():
    res = requests.get('http://www.cwb.gov.tw/V7/forecast/town368/3Hr/6600400.htm')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    rain = soup.find('div').find('table').find_all('tr')[8].find_all('td')  #[1].get_text()[:-1]
    first = 1
    avg = 0
    rainSum = 0
    count = 0
    for x in rain:
            if first == 0:
                text = x.get_text()[:-1]
                print (text)
                rainSum += int(text)
                count +=1
                if count == 1:
                    firstRain = int(text)
            first = 0

    avg= rainSum /count
    collect =0
    print("最近平均降雨機率",avg)
    print("目前降雨機率",firstRain)
    if firstRain > avg and firstRain >50:
        return 1;
    else:
        return 0;

if __name__=="__main__":
    print(collectClothes());





#取得未來三日降雨機率
#print (rain)
#/html/body/div[@class='Forecast-box']/table/tbody/tr[9]/td[2]
