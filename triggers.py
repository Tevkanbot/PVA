from data import Data
from commands import Audio

class Trigger:
    def search_trigger(phrase):
        data = Data.load()
        #triggers = ["стоп", "продолжить", "пауза"]
        phrase = phrase.split()

        #print(phrase)
        #print(data["triggers"])
        for word in phrase:
            for trigger in data["triggers"]:
                if trigger == word:
                    return word
        return False            
    def work(trigWord):
        data = Data.load()
        #print(data["actions"][trigWord]["command"])

        exec(data["actions"][trigWord]["command"])

        print("я запустиль:", trigWord, ">>>", data["actions"][trigWord]["command"])
                 

                                    