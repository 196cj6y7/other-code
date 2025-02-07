import pyautogui
import time

time.sleep(1)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
