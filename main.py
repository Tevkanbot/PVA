from backend.voise import Voice
#from front import main as front_main
from backend.triggers import Trigger as tr
import eel
from multiprocessing import Process as pr
from multiprocessing import Pipe as pipe


def main(end):
    #print(end)
    vo = Voice()
    vo.calibrate_recognizer()

    while True:
        phrase = vo.get_phrase()
        if phrase is None:
            continue
        end.send(phrase)
        print(phrase)
        continue
        searched = tr.search_trigger(phrase)
        res = tr.search_number(searched, phrase)
        print("res: ", res)

        if res["WordCount"] != 0:
            tr.start(res)
    
     
    

if __name__ == "__main__":
    pass