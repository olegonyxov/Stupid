import pyautogui
import time

while True:

    xt = time.time()
    time.sleep(1)
    pyautogui.screenshot(region=(0, 0, 10, 10))
    print("lol")
    print(float(time.time()-xt))
