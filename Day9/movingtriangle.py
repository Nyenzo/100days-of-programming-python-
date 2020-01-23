import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=200, height=400)
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="Black")
for x in range(0, 35):
    canvas.move(1, 10, 0)
    tk.update()
    time.sleep(0.5)
for x in range(0, 14):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(0.5)
for x in range(0, 35):
    canvas.move(1, -10, 0)
    tk.update()
    time.sleep(0.5)
for x in range(0, 14):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(0.5)
canvas.pack()
tk.mainloop()
