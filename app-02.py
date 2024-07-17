# Guitar hero
import pyautogui
import keyboard

pyautogui.PAUSE = 0.02

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1247,909,(0,152,0)):
        pyautogui.press('a')
    if pyautogui.pixelMatchesColor(1337,906,(255,0,0)): 
        pyautogui.press('s')
    if pyautogui.pixelMatchesColor(1427,909,(244,244,2)):
        pyautogui.press('j')
    if pyautogui.pixelMatchesColor(1515,909,(0,152,255)): #azul
        pyautogui.press('k')
    if pyautogui.pixelMatchesColor(1609,910,(255,101,0)): #laranja
        pyautogui.press('l')
