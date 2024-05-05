from voise import Voise
from data import Data
from commands import Audio, Desktop
import time
while True:
    voise = Voise()
    query = voise.get_phrase()
    print(query)
    desktop = Desktop()
    if query =="Закрой все окна":
        desktop.clear()
        print("srtthsrth")
