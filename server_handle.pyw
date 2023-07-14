import pyautogui, time

while 1:
    if len(pyautogui.getWindowsWithTitle("127.0.0.1_/"))>0:
        pyautogui.getWindowsWithTitle("127.0.0.1_/")[0].maximize()

while 1:
    if len(pyautogui.getWindowsWithTitle("ChatGPT")) > 1:
        while 1:
            if len(pyautogui.getWindowsWithTitle("ChatGPT")) < 2:
                for w in pyautogui.getWindowsWithTitle("ChatGPT"):
                    w.close()
                exit()
            time.sleep(.5)
    time.sleep(.5)