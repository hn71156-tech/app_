import tkinter as tk
from tkinter import messagebox
from bus import auth_bus


class LoginUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        tk.Label(self, text="LOGIN",
                 fg="white", bg="#121212",
                 font=("Arial", 20, "bold")).pack(pady=30)

        self.user = tk.Entry(self, width=30)
        self.user.pack(pady=5)

        self.pw = tk.Entry(self, show="*", width=30)
        self.pw.pack(pady=5)

        tk.Button(self, text="Login",
                  width=15,
                  command=self.login).pack(pady=15)

    # ===== LOGIN =====
    def login(self):
        try:
            username = self.user.get().strip()
            password = self.pw.get().strip()

            # kiểm tra rỗng
            if not username or not password:
                raise Exception("Vui lòng nhập đầy đủ tài khoản!")

            # gọi BUS
            role = auth_bus.login(username, password)

            # ===== PHÂN QUYỀN =====
            if role == "admin":
                from ui.dashboard import Dashboard
                self.master.switch_frame(Dashboard)

            elif role == "staff":
                from ui.banve_ui import BanVeUI
                self.master.switch_frame(BanVeUI)

            else:
                messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
