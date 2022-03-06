import pyautogui
import time
from pynput import keyboard

i=1
def funkcja():
    global i
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\jular\OneDrive\Pulpit\projekt\test\screenshot'+str(i)+'.jpg')
    print("screenshot zrobiony")
    i=i+1
    

def on_press(key):
    while True:
        if key == keyboard.Key.enter:
            funkcja()
            time.sleep(2)
            if key == keyboard.Key.esc:
                return False

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()