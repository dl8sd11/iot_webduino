from bs4 import BeautifulSoup
import requests

def getOutdoorInfo():
    res = requests.get('https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    pm = soup.find("table",{"id": "ctl08_gv"}).find_all('tr')[6].find_all("td")[1].get_text()
    pm = pm.replace("\n", "");

    # output="pm2.5: "+pm.get_text()+"μg／m3"

    res2 = requests.get('http://www.cwb.gov.tw/m/f/town368/7day/1001801.htm')
    res2.encoding = 'utf-8'
    soup = BeautifulSoup(res2.text, 'html.parser')
    rain = soup.find("tbody").find_all("tr")[0].find_all("td")[5].get_text()[:-1]

    return {'rain':rain,'pm':pm}
if __name__ == "__main__":
    print(getOutdoorInfo())
