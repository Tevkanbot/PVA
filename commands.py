import pyautogui
class Audio:


    pyautogui.FAILSAFE = True


    def volumeup(): # Volume up
        for i in range(10):
            pyautogui.press('volumeup')
                                

    def volumedown(): # Volume down
        for i in range(10):
            pyautogui.press('volumedown')

    def mute():
        pyautogui.press('volumemute')
                

                
