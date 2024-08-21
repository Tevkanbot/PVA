from backend.voise import Voice
from backend.triggers import Trigger as tr
#from multiprocessing import Pipe

def main(end):

    vo = Voice()
    mic_status = True
    vo.calibrate_recognizer()
    

    while True:
        # Сначала проверяем новые команды, если есть то выполняем
        if end.poll():
            recived_data = end.recv()# Получаем словарь {"command": "какая-то команда", "data": "информация к этой команде"}

            if recived_data["command"] == "change_mic_status":
                mic_status = recived_data["data"]
                print("mic_status: ", mic_status)



        # Потом выполняем рекогнайз и команду при необходимости
        if mic_status:
            phrase = vo.get_phrase()
        else:
            continue
        if phrase is None:
            continue

        end.send({"command": "send_message", "data": phrase})

        searched = tr.search_trigger(phrase)
        res = tr.search_number(searched, phrase)

        print("res: ", res)

        if res["WordCount"] != 0:
            start_data = tr.start(res)
            end.send({"command": "send_message", "data": start_data})