from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from time import time
import os
import wget




driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('http://www.instagram.com')

# username = driver.find_element(by=By.NAME, value='name')
# username = driver.find_element(By.XPATH, '//input[@name="username"]')
# username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys("danielkamau231")

password.clear()
password.send_keys("k_dan_@*20")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), “Not Now”)]'))).click()
# alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), “Not Now”)]'))).click()
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()



###### HERE WE ARE LOGGED IN#########
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

###### SEARCH FOR CERTAIN HASHTAG##############


searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#######SEARCH FOR A KEYWORD##########
keyword = '#cat'
searchbox.send_keys(keyword)

time.sleep(5)
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

num_scrolls = 2
for i in range(0, num_scrolls):
    driver.execute_async_script("window.scrollTo(0, document.body.scrollHeight;)")
    time.sleep(5)

anchors = driver.find_elements_by_class_name('a')
anchors = [a.get_attribute('href') for a in anchors]
anchors = [a for a in anchors if str(a).startswith('https://www.instagram.com/p/')]

print('This is found ' + str(len(anchors)) + ' links to images')
anchors[:5]

images = []
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_element_by_class_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])
    images[:5]

#SAVING IMAGES TO COMPUTER
path = os.getcwd()
path = os.path.join(path, keyword[1:] + 's')

#here we are creating a directory

os.mkdir(path)

#HERE DOWNLOAD THE IMAGES
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + 'jpg') 
    wget.download(image, save_as)
    counter += 1

