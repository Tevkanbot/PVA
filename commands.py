import pyautogui
import time
import os
import winsound as sound
class Audio:               #Работа со звуком

    pyautogui.FAILSAFE = True

    def volumeup(level): # Volume up
        for i in range(level):
            pyautogui.press('volumeup')
            time.sleep(1)

    def volumedown(level): # Volume down
        for i in range(level):
            pyautogui.press('volumedown')
            time.sleep(1)

    def mute(level):
        pyautogui.press('volumemute')
    
    def play(level):
        pyautogui.press('playpause')




class Apps:               #работа с браузером
    class browser:
        def open(level):
            os.startfile("C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe") #C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe

        def close(level):
            os.system("taskkill /f /im browser.exe")
            os.system("taskkill /f /im chrome.exe")

    class powerpoint:
        
        def open(level):
            os.startfile("")

        def close(level):
            os.system("")
                                



class Desktop():         #работа с окнами

    def clear(level):
        pyautogui.hotkey('win','m')

                
