from tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.5)
canvas.pack()
tk.mainloop()
