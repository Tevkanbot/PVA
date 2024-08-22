from backend.voise import Voice
from backend.triggers import Trigger as tr
from backend.commands import Apps
import time


def main(end):

    vo = Voice()
    mic_status = False
    Apps.Search_File.get_desktop_shortcuts()
    print("Успешный запуск, ярлыки получены")

    while True:
        # Сначала проверяем новые команды, если есть то выполняем
        if end.poll():
            recived_data = end.recv()# Получаем словарь {"command": "какая-то команда", "data": "информация к этой команде"}

            if recived_data["command"] == "change_mic_status":
                mic_status = recived_data["data"]
                print("mic_status: ", mic_status)
                if mic_status:

                    end.send({"command": "send_message", "data": "Калибровка микрофона, обеспечьте тишину"})
                    time.sleep(1)
                    vo.calibrate_recognizer()
                    end.send({"command": "send_message", "data": "Калибровка микрофона завершена"})



        # Потом выполняем рекогнайз и команду при необходимости
        if mic_status:
            phrase = vo.get_phrase()
        else:
            continue
        if phrase is None:
            continue

        searched = tr.search_trigger(phrase, end)
        res = tr.search_number(searched, phrase)

        #print("res: ", res)

        if res["WordCount"] != 0:
            start_data = tr.start(res, phrase)
            message = str(f"Запущена команда: '{start_data}'")
            end.send({"command": "send_message", "data": message})