from typing import Any
from data import Data
from commands import Audio, Apps, Desktop

class Trigger:
                
    def search_trigger(phrase): #ищем снала анктивационное слово, затем тригеры во фразе
        
        phrase = phrase.split() # Разделяем фразу на слова
        
        start = False

        for word in phrase:
            if word == "клей":
                print("КЛЕЙ обнаружен \n")
                start = True
                break


        if start == True: # Если активатор найден, то ищем тригеры во фразе


            data = Data.load() # Загружаем данные, в особенности тригерные слова

#----------------- Снача ищем двуСловные тригеры--------------------------------------------------------------------
            twoWordsTriggers = data["TwoWordsTriggers"]
            #print(twoWordsTriggers)

            for TWTList in twoWordsTriggers: # Перебираем все двуСловные тригеры

                TWTList = TWTList.split() # Превращаем двуСловный тригер в список
                #print (TWTList)
                for trigWord in TWTList: # Перебираем все тригеры(слова) из двуСловного тригера

                    for word in phrase: # Перебираем все слова в фразе

                        if trigWord == word: # Если нашли совпадение


                            print("Первый из 2 тригеров найден!")
                            copy = TWTList.copy()

                            #TWTList.remove(trigWord)
                            
                            TWTList.remove(trigWord)
                            
                            remainWord = TWTList.pop(0)

                            for word in phrase:
                                if word == remainWord: #TWTList.pop(0)
                                    print("Второй из 2 тригеров найден----", copy)
                                    num = False
                                    if data["TwoWordsActions"][" ".join(copy)]["num"] :
                                        num = True
                                    return {"WordCount": 2, "trigger": " ".join(copy), "num": num}
                

                                                                                                                

                            
#----------------Потом одноСловные тригеры---------------------------------------------------------

            for word in phrase:
                for trigger in data["OneWordTriggers"]:
                    if trigger == word:
                        return {"WordCount": 1, "trigger": word, "num": num}
                        
            

        else:
            return {"WordCount": 0}
                                

        

    def search_number(fromSearch, phrase):
        
        num = False

        if fromSearch["WordCount"] != 0:
            if fromSearch["num"] == True:
                for item in phrase:
                    try:
                        num =  int(item)
                        break

                    except ValueError:
                        pass
                fromSearch["num"] = num

        
        
                return fromSearch

                        
                        

        else:
            return False



    def work(fromReturn):

    
        data = Data.load()

        trigWord = fromReturn["trigger"]
        num = fromReturn["num"]
        if fromReturn["WordCount"] == 1:
            exec(data["OneWordActions"][trigWord]["command"])

            print("я запустиль:", trigWord, ">>>", data["OneWordActions"][trigWord]["command"])

        if fromReturn["WordCount"] == 2:
            exec(data["TwoWordsActions"][trigWord]["command"])

            print("я запустиль:", trigWord, ">>>", data["TwoWordsActions"][trigWord]["command"])