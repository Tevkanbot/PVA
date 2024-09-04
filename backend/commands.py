import pyautogui
import time
import os
from .sound import Sound
import json
from .data import Data
import webbrowser


class Audio:  # Работа со звуком

    #pyautogui.FAILSAFE = True
    

    def volume(level):
        Sound.volume_set(level)

    def volumeup(): # повышение громкости звука

        Sound.volume_up()

    def volumedown():  # понижение громкости звука
        Sound.volume_down()

    def mute():
        Sound.mute()
                

    def play():
        pyautogui.press('playpause')


class Apps: 

    class Search_File:

        def get_desktop_shortcuts():
            
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            shortcuts = {}

            for filename in os.listdir(desktop_path):
                if filename.endswith(".lnk") or filename.endswith(".exe") or filename.endswith(".url"):\
                
                    shortcut_path = os.path.join(desktop_path, filename)
                    shortcut_name = os.path.splitext(filename)[0]

                    shortcuts[shortcut_name] = shortcut_path

            values = list(shortcuts.values())
            keys = list(shortcuts.keys())

            # фильтр
            for i in range(len(shortcuts)):

                word = keys[i]
                low = word.lower()
                rep = low.replace('.','')
                rep = rep.replace('cm fo42lnktz9vvrzo4 moquqon0gtzwytkd9viqwwzr4qemwspgj4q@g7oimasfyv94qort k15a862438af798f9 ','')
                rep = rep.replace('_','')
                rep = rep.replace('-','')
                rep = rep.replace('exe','')
                rep = rep.replace('(','')
                rep = rep.replace(')','')
                rep = rep.replace('1','')
                rep = rep.replace('2','')
                rep = rep.replace('3','')
                rep = rep.replace('4','')
                rep = rep.replace('5','')
                rep = rep.replace('6','')
                rep = rep.replace('7','')
                rep = rep.replace('8','')
                rep = rep.replace('9','')
                rep = rep.replace('0','')
                
                if rep[-1]== " ":
                    rep = rep[:-1]
                
                keys[i] = rep
                
                i=i+1

            arh = dict(zip(keys, values))

            data = Data.load_app_data()
            data["app"] = arh
            Data.dump_app_data(data)
            


       
    class Browser:
        def open():

            webbrowser.open('https://ya.ru', new=2)

        def close():
            pass
            #os.system("taskkill /f /im browser.exe")
            #os.system("taskkill /f /im chrome.exe")


    

    def open(phrase):
        phrase = phrase.split()

        data = Data.load_app_data()
        data = data["app"]
        keys = data.keys()
        keys = list(keys)
        num = 0

        for trigger_words in data:

            potential_trigger = trigger_words
            value = data.get(potential_trigger)
            trigger_words =  trigger_words.split()
            trigger_words = set(trigger_words)
            
            if  trigger_words.issubset(phrase) != False:
                os.startfile(value)
                
                return("триггер найден")
                
            else:
                print("") 


    def close_app(): # В процессе работы
        os.system(f"taskkill /f /im {Apps.Search_File.find_app_path()}")


class Desktop:  # работа с окнами

    def clear():
        pyautogui.hotkey('win','m')


if __name__ == "__main__":
    
    desktop_shortcuts = Apps.Search_File.get_desktop_shortcuts()
    

    print("Список ярлыков сохранен в файл app_data.json")

