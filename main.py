from classes.voise import Voise as vo
from classes.front import Front as fr
from triggers import Trigger as tr

from multiprocessing import Process as pr

#import os
#from data import Data
#from commands import Audio

def main():

    #fr.start_app()

    while True:
        phrase = vo.get_phrase()
        if phrase == None:
            continue
        
        fr.send_new_message(phrase)

        #print(phrase.split()) 

        searched = tr.search_trigger(phrase)
        #print("tr: ", searched)#

        res = tr.search_number(searched, phrase)
        print("res: ", res)#
        
        if res["WordCount"] != 0:
            tr.work(res)

            

if __name__ == "__main__":
    process_1 = pr(target=main, args=(), daemon=True)
    process_2 = pr(target=fr.start_app, args=(), daemon=True)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
    
    
    # main()


