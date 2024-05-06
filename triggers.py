from data import Data
from commands import Audio, Apps, Desktop

class Trigger:
    def __init__(s, name):
        s.name = name.lower()
                
    def search_trigger(phrase): #ищем снала анктивационное слово, затем тригеры во фразе
        
        phrase = phrase.split() # Разделяем фразу на слова
        
        start = False

        forReturn = {}

        for word in phrase:
            if word == "гена":
                print("ГЕНА обнаружен \n")
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
                                    forReturn =  {"WordCount": 2, "trigger": " ".join(copy)}
                                    break


                        if forReturn["WordCount"] != 0:# КОСТЫЛЬ ЛЮТЫЙ ПРОСТО, не расстреливайте за такое прошу...
                            break
                    if forReturn["WordCount"] != 0:# КОСТЫЛЬ ЛЮТЫЙ ПРОСТО, не расстреливайте за такое прошу...
                        break
                if forReturn["WordCount"] != 0:# КОСТЫЛЬ ЛЮТЫЙ ПРОСТО, не расстреливайте за такое прошу...
                    break

                

                                                                                                                

                            
#----------------Потом одноСловные тригеры---------------------------------------------------------

            for word in phrase:
                for trigger in data["OneWordTriggers"]:
                    if trigger == word:
                        forReturn =   {"WordCount": 1, "trigger": word}
                        break

            if forReturn != {"WordCount": 1, "trigger": word}:
                forReturn =  {"WordCount": 0}
            
#----------------Нужно ли искать число? Если да то ищем---------------------------------------------------------            
            #data = Data.load()
            #if forReturn["WordCount"] == 1:
                #if data["OneWordActions"][trigger] == True:






            return forReturn
        else:
            return {"WordCount": 0}
                                
    def work(wordsCount, trigWord):

    
        data = Data.load()

        if wordsCount == 1:
            exec(data["OneWordActions"][trigWord]["command"])

            print("я запустиль:", trigWord, ">>>", data["OneWordActions"][trigWord]["command"])

        if wordsCount == 2:
            exec(data["TwoWordsActions"][trigWord]["command"])

            print("я запустиль:", trigWord, ">>>", data["TwoWordsActions"][trigWord]["command"])