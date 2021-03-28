import time
import pyautogui

while True:
    xt = time.time()
    time.sleep(1)
    #    if pyautogui.pixelMatchesColor(734, 405, (204, 59, 12), tolerance=10):
    #       print("catching")
    print("waiting")
    if pyautogui.pixelMatchesColor(665, 397, (67, 122, 29), tolerance=10):
        pyautogui.mouseDown()
        print("down")
    else:
        pyautogui.mouseUp()
        print("UP")
        print(time.time() - xt)
