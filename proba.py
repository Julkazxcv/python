import cv2
import pyautogui
import time
import keyboard


def screen():
        myScreenshot1 = pyautogui.screenshot(region=(957,536,5,5))
        myScreenshot1.save(r'C:\Users\jular\OneDrive\Pulpit\projekt\triggerbot\scr1.jpg')
        time.sleep(0.05)
        myScreenshot2 = pyautogui.screenshot(region=(957,536,5,5))
        myScreenshot2.save(r'C:\Users\jular\OneDrive\Pulpit\projekt\triggerbot\scr2.jpg')
        print("screenshot zrobiony")  
        path1 = r'C:\Users\jular\OneDrive\Pulpit\projekt\triggerbot\scr1.jpg'   
        path2= r'C:\Users\jular\OneDrive\Pulpit\projekt\triggerbot\scr2.jpg'
        before = cv2.imread(path1)
        after = cv2.imread(path2)
        difference = cv2.subtract(after, before)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("nie wykryto przeciwnika")
            return True
        else:
            pyautogui.click()
            return False
            


while True:
    if keyboard.is_pressed("enter"):
        while True:
            screen()      


