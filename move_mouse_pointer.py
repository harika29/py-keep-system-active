import pyautogui
import time

# Check if the application (pycharm / terminal) accessibility to control the monitor is enabled
pyautogui.FAILSAFE = False
while True:
    time.sleep(2)
    for i in range(0, 100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 2):
        pyautogui.press('shift')
