import pyautogui
import time

while True:
    time.sleep(2)
    xt = time.time()
    pyautogui.screenshot()
    print("lol")
    print(float(time.time()-xt))
