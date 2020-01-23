from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
def random_triangle(base, height, hyp):
    x1 = random.randrange(base)
    y1 = random.randrange(height)
    z1 = random.randrange(hyp)
    x2 = random.randrange(base)
    y2 = random.randrange(height)
    z2 = random.randrange(hyp)
    canvas.create_polygon(x1, y1, z1, x2, y2 ,z2, fill="", outline="black")
    for x in range(0, 60):
        random_triangle(300, 300, 300)    
canvas.pack()
tk.mainloop()