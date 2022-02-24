from selenium import webdriver
#pip install selenium
import time


#browser = webdriver.Chrome("/Users/hberk/OneDrive/Masaüstü/chromedriver")
browser = webdriver.Edge("/Users/hberk/OneDrive/Masaüstü/msedgedriver")

#yürütme aracı kimliği öğrenme
#my user agent yazılır tarayıcıya
#Mozilla/5.0 (Windows NT 10.0; Win64; x64)
#AppleWebKit/537.36 (KHTML, like Gecko) 
#Chrome/97.0.4692.71 Safari/537.36
#

browser.get("https://www.forbes.com/the-worlds-most-valuable-brands/#177dbf59119c")

#print(browser.page_source)
#tüm veri alınması

#print(browser.title())
#sayfanın title verisi

browser.fullscreen_window()
time.sleep(2)
#pencere full screen

browser.set_window_size(600,400)
time.sleep(3)
#browser boyutu küçültme


browser.save_screenshot("/Users/hberk/OneDrive/Masaüstü/image.png")
#screen shot alındı

#browser.close()
browser.back()
time.sleep(3)
browser.quit()
