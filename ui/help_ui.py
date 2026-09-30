import tkinter as tk


class HelpUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        tk.Label(self,
                 text="📘 TRỢ GIÚP",
                 font=("Arial", 18, "bold"),
                 fg="white",
                 bg="#121212").pack(pady=20)

        text = """
🎟️ Hướng dẫn sử dụng:

1. Bán vé:
- Chọn phim
- Nhập số lượng
- Chọn ghế
- Chọn combo
- Nhấn thanh toán

2. Thống kê:
- Xem doanh thu
- Xem top phim

3. Lịch sử:
- Xem tất cả hóa đơn

⚠️ Lưu ý:
- Phải chọn phim trước khi thanh toán
- Số lượng phải > 0
"""

        tk.Label(self,
                 text=text,
                 justify="left",
                 fg="white",
                 bg="#121212").pack(padx=20)
