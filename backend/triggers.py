from .data import Data
from .commands import *


class Trigger:
                
    def search_trigger(phrase, end):  # Ищем сначала активационное слово, затем триггеры во фразе
        
        probable_command = phrase
        start = False
        phrase = phrase.split()  # Разделяем фразу на слова

        for word in phrase:  # Ищем активационное слово, референс - фраза "Алиса"
            if word == "клей":
                start = True
                end.send({"command": "send_message_as_user", "data": probable_command})
                break

        if start: # Если активатор найден, то ищем триггеры во фразе
            print("клей найден")
            data = Data.load_triggers() # Загружаем данные, в особенности триггерные слова
            num = 0
            for trig in ["four","three","two","one"]:
                print(trig)
                n_word_triggers = data[f"{trig}_word_triggers"]
                
        
                for trigger_words in n_word_triggers:

                    potential_trigger = trigger_words

                    trigger_words =  trigger_words.split()
                    trigger_words = set(trigger_words)

                    if  trigger_words.issubset(phrase) != False:
                        print("триггер найден")
                        return {"WordCount": trig,"trigger": potential_trigger, "num":num}

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



    def start(fromReturn, phrase):

        data = Data.load_triggers()

        trigWord = fromReturn["trigger"]
        
        num = fromReturn["num"]
        if fromReturn["WordCount"] == "four":
            exec(data["four_word_actions"][trigWord]["command"])

            return trigWord

        if fromReturn["WordCount"] == "three":
            exec(data["three_word_actions"][trigWord]["command"])

            return trigWord
        
        if fromReturn["WordCount"] == "two":
            exec(data["two_word_actions"][trigWord]["command"])
            
            return trigWord #data["two_word_actions"][trigWord]["command"]

        if fromReturn["WordCount"] == "one":
            exec(data["one_word_actions"][trigWord]["command"])

            return trigWord