'''
ATTENTION:
This script requires 2 things to be installed.
1. Python (https://www.python.org/downloads/)
2: pyautogui (https://pyautogui.readthedocs.io/en/latest/install.html)

--- CREDITS AND VIDEO LOCATIONS ---
GITHUB: https://github.com/PizzaGod873/mc-mapart-give-command - PizzaGod873
YOUTUBE: (link is being added at the time of recording this video) - @AndrewPCs
REDDIT: https://www.reddit.com/user/SuperPizza999/ (Multiple posts so profile is listed) - SuperPizza999
'''



# This is stuff for the script that helps it work. (NOT RECOMMENDED TO CONFIGURE)

import pyautogui as pag
import time as t

# MODIFY HERE

t.sleep(7.5) # Delay to get into Minecraft

for mmid in range(0, 0 + 1): # Modify the 1st and 2nd numbers to set the ID range.

# This is what actually does the stuff. (NOT RECOMMENDED TO CONFIGURE)

    pag.typewrite('t')
    pag.typewrite('/give @s minecraft:filled_map{map:'+f'{mmid}'+'}')
    pag.press('enter')
