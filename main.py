from voise import Voise
from data import Data
from commands import Audio
from triggers import Trigger
import os
def main():
    #trig = Trigger(name = "гена")

    while True:
        phrase = Voise.get_phrase()
        print(phrase)

        if Trigger.search_trigger(phrase)["WordCount"] != 0:
            Trigger.work(Trigger.search_trigger(phrase)["WordCount"], Trigger.search_trigger(phrase)["trigger"])
            
if __name__ == "__main__":
    main()
