import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from bus import hoadon_bus
import pandas as pd


class ThongKeUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        # ===== TITLE =====
        tk.Label(
            self,
            text="📊 THỐNG KÊ DOANH THU",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=15)

        # ===== TỔNG DOANH THU =====
        self.lbl_total = tk.Label(
            self,
            text="💰 Tổng doanh thu: 0 VNĐ",
            font=("Arial", 14, "bold"),
            fg="#2ecc71",
            bg="#121212"
        )
        self.lbl_total.pack(pady=5)

        # ===== TABLE =====
        table_frame = tk.Frame(self, bg="#121212")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("Phim", "Số vé", "Doanh thu"),
            show="headings",
            height=10
        )

        # heading
        self.tree.heading("Phim", text="Tên phim")
        self.tree.heading("Số vé", text="Số vé")
        self.tree.heading("Doanh thu", text="Doanh thu")

        # column
        self.tree.column("Phim", width=250)
        self.tree.column("Số vé", width=100, anchor="center")
        self.tree.column("Doanh thu", width=180, anchor="e")

        # scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

        # ===== TOP PHIM =====
        tk.Label(
            self,
            text="🔥 TOP PHIM DOANH THU",
            font=("Arial", 14, "bold"),
            fg="orange",
            bg="#121212"
        ).pack(pady=10)

        self.top_box = tk.Frame(self, bg="#121212")
        self.top_box.pack()

        # ===== BUTTON =====
        btn_frame = tk.Frame(self, bg="#121212")
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="📥 Xuất Excel",
            bg="#2ecc71",
            fg="white",
            width=15,
            command=self.export_excel
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="🔄 Reload",
            bg="#3498db",
            fg="white",
            width=15,
            command=self.load
        ).grid(row=0, column=1, padx=5)

        # load
        self.load()

    # ===== LOAD DATA =====
    def load(self):
        try:
            # clear table
            self.tree.delete(*self.tree.get_children())

            data = hoadon_bus.thong_ke()

            total = 0

            for item in data:
                ten = str(item[0])
                so_ve = int(item[1])
                doanh_thu = int(float(item[2]))

                total += doanh_thu

                self.tree.insert("", "end", values=(
                    ten,
                    so_ve,
                    f"{doanh_thu:,} VNĐ"
                ))

            # tổng doanh thu
            self.lbl_total.config(
                text=f"💰 Tổng doanh thu: {total:,} VNĐ"
            )

            # ===== TOP PHIM =====
            for w in self.top_box.winfo_children():
                w.destroy()

            top = hoadon_bus.top_phim()

            if top:
                for i, t in enumerate(top, start=1):
                    tk.Label(
                        self.top_box,
                        text=f"{i}. {t[0]} - {int(float(t[1])):,} VNĐ",
                        fg="white",
                        bg="#121212",
                        font=("Arial", 12)
                    ).pack(anchor="w", pady=2)

            else:
                tk.Label(
                    self.top_box,
                    text="Chưa có dữ liệu",
                    fg="white",
                    bg="#121212"
                ).pack()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== XUẤT EXCEL =====
    def export_excel(self):
        try:
            data = hoadon_bus.thong_ke()

            if not data:
                messagebox.showwarning(
                    "Thông báo",
                    "Không có dữ liệu để xuất!"
                )
                return

            # ===== FORMAT DATA =====
            rows = []

            for item in data:
                rows.append([
                    str(item[0]),
                    int(item[1]),
                    int(float(item[2]))
                ])

            # ===== DATAFRAME =====
            df = pd.DataFrame(
                rows,
                columns=[
                    "Tên phim",
                    "Số vé",
                    "Doanh thu"
                ]
            )

            # ===== CHỌN NƠI LƯU =====
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")],
                title="Lưu file Excel"
            )

            if not file_path:
                return

            # ===== EXPORT =====
            df.to_excel(file_path, index=False)

            messagebox.showinfo(
                "Thành công",
                "Xuất file Excel thành công!"
            )

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))