# This script automatically allows user to remotely login to the OTT platform backend and choose channel name. Then the corresponding video is uploaded and 
# thumbnail is loaded from local storage file. It is followed by alloting correct labels, sub categories and radio button selections.
# Considering upload time according to network bandwidth, the final submission of video is done or can be saved as a draft (scheduling upload date/time) 

import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from credentials import username, password, description_file
from selenium.webdriver.common import action_chains

# FIREFOX
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
#driver.set_window_size(1800,1200)
driver.maximize_window()


url = 'https://mp.abcEncrypted.com/login'
driver.get(url)
time.sleep(2)

field = driver.find_element_by_css_selector("input[type='text']")
field.send_keys('ComedyWebseries')
field = driver.find_element_by_css_selector("input[type='password']")
field.send_keys('Password2021')
time.sleep(2)
button=driver.find_element_by_css_selector("button[type='button']")
button.click()

print("LOGGED IN")

time.sleep(2)

############### BIG LOOP START #########################

driver.find_element_by_css_selector("li[class='tab-item post']").click()

time.sleep(5)

driver.find_element_by_css_selector("div[class='drap-wrap']").click()                #sendKeys("/home/downloads/KOMEDI_LUCU/converted/APEL.mp4")

time.sleep(2)

os.system('autokey-run -s select_video')

time.sleep(40)

print("VIDEO UPLOADED")


field = driver.find_element_by_css_selector("input[class='el-input__inner']")
field.send_keys('APEL')

field = driver.find_element_by_css_selector("textarea[class='el-textarea__inner']")
field.send_keys('APEL')

driver.find_element_by_xpath("//div[@class='el-select el-select--medium']").click()                                                       #language
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[2]").click()

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[6]/div/div").click()     #label1
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[16]").click()

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[7]/div/div").click()     #label2
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]").click()

time.sleep(5)                                                                                                                             #radio-button - Specialsis 

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[11]/div/div/div[1]/span[3]/span/label").click()
 
time.sleep(3)

driver.find_element_by_css_selector("div[class='default_cover_wrap cover_wrap']").click()                                     #sendKeys("/home/downloads/KOMEDI_LUCU/converted/APEL.jpg")

time.sleep(3)

os.system('autokey-run -s select_thumb')

#click on Submit button
driver.find_element_by_css_selector("button[class='el-button el-button--primary el-button--medium']").click()  

time.sleep(10)

print("FILLED DETAILS")

#click on Save as draft button
driver.find_element_by_css_selector("button[class='el-button el-button--default el-button--medium']").click()  

print("SAVED DRAFT")

############### BIG LOOP END #########################

#Go in loop - click on post now - then repeat for next image - see autorun scripts

driver.quit()


#Alternative Approach - can be optimised/ignored from here

driver.execute_script("arguments[0].scrollIntoView();", elem);
actions = action_chains.ActionChains(driver)
actions.move_to_element(elem)
time.sleep(2)
actions.click()
actions.perform()

Dropdown_Element = driver.find_element_by_xpath("//*[text()='Asia']").click()
actions = ActionChains(driver)
# Click on the element using the click(on_element=)s
actions.click(on_element=Dropdown_Element)
time.sleep(2)
actions.perform()

ddelement= Select(driver.find_element_by_xpath("//li[@class='el-select-dropdown__item']"))
ddelement.select_by_visible_text('Asian')

driver.find_element_by_xpath("//div[@class='el-select-dropdown__item]//li[contains(text(),'Asia')]").click()

driver.find_element_by_xpath("//div[@class='el-input el-input--medium el-input--suffix']").paste()  #"Asia" + Keys.ENTER)
driver.find_element_by_xpath("//li[contains(text(),'Asian')]").click()
driver.find_element_by_xpath("//li[@class='el-select-dropdown__item']/span[Asian]").click()

driver.find_element_by_css_selector("div[class='el-select el-select--medium']").click()

ddelement= Select(driver.find_element_by_css_selector("div[class='el-select el-select--medium']"))      #.click()
ddelement.select_by_visible_text('Asian')

chwnd = driver.window_handles[0]
#to switch focus the first child window handle
driver.switch_to.window(chwnd)

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

pixel = robot.get_pixel(location_of_field)
if pixel == (expected_color):
robot.set_mouse_pos(location_of_field)
robot.click_mouse(button='left')


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


