import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, master, text, cmd):
        super().__init__(master,
                         text=text,
                         command=cmd,
                         bg="#2c2c3c",
                         fg="white",
                         relief="flat",
                         width=18,
                         height=2)

        self.bind("<Enter>", lambda e: self.config(bg="#3d3d5c"))
        self.bind("<Leave>", lambda e: self.config(bg="#2c2c3c"))

class Card(tk.Frame):
    def __init__(self, master, title, value):
        super().__init__(master, bg="#2c2c3c", width=200, height=100)

        tk.Label(self, text=title,
                 fg="white", bg="#2c2c3c").pack()

        self.lbl = tk.Label(self, text=value,
                            fg="#2ecc71", bg="#2c2c3c",
                            font=("Arial", 18))
        self.lbl.pack()

    def set(self, v):
        self.lbl.config(text=v)
