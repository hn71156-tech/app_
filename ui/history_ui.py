import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from bus import hoadon_bus
import pandas as pd


class HistoryUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        # ===== TITLE =====
        tk.Label(
            self,
            text="📜 LỊCH SỬ HÓA ĐƠN",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=10)

        # ===== TABLE FRAME =====
        table_frame = tk.Frame(self, bg="#121212")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # ===== TABLE =====
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Phim", "SL", "Tiền", "Ghế", "Ngày"),
            show="headings",
            height=15
        )

        # ===== HEADING =====
        self.tree.heading("ID", text="ID")
        self.tree.heading("Phim", text="Tên phim")
        self.tree.heading("SL", text="Số lượng")
        self.tree.heading("Tiền", text="Tổng tiền")
        self.tree.heading("Ghế", text="Ghế")
        self.tree.heading("Ngày", text="Ngày")

        # ===== COLUMN =====
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Phim", width=220)
        self.tree.column("SL", width=80, anchor="center")
        self.tree.column("Tiền", width=150, anchor="e")
        self.tree.column("Ghế", width=150)
        self.tree.column("Ngày", width=180)

        # ===== SCROLLBAR =====
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

        # ===== BUTTON FRAME =====
        btn_frame = tk.Frame(self, bg="#121212")
        btn_frame.pack(pady=10)

        # ===== EXPORT EXCEL =====
        tk.Button(
            btn_frame,
            text="📥 Xuất Excel",
            bg="#2ecc71",
            fg="white",
            width=15,
            command=self.export_excel
        ).grid(row=0, column=0, padx=5)

        # ===== RELOAD =====
        tk.Button(
            btn_frame,
            text="🔄 Reload",
            bg="#3498db",
            fg="white",
            width=15,
            command=self.load
        ).grid(row=0, column=1, padx=5)

        self.load()

    # ===== LOAD DATA =====
    def load(self):

        self.tree.delete(*self.tree.get_children())

        try:
            data = hoadon_bus.get_all()

            for d in data:

                try:
                    ngay = ""

                    if d[5]:
                        ngay = d[5].strftime("%d/%m/%Y %H:%M")

                    self.tree.insert(
                        "",
                        "end",
                        values=(
                            d[0],                         # ID
                            str(d[1]),                   # Tên phim
                            int(d[2]),                   # Số lượng
                            f"{int(float(d[3])):,} VNĐ", # Tiền
                            str(d[4]),                   # Ghế
                            ngay                         # Ngày
                        )
                    )

                except:
                    self.tree.insert("", "end", values=d)

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                str(e)
            )

    # ===== XUẤT EXCEL =====
    def export_excel(self):

        try:
            data = hoadon_bus.get_all()

            if not data:
                messagebox.showwarning(
                    "Thông báo",
                    "Không có dữ liệu để xuất!"
                )
                return

            rows = []

            for d in data:

                ngay = ""

                try:
                    if d[5]:
                        ngay = d[5].strftime("%d/%m/%Y %H:%M")
                except:
                    ngay = str(d[5])

                rows.append([
                    d[0],
                    str(d[1]),
                    int(d[2]),
                    int(float(d[3])),
                    str(d[4]),
                    ngay
                ])

            # ===== DATAFRAME =====
            df = pd.DataFrame(
                rows,
                columns=[
                    "ID",
                    "Tên phim",
                    "Số lượng",
                    "Tổng tiền",
                    "Ghế",
                    "Ngày"
                ]
            )

            # ===== SAVE FILE =====
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                title="Lưu file Excel"
            )

            if not file_path:
                return

            # ===== EXPORT =====
            df.to_excel(
                file_path,
                index=False
            )

            messagebox.showinfo(
                "Thành công",
                "Xuất Excel thành công!"
            )

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                str(e)
            )