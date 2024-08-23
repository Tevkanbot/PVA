import eel
from pathlib import Path
from backend.data import Data
import multiprocessing 
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
        return data["name"] != "None"
    
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
        end2.send({"command": "change_mic_status", "data": True})
    else:
        eel.display_message_in_chat("Выключение микрофона")
        end2.send({"command": "change_mic_status", "data": False})

@eel.expose
def toggleSwitch(isHidden):#Согласие с лицензией
        data = Data.load_app_data()
        data["Agree with license"] = "yes"
        Data.dump_app_data(data)

@eel.expose #Вытягивание имени пользователя (первая буква)
def get_initials_from_json():
    data = Data.load_app_data()
    name = data["name"]
    return name[:1]

@eel.expose
def send_Message_Input(message): #Отправка сообщение через строку ввода
    end2.send({"command": "text_command", "data": message})
    print(message)

@eel.expose
def on_load(): # Функция вызывается из JavaScript при запуске страницы
    eel.display_message_in_chat("Добро пожаловать! Я ваш Персональный Голосовой Ассистент - Клей")
    
    process_2 = multiprocessing.Process(target=start_backend, kwargs={"end": end1}, daemon=True)
    process_2.start()

@eel.expose
def wait_for_commands():
    if end2.poll():
        recived_data = end2.recv() # Получаем словарь {"command": "какая-то команда", "data": "информация к этой команде"}

        if recived_data["command"] == "send_message":
            eel.display_message_in_chat(recived_data["data"])

        elif recived_data["command"] == "send_message_as_user":
            eel.display_message_as_user(recived_data["data"])

if __name__ == "__main__":
    app_process = multiprocessing.Process(target=Front.start_app)
    app_process.start()