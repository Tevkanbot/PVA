import eel
import json
import os


eel.init("C:\\Users\\HOME\\Desktop\\GLUE2\\PVA\\web")
users_file = 'users.json'


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
    try:
        with open(users_file, 'r', encoding='utf-8') as file:
            users = json.load(file)
            # Проверяем, есть ли хотя бы один пользователь в списке
            return len(users) > 0
    except (json.JSONDecodeError, FileNotFoundError):
        return False

# Функция для сохранения пользователя в файл
def save_user(name):
    # Читаем существующий список пользователей или создаем пустой список, если файла нет
    try:
        with open(users_file, 'r', encoding='utf-8') as file:
            users = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        users = []

    # Добавляем нового пользователя в список
    users.append({'name': name})

    # Сохраняем обновленный список пользователей в файл
    with open(users_file, 'w', encoding='utf-8') as file:
         json.dump(users, file, ensure_ascii=False, indent=4)

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
    print('Имя сайта:', inputFieldValue2)
    print('Ссылка на сайт:', inputField2Value2)

# Проверка наличия имени пользователя при запуске
if is_user_registered():
    eel.start('index.html', size=(700, 500))
else:
    eel.start('register.html', size=(700, 500))
    
    