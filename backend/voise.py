import speech_recognition

class Voice:
    def __init__(self):
        self.sr =  speech_recognition.Recognizer()

        self.sr.pause_threshold = 0.3
        self.sr.non_speaking_duration = 0.1

    def calibrate_recognizer(self):
        import time
        with speech_recognition.Microphone() as mic:
            print("Калибровка, ничего не говорите!")
            time.sleep(1)
            self.sr.adjust_for_ambient_noise(source=mic, duration=1)
            print("Калибровка завершена")
            

    def get_phrase(self):
        try:
            with speech_recognition.Microphone() as mic:
                print("<<<<<>>>>>")
                
                audio = self.sr.listen(source=mic, timeout=0.3)
                query = self.sr.recognize_google(audio_data=audio, language="ru-RU").lower()

                return query
            
        except speech_recognition.WaitTimeoutError:
            pass
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError as e:
            pass
    
if __name__ == "__main__":
    while True:
        print(Voice.get_phrase())