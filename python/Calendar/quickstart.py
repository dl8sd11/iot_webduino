from __future__ import print_function
import httplib2
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
import time
import requests

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    show  = 2;

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if  not credentials or  credentials.invalid or show==1:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getCalendar():
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    

    now = datetime.datetime.now()
    night = now.replace(hour=23, minute=59)

    #I'm at UTC+8
    utcNow = now-datetime.timedelta(hours=15)
    utcnight = night - datetime.timedelta(hours=8)

    isoNow = utcNow.isoformat() + 'Z' # 'Z' indicates UTC time
    isoNight=utcnight.isoformat() + 'Z'

    eventsResult = service.events().list(
        calendarId='primary', timeMin=isoNow,timeMax=isoNight, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    print('The Calendar is ready!')
    return events
      

def showForm(events,image_url):
    img_path = '../../tmp/test.jpg'
    #img_data = requests.get(image_url).content
    #with open(img_path, 'wb') as handler:
    #    handler.write(img_data)
    
    root = Tk()
    root.title = ("wardrobe")
    root.configure(background='white')

    image = Image.open(img_path)
    width, height = image.size


    res = requests.get('http://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    temp = soup.select('.FcstBoxTable01')[0].find('tbody').find_all('tr')[0].find_all('td')[0].get_text()
    
    tempText = "氣溫:"+ temp+'°C\n'+'建議你可以這樣穿'
        
    tempLab = Label(root,text=tempText,font=("monospace", 24))
    tempLab.configure(background='white')
    tempLab.grid(column = 0 ,row = 0,rowspan = 3,padx = 100 )

    image = image.resize((int(width*400/height), 400), Image.ANTIALIAS)

    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.configure(background='white')
    label.grid(column = 0 ,row = 3,rowspan = 8,sticky=N,pady=20)
    a=0
    label2 = Label(root,text="今天行程:",font=("monospace", 24));
    label2.configure(background='white')
    label2.grid(column = 1 ,row = a,padx=50,pady=20)
    a=a+1
    if not events:
            print('No upcoming events found.')
    for event in events:
            
           start = event['start'].get('dateTime', event['start'].get('date'))
           label2 = Label(root,text=str(a)+'. '+event['summary'],font=("monospace", 24))
           label2.configure(background='white')
           label2.grid(column = 1 ,row = a,sticky='w')
           a+=1
           print(event['summary']) 
    
    
    root.mainloop()
    return
def getClothesUrl(gender):
    
    chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" 
    web = webdriver.Chrome(chrome_path)
    
    clothes_url = 'http://www.dressbyweather.com/'
    web.get(clothes_url)
    
    time.sleep(5)
    
    if gender == 'm':
        web.find_element_by_class_name('gender-input').click()
        web.find_element_by_name()
   
    pageSource = web.page_source
    soup = BeautifulSoup(pageSource,'lxml')
    result = soup.select('.main-image')
    attr = result[0]
    
    web.close()
    return attr.attrs['src']


events = getCalendar()
clothes_Url = getClothesUrl('t');
                 
file_path = '../../command/getclothes.txt'
while True:
    try:
        object = open(file_path,'r')
        if object.read() == 'true':
               print('true')
               object.close()
               open(file_path,'w').write('false')
               showForm(events,clothes_Url)  
        object.close()
    except:
        print("error")

