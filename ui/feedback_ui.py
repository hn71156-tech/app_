import tkinter as tk
from tkinter import ttk, messagebox
from bus import feedback_bus


class FeedbackUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        # ===== TITLE =====
        tk.Label(
            self,
            text="📩 KHIẾU NẠI / GÓP Ý",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#121212"
        ).pack(pady=15)

        # ===== FORM =====
        form = tk.Frame(self, bg="#1e1e1e", padx=20, pady=20)
        form.pack(pady=10)

        # HỌ TÊN
        tk.Label(
            form,
            text="Họ tên",
            fg="white",
            bg="#1e1e1e"
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.hoten = tk.Entry(form, width=40)
        self.hoten.grid(row=0, column=1, pady=5)

        # SỐ ĐIỆN THOẠI
        tk.Label(
            form,
            text="Số điện thoại",
            fg="white",
            bg="#1e1e1e"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.sdt = tk.Entry(form, width=40)
        self.sdt.grid(row=1, column=1, pady=5)

        # NỘI DUNG
        tk.Label(
            form,
            text="Nội dung",
            fg="white",
            bg="#1e1e1e"
        ).grid(row=2, column=0, sticky="nw", pady=5)

        self.txt = tk.Text(
            form,
            width=40,
            height=6
        )
        self.txt.grid(row=2, column=1, pady=5)

        # ===== BUTTON =====
        tk.Button(
            self,
            text="📨 Gửi khiếu nại",
            bg="#2ecc71",
            fg="white",
            width=20,
            command=self.send
        ).pack(pady=10)

        # ===== TABLE =====
        tk.Label(
            self,
            text="📜 LỊCH SỬ KHIẾU NẠI",
            font=("Arial", 14, "bold"),
            fg="orange",
            bg="#121212"
        ).pack(pady=10)

        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Tên", "SĐT", "Nội dung", "Ngày"),
            show="headings",
            height=8
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Tên", text="Họ tên")
        self.tree.heading("SĐT", text="SĐT")
        self.tree.heading("Nội dung", text="Nội dung")
        self.tree.heading("Ngày", text="Ngày gửi")

        self.tree.column("ID", width=50)
        self.tree.column("Tên", width=150)
        self.tree.column("SĐT", width=120)
        self.tree.column("Nội dung", width=350)
        self.tree.column("Ngày", width=150)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

        self.load()

    # ===== LOAD DATA =====
    def load(self):
        try:
            self.tree.delete(*self.tree.get_children())

            data = feedback_bus.get_all()

            for d in data:
                self.tree.insert("", "end", values=(
                    d[0],
                    d[1],
                    d[2],
                    d[3],
                    str(d[4])
                ))

        except:
            pass

    # ===== GỬI KHIẾU NẠI =====
    def send(self):
        try:
            hoten = self.hoten.get().strip()
            sdt = self.sdt.get().strip()
            noidung = self.txt.get("1.0", tk.END).strip()

            # validate
            if not hoten:
                raise Exception("Chưa nhập họ tên!")

            if not sdt:
                raise Exception("Chưa nhập số điện thoại!")

            if not noidung:
                raise Exception("Vui lòng nhập nội dung!")

            # lưu database
            feedback_bus.insert(
                hoten,
                sdt,
                noidung
            )

            messagebox.showinfo(
                "Thành công",
                "Đã gửi khiếu nại!"
            )

            # clear
            self.hoten.delete(0, tk.END)
            self.sdt.delete(0, tk.END)
            self.txt.delete("1.0", tk.END)

            # reload
            self.load()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))