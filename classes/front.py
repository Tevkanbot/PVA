import eel

class Front:
    def __init__(self):
        eel.init("web")


        @eel.expose
        def process_name(name):
            # Обработка имени пользователя
            print(f"Имя пользователя: {name}")
            # Здесь может быть код для сохранения имени или другие действия

        @eel.expose
        def saveData(inputFieldValue, inputField2Value):
            print('Имя приложения:', inputFieldValue)
            print('Путь приложения:', inputField2Value)
        
        @eel.expose
        def saveData2(inputFieldValue2, inputField2Value2):
            print('Имя сайта:', inputFieldValue2)
            print('Ссылка на сайт:', inputField2Value2)


        @eel.expose
        def forward_button_pressed():  #отправка о завершении регистрации 
            print(1)


        # Запуск приложения
        eel.start('index.html', size=(700, 500))  # Размер окна приложения