from backend.data import Data
from backend.commands import Audio, Apps, Desktop


class Trigger:
                
    def search_trigger(phrase):  # Ищем сначала активационное слово, затем триггеры во фразе
        
        start = False
        phrase = phrase.split()  # Разделяем фразу на слова

        for word in phrase:  # Ищем активационное слово, референс - фраза "Алиса"
            if word == "клей":
                start = True
                break

        if start:  # Если активатор найден, то ищем триггеры во фразе

            data = Data.load_triggers()  # Загружаем данные, в особенности триггерные слова
            two_word_triggers = data["two_word_triggers"]
            num = 0

            for two_word_triggers_list in two_word_triggers:  # Перебираем все двусловные триггеры

                two_word_triggers_list = two_word_triggers_list.split()  # Превращаем двусловный триггер в список

                for trigger_word in two_word_triggers_list:  # Перебираем все триггеры (слова) из двусловного триггера

                    for word in phrase:  # Перебираем все слова в фразе

                        if trigger_word == word:  # Если нашли совпадение

                            potential_trigger = two_word_triggers_list.copy()
                            
                            two_word_triggers_list.remove(trigger_word)
                            
                            remainWord = two_word_triggers_list.pop(0)

                            for word in phrase:
                                if word == remainWord:
                                    return {"WordCount": 2, "trigger": " ".join(potential_trigger), "num": num}
            
            # Если не нашли двусловные триггеры, ищем однословные триггеры
            for word in phrase:
                for trigger in data["one_word_triggers"]:
                    if trigger == word:
                        return {"WordCount": 1, "trigger": word, "num": num}
            
            # Если не найдены ни двусловные, ни однословные триггеры
            return {"WordCount": 0}

        else:
            # Если активационное слово не найдено
            return {"WordCount": 0}


    def search_number(fromSearch, phrase):

        phrase = phrase.split()
        num = 0
        num_words = ["ноль", "один","два","три","четыре","пять","шесть","семь","восемь","девять"]

        if fromSearch["WordCount"] != 0: 
            for word in phrase:
                if word.isdigit(): 
                             

                    num = int(word)
                    break
                else:
                    #
                    for el in num_words:
                        if word == el:
                            num = el.index(el)
            fromSearch["num"] = num
            
            return fromSearch

        else:
            return fromSearch



    def start(fromReturn):

        data = Data.load_triggers()

        trigWord = fromReturn["trigger"]
        
        num = fromReturn["num"]
        if fromReturn["WordCount"] == 1:
            exec(data["one_word_actions"][trigWord]["command"])

            print("Запущено:", trigWord, ">>>", data["one_word_actions"][trigWord]["command"])

        if fromReturn["WordCount"] == 2:
            exec(data["two_word_actions"][trigWord]["command"])

            print("Запущено:", trigWord, ">>>", data["two_word_actions"][trigWord]["command"])