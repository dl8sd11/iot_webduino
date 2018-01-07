# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:49:03 2017

@author: TommyDong
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image, ImageTk
import time

import requests

def showClothesFromUrl(image_url):
    img_path = '../tmp/test.jpg'
    img_data = requests.get(image_url).content
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    
    root = Tk()
    
    image = Image.open(img_path)
    width, height = image.size


    image = image.resize((int(width*710/height), 710), Image.ANTIALIAS)

    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()
    root.mainloop()
    return
def getClothesUrl(gender):
    
    chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
    web = webdriver.Chrome(chrome_path)
    
    clothes_url = 'http://www.dressbyweather.com/'
    web.get(clothes_url)
    web.set_window_position(0,0) #瀏覽器位置
    
    time.sleep(2)
    
    if gender == 'm':
        web.find_element_by_class_name('gender-input').click()
        web.find_element_by_name()
   
    pageSource = web.page_source
    soup = BeautifulSoup(pageSource,'lxml')
    result = soup.select('.main-image')
    attr = result[0]
    
    web.close()
    return attr.attrs['src']
file_path = '../command/getclothes.txt'
while True:
    object = open(file_path,'r')
    if object.read() == 'true':
           print('true')
           object.close()
           open(file_path,'w').write('false')
           showClothesFromUrl(getClothesUrl('fuck'))
    object.close()
    
