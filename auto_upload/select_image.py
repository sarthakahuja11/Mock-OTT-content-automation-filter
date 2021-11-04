# !~~~ATTENTION~~~!
# This file should be added to the scripts of autokey.
# It can be done by using Autokey main window.
# Save this script as select_image
# This automation is suited for spacefm where ctrl-l activates the address bar and then searches image_name in that directory 
# change according to your file manager



import time

image_path = "/home/downloads/KOMEDI_LUCU/converted"     #try removing / before home

#image_name = 'APEL'

#keyboard.send_keys('<ctrl>+l')
#keyboard.send_keys(image_path)
#keyboard.send_keys('<ctrl>+v')
time.sleep(2)

keyboard.send_keys('<enter>')
time.sleep(2)

#keyboard.send_keys('<ctrl>+f')
#keyboard.send_keys('APEL.mp4')
keyboard.send_keys('<enter>')

time.sleep(10)
