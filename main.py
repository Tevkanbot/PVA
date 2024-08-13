from backend.voise import Voice
from frontend.front import Front as fr
from backend.triggers import Trigger as tr
import eel
from fastapi import FastAPI
import requests
import uvicorn
from multiprocessing import Process as pr

app = FastAPI()
vo = Voice()

def main():
    vo.calibrate_recognizer()

    while True:
        phrase = vo.get_phrase()
        if phrase is None:
            continue

        print(phrase)
        searched = tr.search_trigger(phrase)
        res = tr.search_number(searched, phrase)
        print("res: ", res)
        
        if res["WordCount"] != 0:
            tr.start(res)

@app.get("/api/microphone")
async def microphone(mic_status: bool):
    if mic_status:
        print("mic is on")
    elif not mic_status:
        print("mic is off")
        
    return mic_status

@app.get("/api/microphone/calibrate")
async def callibrate_microphone():
    vo.calibrate_recognizer()

    return "calibrated"

if __name__ == "__main__":

    process_1 = pr(target=main, args=(), daemon=True)
    process_2 = pr(target=fr.start_app, args=(), daemon=True)
    process_3 = pr(target=uvicorn.run, args=("main:app", ), kwargs={"host": "127.0.0.1", "port": 5000}, daemon=True)

    process_1.start()
    process_2.start()
    process_3.start()

    process_1.join()
    process_2.join()
    process_3.join()