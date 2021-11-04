import os
import time
from selenium import webdriver
#from credentials import username, password, description_file
from selenium.webdriver.common import action_chains
 
# FIREFOX
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
driver.set_window_size(1080,720)
 
 
url = 'https://mp.wshareit.com/login'
driver.get(url)
time.sleep(0.5)
 
 
field = driver.find_element_by_css_selector("input[type='text']")
field.send_keys('KomediLucu')
field = driver.find_element_by_css_selector("input[type='password']")
field.send_keys('Password2021!')
time.sleep(2)
button=driver.find_element_by_css_selector("button[type='button']")
button.click()
 
print("LOGGED IN")
 
time.sleep(1)
 
driver.find_element_by_css_selector("li[class='tab-item post']").click()
 
#driver.find_elements_by_xpath("//*[contains(text(), 'icon-post')]").click()
time.sleep(10)
 
driver.find_element_by_css_selector("div[class='drap-wrap']").click()
 
time.sleep(15)
 
driver.quit()
 
'''
os.system('autokey-run -s select_image')
 
time.sleep(10)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Expand')]")
if len(button) > 0:
    button[0].click()
 
time.sleep(20)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Next')]")
button[0].click()
 
time.sleep(10)
field = driver.find_elements_by_tag_name('textarea')[0]
field.click()
 
with open(description_file, 'r') as file:
    description = file.read()
 
field.send_keys(description)
 
time.sleep(15)
button = driver.find_elements_by_xpath("//*[contains(text(), 'Share')]")[1]
 
driver.execute_script("arguments[0].scrollIntoView();", button);
action = action_chains.ActionChains(driver)
action.move_to_element(button)
action.click()
action.perform()
 
time.sleep(15)
driver.quit()
 
 
pixel = robot.get_pixel(location_of_field)
if pixel == (expected_color):
robot.set_mouse_pos(location_of_field)
robot.click_mouse(button='left')
 
'''