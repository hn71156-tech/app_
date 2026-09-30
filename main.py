import tkinter as tk
from ui.login import LoginUI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinema App")
        self.geometry("1000x600")
        self.configure(bg="#121212")

        self.current = None
        self.switch_frame(LoginUI)

    def switch_frame(self, frame):
        if self.current:
            self.current.destroy()
        self.current = frame(self)
        self.current.pack(fill="both", expand=True)

app = App()
app.mainloop()
