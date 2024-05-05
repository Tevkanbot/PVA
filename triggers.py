from data import Data
from commands import Audio

class Trigger:
    def __init__(self, name):
        self.name = name.lower()
                
    def search_trigger(phrase): #ищем снала анктивационное слово, затем тригеры во фразе
        
        phrase = phrase.split() # Разделяем фразу на слова
        
        start = False

        for word in phrase:
            if word == "гена":
                print("Активатор обнаружен \n")
                start = True


        if start == True: # Если активатор найден, то ищем тригеры во фразе


            data = Data.load() # Загружаем данные, в особенности тригерные слова

            #print(phrase)
            #print(data["triggers"])

            for word in phrase:
                for trigger in data["triggers"]:
                    if trigger == word:
                        return word
            return False
        

        
        else:
            return False
                                
    def work(trigWord):
        data = Data.load()
        #print(data["actions"][trigWord]["command"])

        exec(data["actions"][trigWord]["command"])

        print("я запустиль:", trigWord, ">>>", data["actions"][trigWord]["command"])
                 

                                    