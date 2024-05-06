import pyautogui
import time
import os
class Audio:               #Работа со звуком

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




class Apps:               #работа с браузером
    class browser:
        def open():
            os.startfile("C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe") #C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe

        def close():
            os.system("taskkill /f /im browser.exe")
            os.system("taskkill /f /im chrome.exe")

    class powerpoint:
        
        def open():
            os.startfile("")

        def close():
            os.system("")
                                



class Desktop():         #работа с окнами

    def clear():
        pyautogui.hotkey('win','m')

                
