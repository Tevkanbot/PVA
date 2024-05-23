from classes.voise import Voise as vo
from classes.front import Front as fr
from triggers import Trigger as tr

#import os
#from data import Data
#from commands import Audio

def main():

    fr.start_app()

    while True:
        phrase = vo.get_phrase()
        if phrase == None:
            continue
        
        print("phrase: ", phrase)#

        print(phrase.split()) 

        searched = tr.search_trigger(phrase)
        print("tr: ", searched)#

        res = tr.search_number(searched, phrase)
        print("res: ", res)#
        
        if res["WordCount"] != 0:
            tr.work(res)

            

if __name__ == "__main__":
    main()


