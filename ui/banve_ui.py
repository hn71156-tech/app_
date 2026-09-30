import tkinter as tk
from tkinter import ttk, messagebox
from bus import phim_bus, hoadon_bus


class BanVeUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#181818")

        # ===== TITLE =====
        tk.Label(self, text="🎟️ BÁN VÉ XEM PHIM",
                 fg="white", bg="#181818",
                 font=("Arial", 18, "bold")).pack(pady=15)

        # ===== FORM =====
        box = tk.Frame(self, bg="#2c2c3c", padx=20, pady=20)
        box.pack(pady=10)

        tk.Label(box, text="Phim", fg="white", bg="#2c2c3c").grid(row=0, column=0)
        self.cb = ttk.Combobox(box, width=25)
        self.cb.grid(row=0, column=1, pady=5)
        self.cb.bind("<<ComboboxSelected>>", self.load_ghe)

        tk.Label(box, text="Giờ chiếu", fg="white", bg="#2c2c3c").grid(row=1, column=0)
        self.time_cb = ttk.Combobox(box, values=[
            "08:00", "10:00", "13:00", "15:00", "18:00", "21:00"
        ])
        self.time_cb.grid(row=1, column=1, pady=5)

        # ===== GHẾ =====
        tk.Label(self, text="💺 Chọn ghế",
                 fg="white", bg="#181818",
                 font=("Arial", 12, "bold")).pack(pady=5)

        self.selected_seats = set()
        self.seat_buttons = {}

        self.seat_frame = tk.Frame(self, bg="#181818")
        self.seat_frame.pack(pady=10)

        self.create_seats()

        # ===== COMBO =====
        combo_frame = tk.Frame(self, bg="#181818")
        combo_frame.pack(pady=15)

        self.popcorn = tk.IntVar()
        self.water = tk.IntVar()

        tk.Checkbutton(combo_frame, text="🍿 Bắp (+30k)",
                       variable=self.popcorn,
                       bg="#181818", fg="white",
                       selectcolor="#2ecc71").pack(anchor="w")

        tk.Checkbutton(combo_frame, text="🥤 Nước (+20k)",
                       variable=self.water,
                       bg="#181818", fg="white",
                       selectcolor="#2ecc71").pack(anchor="w")

        # ===== KẾT QUẢ =====
        self.kq = tk.Label(self, text="0 VNĐ",
                           fg="#2ecc71", bg="#181818",
                           font=("Arial", 14, "bold"))
        self.kq.pack(pady=10)

        # ===== BUTTON =====
        tk.Button(self, text="Tính tiền",
                  bg="#3498db", fg="white",
                  command=self.tinh).pack(pady=5)

        tk.Button(self, text="Thanh toán",
                  bg="#2ecc71", fg="white",
                  command=self.pay).pack(pady=5)

        self.load()

    # ===== TẠO GHẾ =====
    def create_seats(self):
        rows = ["A", "B", "C"]
        cols = range(1, 6)

        for i, r in enumerate(rows):
            for j, c in enumerate(cols):
                seat = f"{r}{c}"

                btn = tk.Button(
                    self.seat_frame,
                    text=seat,
                    width=5,
                    bg="#444",
                    fg="white",
                    command=lambda s=seat: self.toggle_seat(s)
                )

                btn.grid(row=i, column=j, padx=4, pady=4)
                self.seat_buttons[seat] = btn

    # ===== LOAD PHIM =====
    def load(self):
        data = phim_bus.get_list()
        self.ds = {}

        for p in data:
            try:
                self.ds[p.ten] = p.gia
            except:
                self.ds[p[1]] = p[3]

        self.cb["values"] = list(self.ds.keys())

    # ===== LOAD GHẾ ĐÃ BÁN =====
    def load_ghe(self, event=None):
        ten = self.cb.get()
        self.selected_seats.clear()

        ghe_daban = hoadon_bus.get_ghe_daban(ten)

        for seat, btn in self.seat_buttons.items():
            if seat in ghe_daban:
                btn.config(bg="red", state="disabled")
            else:
                btn.config(bg="#444", state="normal", text=seat)

    # ===== CHỌN GHẾ =====
    def toggle_seat(self, seat):
        btn = self.seat_buttons[seat]

        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
            btn.config(bg="#444", text=seat)
        else:
            self.selected_seats.add(seat)
            btn.config(bg="#2ecc71", text=f"✔ {seat}")

    # ===== TÍNH TIỀN =====
    def tinh(self):
        try:
            ten = self.cb.get()
            if not ten:
                raise Exception("Chưa chọn phim!")

            gia = self.ds[ten]

            # 👉 số lượng = số ghế
            sl = len(self.selected_seats)

            if sl == 0:
                raise Exception("Chưa chọn ghế!")

            tong = gia * sl

            if self.popcorn.get():
                tong += 30000
            if self.water.get():
                tong += 20000

            self.kq.config(text=f"{tong:,} VNĐ")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== THANH TOÁN =====
    def pay(self):
        try:
            ten = self.cb.get()
            if not ten:
                raise Exception("Chưa chọn phim!")

            sl = len(self.selected_seats)
            if sl == 0:
                raise Exception("Chưa chọn ghế!")

            gia = self.ds[ten]
            tong = gia * sl

            if self.popcorn.get():
                tong += 30000
            if self.water.get():
                tong += 20000

            ghe_str = ",".join(self.selected_seats)

            hoadon_bus.thanh_toan(ten, sl, gia, ghe_str)

            messagebox.showinfo(
                "Thành công",
                f"Phim: {ten}\n"
                f"Ghế: {ghe_str}\n"
                f"Tổng: {tong:,} VNĐ"
            )

            # reset
            self.selected_seats.clear()
            self.kq.config(text="0 VNĐ")

            self.load_ghe()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
