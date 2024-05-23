import json
class Data():
    
    def load_triggers(): # Получаем словарь из файла users.json и возвращаем его
        data = {} # рабочий словарь

        with open("jsons\\triggers_and_commands.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        return data

    def dump_triggers(data): # Проверяем что аргумент это словарь, и если это словарь, то сохраняем его в файл

        if type(data)!= dict:
            raise TypeError("Argument must be a dict")

        with open("jsons\\triggers_and_commands.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
            return True # Подтверждам успешное сохранение (для отладки мб пригодиться)
    


    def load_app_data(): # Получаем словарь из файла users.json и возвращаем его
        data = {} # рабочий словарь

        with open("C:\\Users\\User\\Desktop\\PVA\\PVA\\classes\\jsons\\app_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        return data



    def dump_app_data(data): # Проверяем что аргумент это словарь, и если это словарь, то сохраняем его в файл

        if type(data)!= dict:
            raise TypeError("Argument must be a dict")

        with open("C:\\Users\\User\\Desktop\\PVA\\PVA\\classes\\jsons\\app_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
            return True # Подтверждам успешное сохранение (для отладки мб пригодиться)
        
        
            

