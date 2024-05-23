import eel
import json
import os
from data import Data

eel.init("web")



@eel.expose
def send_message(message):
    # Здесь ваша логика для отправки сообщения
    eel.send_message_to_chat(message)


# Отправляем "Добро пожаловать" при запуске программы
send_message('Добро пожаловать')


@eel.expose
def enableMicrophone(state):
    
    if state:
        print("Включение микрофона")
        # Здесь должен быть код для включения микрофона
        send_message("Микрофон включен")
    else:
        print("Выключение микрофона")
        send_message("Микрофон выключен")




@eel.expose
def toggle_sound(action):
    if action == 'Включение звука':
        print('Включение звука')
    elif action == 'Выключение звука':
        print('Выключение звука')





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





@eel.expose
def process_name(name):
    print(f"Имя пользователя: {name}")
    save_user(name)  # Сохраняем имя пользователя в файл

@eel.expose
def saveData(inputFieldValue, inputField2Value):
    print('Имя приложения:', inputFieldValue)
    print('Путь приложения:', inputField2Value)

@eel.expose
def saveData2(inputFieldValue2, inputField2Value2):
    print('Имя сайта:', inputFieldValue2)
    print('Ссылка на сайт:', inputField2Value2)

# Проверка наличия имени пользователя при запуске
if is_user_registered():
    eel.start('index.html', size=(700, 500))
else:
    eel.start('register.html', size=(700, 500))
    
    