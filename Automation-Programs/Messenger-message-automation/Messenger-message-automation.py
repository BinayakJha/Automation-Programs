import pyautogui
import time
time.sleep(5)
text = "This is a message automation"
while true:
  pyautogui.typewriter(text)
  time.sleep(1)
  pyautogui.press('enter')
  

