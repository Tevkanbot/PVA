from backend.voise import Voise
from backend.triggers import Trigger as tr
from backend.commands import Apps
import time


def main(end):

    vo = Voise()
    mic_status = False
    Apps.Search_File.get_desktop_shortcuts()
    print("Успешный запуск, ярлыки получены")

    while True:
        phrase = None
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
            elif recived_data["command"] == "text_command":
                phrase = recived_data["data"].lower()
                print("phrase: ", phrase)


        # Потом выполняем рекогнайз и команду при необходимости
        if mic_status and phrase is None:
            phrase = vo.get_phrase()

        elif phrase is not None:
            pass

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