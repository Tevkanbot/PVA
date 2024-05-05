from voise import Voise
from data import Data
from commands import Audio
from triggers import Trigger

def main():

    #trig = Trigger(name = "гена")

    while True:
        phrase = Voise.get_phrase()
        print(phrase)
        do = Trigger.search_trigger(phrase)
        print(do)

        if do != False:
            Trigger.work(do)
            
if __name__ == "__main__":
    main()
