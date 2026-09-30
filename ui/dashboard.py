import tkinter as tk
from bus import hoadon_bus, phim_bus


class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#181818")
        self.pack(fill="both", expand=True)

        # ===== SIDEBAR =====
        sidebar = tk.Frame(self, bg="#2c2c3c", width=220)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar,
                 text="🎬 CINEMA APP",
                 fg="white",
                 bg="#2c2c3c",
                 font=("Arial", 14, "bold")).pack(pady=15)

        # ===== MENU =====
        self.create_btn(sidebar, "🏠 Trang chủ", self.home)
        self.create_btn(sidebar, "🎟️ Bán vé", self.open_banve)
        self.create_btn(sidebar, "📊 Thống kê", self.open_tk)
        self.create_btn(sidebar, "🎬 Quản lý phim", self.open_phim)
        self.create_btn(sidebar, "📜 Lịch sử hóa đơn", self.open_hd)
        self.create_btn(sidebar, "💬 Chat hỗ trợ", self.open_chat)
        self.create_btn(sidebar, "📘 Trợ giúp", self.open_help)
        self.create_btn(sidebar, "📩 Khiếu nại", self.open_feedback)

        # ===== CONTENT =====
        self.content = tk.Frame(self, bg="#181818")
        self.content.pack(side="right", fill="both", expand=True)

        self.home()

    # ===== STYLE BUTTON =====
    def create_btn(self, parent, text, command):
        tk.Button(parent,
                  text=text,
                  command=command,
                  bg="#34495e",
                  fg="white",
                  activebackground="#2ecc71",
                  relief="flat",
                  height=2).pack(fill="x", pady=3, padx=5)

    # ===== LOAD UI =====
    def load(self, FrameClass):
        for widget in self.content.winfo_children():
            widget.destroy()

        frame = FrameClass(self.content)
        frame.pack(fill="both", expand=True)

    # ===== HOME =====
    def home(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(self.content,
                 text="🏠 DASHBOARD",
                 fg="white",
                 bg="#181818",
                 font=("Arial", 20, "bold")).pack(pady=20)

        try:
            total_phim = len(phim_bus.get_list())
        except:
            total_phim = 0

        try:
            doanh_thu = hoadon_bus.get_doanhthu()
        except:
            doanh_thu = 0

        tk.Label(self.content,
                 text=f"🎬 Tổng phim: {total_phim}",
                 fg="white",
                 bg="#181818",
                 font=("Arial", 14)).pack(pady=10)

        tk.Label(self.content,
                 text=f"💰 Doanh thu: {doanh_thu:,} VNĐ",
                 fg="#2ecc71",
                 bg="#181818",
                 font=("Arial", 14, "bold")).pack(pady=10)

    # ===== NAVIGATION =====
    def open_banve(self):
        from ui.banve_ui import BanVeUI
        self.load(BanVeUI)

    def open_tk(self):
        from ui.thongke_ui import ThongKeUI
        self.load(ThongKeUI)

    def open_phim(self):
        from ui.phim_ui import PhimUI
        self.load(PhimUI)

    def open_hd(self):
        from ui.history_ui import HistoryUI
        self.load(HistoryUI)

    def open_chat(self):
        from ui.chat_ui import ChatUI
        self.load(ChatUI)

    def open_help(self):
        from ui.help_ui import HelpUI
        self.load(HelpUI)

    def open_feedback(self):
        from ui.feedback_ui import FeedbackUI
        self.load(FeedbackUI)
