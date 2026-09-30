import tkinter as tk

class GheUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.selected = set()
        self.buttons = {}

        for i in range(5):
            for j in range(5):
                seat = chr(65+i) + str(j+1)

                btn = tk.Label(
                    self,
                    text=seat,
                    width=6,
                    height=2,
                    bg="#444",
                    fg="white",
                    bd=2,
                    relief="ridge"
                )

                btn.grid(row=i, column=j, padx=4, pady=4)

                # 👇 bind click trực tiếp
                btn.bind("<Button-1>", lambda e, s=seat: self.toggle(s))

                self.buttons[seat] = btn

    def toggle(self, seat):
        btn = self.buttons[seat]

        if seat in self.selected:
            self.selected.remove(seat)

            btn.config(
                text=seat,
                bg="#444",
                relief="ridge"
            )
        else:
            self.selected.add(seat)

            btn.config(
                text="✔ " + seat,
                bg="#2ecc71",
                relief="solid"
            )

        print("Ghế:", self.selected)
