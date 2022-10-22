from time import sleep
import pyautogui
import keyboard

run = True

while run:
    pyautogui.leftClick()
    sleep(1)
    run = not keyboard.is_pressed("c")