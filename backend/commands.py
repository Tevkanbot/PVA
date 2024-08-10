import pyautogui
import time
import os
from .sound import Sound
import winreg # Для работы с реестром Windows


class Audio:  # Работа со звуком

    pyautogui.FAILSAFE = True
    

    def volume(level):
        Sound.volume_set(level)

    def volumeup(level): # Volume up

        Sound.volume_up()

    def volumedown(level):  # Volume down
        Sound.volume_down()

    def mute(level):
        Sound.mute()
                

    def play(level):
        pyautogui.press('playpause')


class Apps:  # работа с браузером

    class Search_File:
        
        def find_browser():

            def find_browser_path(browser_name):
                #Ищет путь к браузеру по его имени.

                try:
                    # Открываем ключ реестра для браузеров
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths")

                    # Ищем ключ с именем браузера
                    with winreg.OpenKey(key, browser_name + ".exe") as browser_key:
                        # Извлекаем путь из значения по умолчанию
                        path, _ = winreg.QueryValueEx(browser_key, "")
                        return path

                except FileNotFoundError:
                    pass
                    return None

            yandex_path = find_browser_path("yandexbrowser")
            google_path = find_browser_path("chrome")

            if yandex_path:
                return yandex_path
        
            elif google_path:
                return google_path
        
        
            

    class browser:
        def open(level):
            browser_path = Apps.Search_File.find_browser()

            os.startfile(browser_path)

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


