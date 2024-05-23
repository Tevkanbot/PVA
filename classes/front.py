import eel
import json
import os
from .data import Data




#============================================================FRONT FUNCTIONS===================================================================


class Front:


    # Функция для проверки наличия имени пользователя
    def is_user_registered():


        data = Data.load_app_data()

        if data["name"] != "None":
            return True
        return False


    # Функция для сохранения пользователя в файл
    def save_user(name):

        data = Data.load_app_data()

        data['name'] = name.lower()

        Data.dump_app_data(data)


    # Функция для сохранения приложения в файл
    def save_app(input_value_1, input_value_2):

        data = Data.load_app_data()

        data["apps"][input_value_1] = input_value_2.lower()

        Data.dump_app_data(data)


    # Функция для сохранения сайта в файл
    def save_website(input_value_1, input_value_2):

        data = Data.load_app_data()

        data["websites"][input_value_1] = input_value_2.lower()

        Data.dump_app_data(data)


    # Главная функция. Запускаем UI
    def start_app():

        eel.init("C:\\Users\\HOME\\Desktop\\GLUE2\\PVA\\web")

        if Front.is_user_registered():
            eel.start('index.html', size=(700, 500))
            Front.send_message('Добро пожаловать') 
        else:
            eel.start('register.html', size=(700, 500))
 

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
    elif action == 'Выключение звука':
        print('Выключение звука')


@eel.expose
def send_message(message):
    # Здесь ваша логика для отправки сообщения
    eel.send_message_to_chat(message)


# Отправляем "Добро пожаловать" при запуске программы



@eel.expose
def enableMicrophone(state):
    
    if state:
        print("Включение микрофона")
        # Здесь должен быть код для включения микрофона
        send_message("Микрофон включен")
    else:
        print("Выключение микрофона")
        ("Микрофон выключен")