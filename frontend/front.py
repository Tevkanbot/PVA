import eel
from pathlib import Path
from backend.data import Data
from fastapi import FastAPI

# Путь к папке с HTML, CSS и JS файлами
project_root = Path(__file__).resolve().parent.parent
web_dir = project_root / 'frontend' / 'static'
eel.init(web_dir.as_posix())

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
            eel.start('index.html', size=(700, 500), port=5000)
            send_message('Добро пожаловать')
        else:
            eel.start('register.html', size=(700, 500), port=5000)

    


    def send_new_message(phrase):
        send_message(phrase)
                


#==============================================================ELL FUNCTIONS======================================================================

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
        send_message_to_chat("Включение звука")
    elif action == 'Выключение звука':
        send_message_to_chat("Выключение звука")


@eel.expose
def enableMicrophone(state):
    if state:
        send_message_to_chat("Включение микрофона")
    else:
        send_message_to_chat("Выключение микрофона")
        

@eel.expose
def send_message_to_chat(message):
    eel.display_message_in_chat(message)

@eel.expose
def on_load():
    # Функция вызывается из JavaScript
    send_message_to_chat("Добро пожаловать! Я PVA - Клей")


if __name__ == "__main__":
    Front.start_app()  # Запуск приложения
