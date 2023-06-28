import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(930,626,(0,152,0)):
        pyautogui.press('a')
        sleep(0.02)
    if pyautogui.pixelMatchesColor(1023,623,(255,0,0)):
        pyautogui.press('s')
        sleep(0.02)
    if pyautogui.pixelMatchesColor(1108,625,(244,244,2)):
        pyautogui.press('j')
        sleep(0.02)