import eel
import asyncio
from pathlib import Path
from backend.data import Data
import multiprocessing 
import time
import os
from main import main as start_backend



# Путь к папке с HTML, CSS и JS файлами
project_root = Path(__file__).resolve().parent.parent
web_dir = project_root / 'PVA' / 'frontend' / 'static'
eel.init(web_dir.as_posix())

end1, end2 = multiprocessing.Pipe()

class Front:
    @staticmethod
    def is_user_registered():
        data = Data.load_app_data()
        return data.get("name") != "None"
    @staticmethod
    def save_user(name):
        data = Data.load_app_data()
        data['name'] = name.lower()
        Data.dump_app_data(data)
    @staticmethod
    def save_app(input_value_1, input_value_2):
        data = Data.load_app_data()
        data["apps"][input_value_1] = input_value_2.lower()
        Data.dump_app_data(data)
    @staticmethod
    def save_website(input_value_1, input_value_2):
        data = Data.load_app_data()
        data["websites"][input_value_1] = input_value_2.lower()
        Data.dump_app_data(data)
    @staticmethod
    def start_app():
        if Front.is_user_registered():
            eel.start('index.html', size=(700, 500), port=8000)
        else:
            eel.start('register.html', size=(700, 500), port=8000)
# ==============================================================
#                  EEL FUNCTIONS
# ==============================================================
@eel.expose
def process_name(name):
    print(f"Имя пользователя: {name}")
    Front.save_user(name)  # Сохраняем имя пользователя в файл

@eel.expose
def saveData(input_value_1, input_value_2):
    Front.save_app(input_value_1, input_value_2)

@eel.expose
def saveData2(input_value_1, input_value_2):
    Front.save_website(input_value_1, input_value_2)

@eel.expose
def toggle_sound(action):
    if action == 'Включение звука':
        eel.display_message_in_chat("Включение звука")
    elif action == 'Выключение звука':
        eel.display_message_in_chat("Выключение звука")

@eel.expose
def enableMicrophone(state):
    if state:
        eel.display_message_in_chat("Включение микрофона")
    else:
        eel.display_message_in_chat("Выключение микрофона")
    
    #await asyncio.sleep(1)

@eel.expose
def send_message_to_chat(message):
    print(f"Отправка сообщения в чат через: {message}")
    eel.display_message_in_chat(message)  # Это вызывает JavaScript функцию
    #await asyncio.sleep(1)


@eel.expose
def on_load():
    # Функция вызывается из JavaScript
    
    eel.display_message_in_chat("Добро пожаловать! Я PVA - Клей")
    
    process_2 = multiprocessing.Process(target=start_backend, kwargs={"end": end1}, daemon=True)
    process_2.start()

    #frontend_process = multiprocessing.Process(target=main)
    #frontend_process.start()    

@eel.expose
def search_and_send_message():

    if end2.poll():
        data = end2.recv()
        print("data: ", data)
        eel.display_message_in_chat(data)   

if __name__ == "__main__":


    process_3 = multiprocessing.Process(target=Front.start_app)
    process_3.start()