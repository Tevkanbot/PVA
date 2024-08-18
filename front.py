import eel
from pathlib import Path
from backend.data import Data
import threading
import multiprocessing
import os
from main import main as start_backend
import time


# Путь к папке с HTML, CSS и JS файлами
project_root = Path(__file__).resolve().parent.parent
web_dir = project_root / 'PVA' / 'frontend' / 'static'
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
    print(f"Отправка сообщения в чат: {message}")
    eel.display_message_in_chat(message)  # Это вызывает JavaScript функцию

@eel.expose
def on_load():
    # Функция вызывается из JavaScript
    send_message_to_chat("Добро пожаловать! Я PVA - Клей")

# Используем блокировку для предотвращения дублирования сообщений
message_lock = threading.Lock()
message_cache = set()  # Используем множество для хранения уже отправленных сообщений

def start_backend_thread(end):
    while True:
        if end.poll():
            data = end.recv()
            with message_lock:
                if data not in message_cache:
                    message_cache.add(data)
                    eel.display_message_in_chat(data)
            time.sleep(1)  # Возможно, это все-таки необходимо для предотвращения быстрого повторного вызова

def clear_message_cache():
    global message_cache
    while True:
        time.sleep(10)  # Очистка кэша каждые 10 секунд
        with message_lock:
            message_cache.clear()

@eel.expose
def main():
    end1, end2 = multiprocessing.Pipe()
    # process_2 = multiprocessing.Process(target=start_backend, args=(end1,), daemon=True)
    # process_2.start()
    backend_thread = threading.Thread(target=start_backend_thread, args=(end1,), daemon=True)
    backend_thread.start()

    # Запускаем поток для очистки кэша сообщений
    cache_clear_thread = threading.Thread(target=clear_message_cache, daemon=True)
    cache_clear_thread.start()

if __name__ == "__main__":
    # Запускаем Front.start_app() в основном потоке
    front_thread = threading.Thread(target=Front.start_app, daemon=True)
    front_thread.start()

    # Запускаем main() в отдельном потоке
    main_thread = threading.Thread(target=main, daemon=True)
    main_thread.start()

    # Даем потокам время на запуск
    front_thread.join()
    main_thread.join()
