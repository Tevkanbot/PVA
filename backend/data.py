import json
import os
import sys

class Data:
    # Определяем путь к директории скрипта
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    @staticmethod
    def load_triggers():
        # Путь к файлу triggers_and_commands.json
        file_path = os.path.join(Data.script_dir, "backend", "jsons", "triggers_and_commands.json")
        
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        return data

    @staticmethod
    def dump_triggers(data):
        if not isinstance(data, dict):
            raise TypeError("Argument must be a dict")
        
        # Путь к файлу triggers_and_commands.json
        file_path = os.path.join(Data.script_dir, "backend", "jsons", "triggers_and_commands.json")
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, sort_keys=True)
        
        return True
    
    @staticmethod
    def load_app_data():
        # Путь к файлу app_data.json
        file_path = os.path.join(Data.script_dir, "backend", "jsons", "app_data.json")
        
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        return data

    @staticmethod
    def dump_app_data(data):
        if not isinstance(data, dict):
            raise TypeError("Argument must be a dict")
        
        # Путь к файлу app_data.json
        file_path = os.path.join(Data.script_dir, "backend", "jsons", "app_data.json")
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, sort_keys=True)
        
        return True
    