import eel
import json
from pathlib import Path
from backend.data import Data








@eel.expose
def send_message(message):
    # Здесь ваша логика для отправки сообщения
    eel.send_message_to_chat(message)


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
        # Определяем путь к корню проекта
        project_root = Path(__file__).resolve().parent.parent
        web_dir = project_root / 'web'

        # Инициализация Eel с использованием относительного пути
        eel.init(web_dir.as_posix())

        if Front.is_user_registered():
            eel.start('index.html', size=(700, 500), port=8001)
            send_message('Добро пожаловать')
        else:
            eel.start('register.html', size=(700, 500), port = 8001)

    


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
        print('Включение звука')
        send_message("Включение звука")
    elif action == 'Выключение звука':
        print('Выключение звука')
        send_message("Выключение звука")



@eel.expose
def enableMicrophone(state):
    if state:
        print("Включение микрофона")
        # Здесь должен быть код для включения микрофона
        send_message("Микрофон включен")
    else:
        print("Выключение микрофона")
        send_message("Микрофон выключен")

# Пример вызова для запуска приложения
