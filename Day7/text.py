from tkinter import*
tk = Tk()
tk.geometry('300x300')
canvas = Canvas(tk, width=400, height=400)
canvas.create_text(150, 200, text='Atleast its running',
font=('Helvetica', 20))
canvas.pack()
tk.mainloop()