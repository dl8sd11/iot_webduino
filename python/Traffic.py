from selenium import webdriver
import time
import pyscreenshot as ImageGrab

def updateTraffic():
    web = webdriver.Chrome()
    #@24.8070443,120.9629226,13.74z
    map_url = 'https://www.google.com.tw/maps/@24.7923657,121.0101596,13.35z/data=!5m1!1e1?hl=zh-TW'
    web.get(map_url)
    web.set_window_size(1920,1080)
    web.set_window_position(0,0)
    time.sleep(0.5)
    pic= ImageGrab.grab().crop((520,154,1536,864))
    pic.save('../pic/traffic.jpg')
    web.close()
    return
