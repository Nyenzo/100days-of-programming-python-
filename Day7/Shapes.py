from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="",
outline="blue")
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="",
outline="black")
canvas.create_rectangle(10, 10, 50, 300)
canvas.create_oval(30, 50, 100, 250)
canvas.pack()
tk.mainloop()