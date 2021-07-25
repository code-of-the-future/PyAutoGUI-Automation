# Import the relevant modules
import pyautogui
import time

# Spiral drawing using pyautogui
time.sleep(3)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, button="left")
    pyautogui.dragRel(-distance, 0, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, button="left")
    # time.sleep(2)