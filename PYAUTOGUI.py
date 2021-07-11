# Import the relevant modules
import pyautogui
import time

# Give the python file some time before continuing
time.sleep(3)

# Mouse Functions
# Prints the resolution of your screen
print(pyautogui.size())
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (3 seconds)
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)

# Click
pyautogui.click(500, 500, 3, 3, button="left")
pyautogui.tripleClick()
pyautogui.doubleClick()
pyautogui.leftClick()
pyautogui.rightClick()

# Scrolls up 500
pyautogui.scroll(500)
# Scrolls down 500
pyautogui.scroll(-500)

# Mouse up and down
pyautogui.mouseUp(100, 100, button="left")
pyautogui.mouseDown(100, 100, button="left")

# Example of mouse up and down
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)

# Intermittent drawing of lines on paint - NOT MENTIONED IN YOUTUBE VIDEO
time.sleep(3)
pyautogui.mouseDown(300, 400, button='left')
pyautogui.moveTo(500, 400)
pyautogui.mouseUp()
pyautogui.moveTo(700, 400)
pyautogui.mouseDown()
pyautogui.moveTo(900, 400)


# Spiral drawing using pyautogui
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
    time.sleep(4)


# TikTok Liker - example
time.sleep(3)
# range will be the number of TikTok's you want to like
for i in range(10):
    pyautogui.moveTo(450, 500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(854, 515)
    time.sleep(1)
    pyautogui.leftClick()


# Keyboard functions
pyautogui.write("hello")
pyautogui.press("enter")
pyautogui.press("space")

# Dino Game - Chrome
time.sleep(3)
for i in range(20):
    pyautogui.press("space")
    time.sleep(0.5)

# Screenshot in pyautogui
pyautogui.screenshot("screenshot.png")





