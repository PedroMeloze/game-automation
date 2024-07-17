# PIANO TILES
import keyboard
import pyautogui
import win32api
import win32con
from time import sleep


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1232,727, (0,0,0)):
        click(1232,727)
    if pyautogui.pixelMatchesColor(1369,727, (0,0,0)):
        click(1369,727)
    if pyautogui.pixelMatchesColor(1488,727, (0,0,0)):
        click(1488,727)
    if pyautogui.pixelMatchesColor(1618,727, (0,0,0)):
        click(1618,727)