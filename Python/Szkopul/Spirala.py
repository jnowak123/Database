from pyautogui import *
import time

time.sleep(3)

mouse = [1368, 912]
move = 10
moveTo(mouse[0], mouse[1])

for a in range(30):
    dragRel(move, 0)
    move += 5
    dragRel(0, move)
    move += 5
    dragRel(-move, 0)
    move += 5
    dragRel(0, -move)
    move += 5