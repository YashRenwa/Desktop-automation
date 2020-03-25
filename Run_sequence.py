import pyautogui as pg
import os
import time
f = open("coordinates and shortcuts", 'r')
num_of_lines = 0
for line in f:
    num_of_lines += 1
f.seek(0)
for i in range(0, num_of_lines):
    x = f.readline()
    if x.find('+') != -1:
        ind = x.index('+')
        time.sleep(2)
        pg.hotkey(x[:ind], x[ind+1:len(x)-1])
    elif x[:len(x)-1].isdigit():
        try:
            time.sleep(2)
            y = f.readline()
            pg.click(int(x[:len(x)-1]), int(y[:len(y)-1]))
        except ValueError :
            pass
    elif ':' in x or "\\" in x:
        time.sleep(2)
        os.startfile(x[:len(x)-1])
    else:
        time.sleep(2)
        for i in x:
            pg.press(i)