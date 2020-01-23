from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
test_image= PhotoImage(file='c:\\house.gif')
canvas.create_image(0, 0, anchor=NW, image=test_image)
canvas.pack()
tk.mainloop()