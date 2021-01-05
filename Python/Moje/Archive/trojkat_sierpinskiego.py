from pyautogui import moveTo, dragTo
import time
import subprocess

def triangle(a, b, c):
    moveTo(a)
    dragTo(b)
    dragTo(c)
    dragTo(a)

def middle(x, y):
    return ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2)

def sierpinski(a, b, c, level):
    triangle(a, b, c)
    if level > 0:
        sierpinski(a, middle(a, c), middle(a, b), level -1)
        sierpinski(middle(a, b), b, middle(b, c), level -1)
        sierpinski(middle(a, c), middle(b, c), c, level -1)

def main():
    subprocess.Popen(r'C:\WINDOWS\system32\mspaint.exe')
    time.sleep(3)
    corners = [[1600, 1600], [2600, 1600], [2100, 1600 - 707.1067811865476]]
    sierpinski(corners[0], corners[1], corners[2], 6)

main()