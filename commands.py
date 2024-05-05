import pyautogui
import time
import os
class Audio:


    pyautogui.FAILSAFE = True


    def volumeup(): # Volume up
        for i in range(5):
            pyautogui.press('volumeup')
            #time.sleep(1)
                                
    def volumedown(): # Volume down
        for i in range(5):
            pyautogui.press('volumedown')
            #time.sleep(1)

    def mute():
        pyautogui.press('volumemute')
    
    def play():
        pyautogui.press('playpause')
                
class Apps:
    class browser:
        def open():
            os.startfile("C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")

        def close():
            os.system("taskkill /f /im browser.exe")
                    

                
