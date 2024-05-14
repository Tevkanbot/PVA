import pyautogui
import time
import os
from sound import Sound
class Audio:  # Работа со звуком

    pyautogui.FAILSAFE = True
    

    def volume(level):
        Sound.volume_set(level)

    def volumeup(level): # Volume up

        Sound.volume_up()
        #for i in range(level):
          
            #pyautogui.press('volumeup')
            # time.sleep(1)

    def volumedown(level):  # Volume down
        Sound.volume_down()

    def mute(level):
        Sound.mute()
                

    def play(level):
        pyautogui.press('playpause')


class Apps:  # работа с браузером
    class browser:
        def open(level):
            os.startfile("C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")
            #os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        def close(level):
            os.system("taskkill /f /im browser.exe")
            os.system("taskkill /f /im chrome.exe")

    class powerpoint:  # открытие преложений

        def open(level):
            os.startfile("POWERPNT.EXE")

        def close(level):
            os.system("taskkill /f /im POWERPNT.EXE")


class Desktop:  # работа с окнами

    def clear(level):
        pyautogui.hotkey('win','m')


