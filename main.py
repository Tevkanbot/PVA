from backend.voise import Voise as vo
from frontend.front import Front as fr
from backend.triggers import Trigger as tr
import eel

from multiprocessing import Process as pr

#import os
#from data import Data
#from commands import Audio
#fr.send_new_message("test")



def main():

    #fr.start_app()
    
    while True:
        phrase = vo.get_phrase()
        if phrase == None:
            continue
        
        #fr.send_new_message("ASD[ASdd[asDFJKSaldfhaksdyfGD,FK]]")




        print(phrase) 

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


