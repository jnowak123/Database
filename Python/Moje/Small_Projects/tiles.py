import pyautogui as py
from pynput.mouse import Listener
import win32api, win32con
import time
import keyboard

class Bot:

    def __init__(self):
        self.main()

    def set_points(self): #grabs 4 points on click
        self.points = []

        def on_click(x, y, button, pressed):
            self.points.append((x, y))
            if len(self.points) >= 8: # because for some reasone the function returns values on release of a click
                return False
            
        with Listener(on_click=on_click) as listener:
            listener.join()

    def click(self, x, y):
        win32api.SetCursorPos((x,y))
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
    def main(self):
        self.set_points()
        while keyboard.is_pressed('q') == False:
            for i in range(0, 8, 2):
                if py.pixel(*self.points[i])[0] == 0:
                    self.click(*self.points[i])    

Bot()

