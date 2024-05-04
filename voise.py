import speech_recognition
#import pyaudio

class Voise:
    def get_phrase(): # Получает разделённый на фразы голос, если не нашли то возвращает "NOTEXT"
        try:
            with speech_recognition.Microphone() as mic:

                sr = speech_recognition.Recognizer()
                sr.pause_threshold = 0.5

                sr.adjust_for_ambient_noise(source=mic, duration=0.2)

                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()

                return query
        except speech_recognition.UnknownValueError:
            return "NOTEXT"
        

        























        #if query == "создай функцию":
            #sr = speech_recognition.Recognizer()
            #sr.pause_threshold = 0.5


        
            #print("Hello world")
            #if query == "название":
                #print("запись работает")


            #if query == "значение фунции":
                #print("херь сработала")

            #print("работает")
            #write(query, 'Hernya.json')