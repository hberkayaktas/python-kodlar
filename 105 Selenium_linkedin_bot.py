import email
from re import search
from statistics import mode
from selenium import webdriver
#pip install selenium
import time
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome("/Users/hberk/OneDrive/Masaüstü/chromedriver")
browser = webdriver.Edge("/Users/hberk/OneDrive/Masaüstü/msedgedriver")

#yürütme aracı kimliği öğrenme
#my user agent yazılır tarayıcıya
#Mozilla/5.0 (Windows NT 10.0; Win64; x64)
#AppleWebKit/537.36 (KHTML, like Gecko) 
#Chrome/97.0.4692.71 Safari/537.36
#

browser.get("http://www.linkedin.com/login/tr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


"""
#pencere full screen
browser.set_window_size()
time.sleep(2)

browser.set_window_size(1000,1000)
time.sleep(3)


login = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[1]/form/div[3]/button")
login.click()
time.sleep(5)
"""

email = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[1]/form/div[1]/input")
password = browser.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[1]/form/div[2]/input")

email.send_keys("hberkayaktas@gmail.com")
password.send_keys("sifre")
login_button = browser.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
login_button.click()
time.sleep(5)

"""
browser.fullscreen_window()
time.sleep(2)
"""

popupclose = browser.find_element_by_xpath("/html/body/div[5]/aside/div[1]/header/div[3]/button[2]")
popupclose.click()
time.sleep(1)

""" arama yapma
search_bar = browser.find_element_by_xpath("/html/body/div[5]/header/div/div/div/div[1]/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
"""
############################# anasayfa yazisi #########################################
anasayfayazi = browser.find_elements_by_class_name("break-words")
print(anasayfayazi)
anaListesi = []

for anasayfayazitek in anasayfayazi:
        anaListesi.append(anasayfayazitek.text)
        print(anasayfayazitek)
####################################################################################

contact = browser.find_element_by_xpath("/html/body/div[5]/header/div/nav/ul/li[2]/a")
contact.click()
time.sleep(3)

for i in range(1,3): #3 kez scroll yap
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)



followers = browser.find_elements_by_class_name("discover-person-card__name t-16 t-black t-bold")
print(followers)
followerListesi = []

for follower in followers:
        followerListesi.append(follower.text)
        print(follower)

with open ("lifollower.txt",mode="w+",encoding="UTF-8") as file:
    for anayazdir in anaListesi:
        file.write(anayazdir + "/n")
        print(anayazdir)
    for followera in followerListesi:
        file.write(followera + "/n")
        print(followera)


time.sleep(3) 
browser.quit()


"""#print(browser.page_source)
#tüm veri alınması

#print(browser.title())
#sayfanın title verisi


browser.set_window_size(600,400)
time.sleep(3)
#browser boyutu küçültme


browser.save_screenshot("/Users/hberk/OneDrive/Masaüstü/image.png")
#screen shot alındı

#browser.close()
browser.back()
time.sleep(3)
browser.quit()
"""