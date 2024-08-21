from .data import Data
#from commands import Audio, Apps, Desktop


class Trigger:
                
    def search_trigger(phrase):  # Ищем сначала активационное слово, затем триггеры во фразе
        

        start = False
        phrase = phrase.split()  # Разделяем фразу на слова

        for word in phrase:  # Ищем активационное слово, референс - фраза "Алиса"
            if word == "клей":
                start = True
                break

        if start: # Если активатор найден, то ищем триггеры во фразе
            print("клей найден")
            data = Data.load_triggers() # Загружаем данные, в особенности триггерные слова
            num = 0
            for trig in ["four","three","two","one"]:
                print(trig)
                n_word_triggers = data[f"{trig}_word_triggers"]
                
        
                for trigger_words in n_word_triggers:
                    print(trigger_words)
                    trigger_words =  trigger_words.split()
                    trigger_words = set(trigger_words)
                    if  trigger_words.issubset(phrase) != False:
                        print("триггер найден")
                        return {"WordCount": trig,"триггер":phrase,"num":num}
                    else:
                        print("триггер не найден")
                        

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