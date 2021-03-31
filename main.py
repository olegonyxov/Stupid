import time
import pyautogui
from pynput.mouse import Button, Controller
mouse = Controller()
while True:
    xt = time.time()
    time.sleep(1)
#   if pyautogui.pixelMatchesColor(734, 405, (204, 59, 12), tolerance=10):
#   print("catching")
#   print("waiting")
    if 1 == 0:
                print("down")
    else:
        mouse.press(Button.left)
        print("UP")
        print(time.time() - xt)
