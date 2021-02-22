from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


path = r"C:\Users\LENOVO\Devlopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get('https://tinder.com/')

tinder_login = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
tinder_login.click()
time.sleep(3)

try:
    fb_login = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
except NoSuchElementException:
    tinder_more_option = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/button')
    tinder_more_option.click()
    time.sleep(1)
    fb_login = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
else:
    fb_login.click()
time.sleep(3)

# print(driver.window_handles)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(3)
# Facebook login
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys("-----------Your Email--------------")
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("---------- Password ---------------")
password.send_keys(Keys.ENTER)

#Tinder dashbord
driver.switch_to.window(base_window)
time.sleep(5)
print(driver.title)
# share location
allow_share_location = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[1]')
allow_share_location.click()
time.sleep(1)
# disable notification
notifications_button = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
time.sleep(1)
#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print(n, ' swipe')
        like_button = driver.find_element_by_xpath(
            '//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()
    except NoSuchElementException:
        try:
            print('Super like')
            # Not now!
            super_like = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/button[2]')
            super_like.click()

        except NoSuchElementException:
            print('disable')
            # Add  to home Screen, NO!
            disable_home = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[2]/button[2]')
            disable_home.click()


    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)



driver.quit()

