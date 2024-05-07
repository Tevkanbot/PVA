import pyautogui
import time
import os


class Audio:  # Работа со звуком

    pyautogui.FAILSAFE = True

    def volumeup(level):  # Volume up
        for i in range(5):
            pyautogui.press('volumeup')
            # time.sleep(1)

    def volumedown(level):  # Volume down
        for i in range(5):
            pyautogui.press('volumedown')
            # time.sleep(1)

    def mute(level):
        pyautogui.press('volumemute')

    def play(level):
        pyautogui.press('playpause')


class Apps:  # работа с браузером
    class browser:
        def open(level):
            #os.startfile("C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

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


