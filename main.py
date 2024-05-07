from voise import Voise
from triggers import Trigger

#import os
#from data import Data
#from commands import Audio

def main():
    #trig = Trigger(name = "гена")

    while True:
        phrase = Voise.get_phrase()
        print(phrase)
        tr = Trigger.search_trigger
        res = Trigger.search_number(tr, phrase)

        if res != 0:

            Trigger.work(res)

            

if __name__ == "__main__":
    main()


