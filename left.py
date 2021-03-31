import time
import pyautogui
import mouse

while True:

    xt = time.time()
    time.sleep(1)

    if pyautogui.pixelMatchesColor(734, 405, (204, 59, 12), tolerance=10):
        print("catching")
        print("waiting")
    else:

        print("UPed")
        print(float(time.time() - xt))
