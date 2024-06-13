## mc-mapart-give-command
This Repository is a Python script to automatically type give commands for mapart.
# Guide
# AND YES I AM VERY AWARE IT MIGHT NOT GIVE A FEW MAPS SOMETIMES
ATTENTION:
This script requires 2 things to be installed.   
1: Python (https://www.python.org/downloads/)   
2: pyautogui (https://pyautogui.readthedocs.io/en/latest/install.html)   
Install them to your computer or special test editor (like VS code)

### Video tutorial for configuration
[![Tutorial](https://img.youtube.com/vi/vZ7z6WNted4/maxresdefault.jpg)](https://youtu.be/vZ7z6WNted4)
### Configuration
Look at line 22. change the 7.5 in
```t.sleep(7.5) # Delay to get into Minecraft```
to the amount of time (in seconds) it takes you to click on Minecraft and resume.

Look at line 24 and modify the 0's
```for mmid in range(0, 0 + 1): # Modify the 1st and 2nd numbers to set the ID range.```
to be the range of map ID's.
