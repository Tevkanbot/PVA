import pyautogui
import time
import os
#from .sound import Sound
import json
import winreg # Для работы с реестром Windows
from .data import Data


class Audio:  # Работа со звуком

    pyautogui.FAILSAFE = True
    

    def volume(level):
        Sound.volume_set(level)

    def volumeup(level): # повышение громкости звука

        Sound.volume_up()

    def volumedown(level):  # понижение громкости звука
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


        def get_desktop_shortcuts():
            
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            shortcuts = {}

            for filename in os.listdir(desktop_path):
                if filename.endswith(".lnk") or filename.endswith(".exe") or filename.endswith(".url"):
                    shortcut_path = os.path.join(desktop_path, filename)
                    shortcut_name = os.path.splitext(filename)[0]
                    shortcuts[shortcut_name] = shortcut_path

            values = list(shortcuts.values())
            keys = list(shortcuts.keys())

            #фильтр
            for i in range(len(shortcuts)):
                word = keys[i]
                low = word.lower()
                rep = low.replace('.','')
                rep = rep.replace('_',' ')
                rep = rep.replace('-','')
                rep = rep.replace('exe','')
                rep = rep.replace('(','')
                rep = rep.replace(')','')
                rep = rep.replace('cm fo42lnktz9vvrzo4 moquqon0gtzwytkd9viqwwzr4qemwspgj4q@g7oimasfyv94qort k15a862438af798f9 ','')
                keys[i] = rep
                
                i=i+1

            print(type(keys))
            print(type(values))

            arh = dict(zip(keys, values))
            print(arh)
            print(type(arh))

            data = Data.load_app_data()
            data["app"] = arh
            print(data)
            Data.dump_app_data(data)
            


       
    class Browser:
        def open(level):
            browser_path = Apps.Search_File.find_browser()

            os.startfile(browser_path)

        def close(level):
            os.system("taskkill /f /im browser.exe")
            os.system("taskkill /f /im chrome.exe")


    class Open_Close_App:  # открытие и закрытие преложений

        def open_app(level):

            if Apps.Search_File.find_app_path():
                os.startfile(f"{Apps.Search_File.find_app_path()}")

            else: 
                return None

        def close_app(level):
            os.system(f"taskkill /f /im {Apps.Search_File.find_app_path()}")


class Desktop:  # работа с окнами

    def clear(level):
        pyautogui.hotkey('win','m')


if __name__ == "__main__":
    
    desktop_shortcuts = Apps.Search_File.get_desktop_shortcuts()
    

    print("Список ярлыков сохранен в файл app_data.json")


