import tkinter as tk

class Yasss(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Click if you're a programmer"
        self.hi_there["command"] = self.sayhey
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def sayhey(self):
        print("You is clowning!! "*100)

root = tk.Tk()
app = Yasss(master=root)
app.mainloop()