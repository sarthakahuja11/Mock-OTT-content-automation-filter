# !~~~ATTENTION~~~!
# This file should be added to the scripts of autokey.
# It can be done by using Autokey main window.
# Save this script as select_image
# This automation is suited for spacefm where ctrl-l activates the address bar and then searches image_name in that directory 
# change according to your file manager

import time

image_path = '/home/bsil/youtubedownloads/KOMEDI%20LUCU/converted/'
image_name = 'APEL'

keyboard.send_keys('<ctrl>+l')
keyboard.send_keys(image_path)

keyboard.send_keys('<enter>')
time.sleep(3)

#keyboard.send_keys('<ctrl>+f')
keyboard.send_keys(image_name)
keyboard.send_keys('<enter>')

