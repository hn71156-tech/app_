import tkinter as tk
from tkinter import ttk, messagebox
from bus import phim_bus


class PhimUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#181818")
        self.pack(fill="both", expand=True)

        # ===== TITLE =====
        tk.Label(
            self,
            text="🎬 QUẢN LÝ PHIM",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#181818"
        ).pack(pady=10)

        # ===== FORM =====
        form = tk.Frame(self, bg="#2c2c3c", padx=15, pady=15)
        form.pack(pady=10)

        # ===== ID =====
        tk.Label(
            form,
            text="ID",
            fg="white",
            bg="#2c2c3c"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.id = tk.Entry(form, width=30)
        self.id.grid(row=0, column=1, pady=5)

        # ===== TÊN PHIM =====
        tk.Label(
            form,
            text="Tên phim",
            fg="white",
            bg="#2c2c3c"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.ten = tk.Entry(form, width=30)
        self.ten.grid(row=1, column=1, pady=5)

        # ===== THỂ LOẠI =====
        tk.Label(
            form,
            text="Thể loại",
            fg="white",
            bg="#2c2c3c"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.loai = tk.Entry(form, width=30)
        self.loai.grid(row=2, column=1, pady=5)

        # ===== GIÁ =====
        tk.Label(
            form,
            text="Giá vé",
            fg="white",
            bg="#2c2c3c"
        ).grid(row=3, column=0, padx=5, pady=5)

        self.gia = tk.Entry(form, width=30)
        self.gia.grid(row=3, column=1, pady=5)

        # ===== BUTTON =====
        btn_frame = tk.Frame(self, bg="#181818")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="➕ Thêm",
            bg="#2ecc71",
            fg="white",
            width=12,
            command=self.add
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="✏️ Sửa",
            bg="#f39c12",
            fg="white",
            width=12,
            command=self.update
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="❌ Xóa",
            bg="#e74c3c",
            fg="white",
            width=12,
            command=self.delete
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            btn_frame,
            text="🔄 Làm mới",
            bg="#3498db",
            fg="white",
            width=12,
            command=self.clear
        ).grid(row=0, column=3, padx=5)

        # ===== TABLE =====
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Tên", "Loại", "Giá"),
            show="headings",
            height=12
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Tên", text="Tên phim")
        self.tree.heading("Loại", text="Thể loại")
        self.tree.heading("Giá", text="Giá vé")

        self.tree.column("ID", width=80)
        self.tree.column("Tên", width=220)
        self.tree.column("Loại", width=150)
        self.tree.column("Giá", width=120)

        self.tree.pack(fill="both", expand=True)

        # CLICK ROW
        self.tree.bind("<<TreeviewSelect>>", self.select_data)

        self.load()

    # ===== LOAD DATA =====
    def load(self):
        self.tree.delete(*self.tree.get_children())

        try:
            for p in phim_bus.get_list():
                self.tree.insert("", "end", values=(
                    p[0],
                    p[1],
                    p[2],
                    f"{int(float(p[3])):,} VNĐ"
                ))

        except Exception as e:
            messagebox.showerror("Lỗi load", str(e))

    # ===== CHỌN DỮ LIỆU =====
    def select_data(self, event):
        try:
            item = self.tree.selection()[0]
            data = self.tree.item(item)["values"]

            self.clear()

            self.id.insert(0, data[0])
            self.ten.insert(0, data[1])
            self.loai.insert(0, data[2])

            gia = str(data[3]).replace("VNĐ", "").replace(",", "").strip()
            self.gia.insert(0, gia)

        except:
            pass

    # ===== THÊM =====
    def add(self):
        try:
            id_phim = self.id.get().strip()
            ten = self.ten.get().strip()
            loai = self.loai.get().strip()

            gia = int(float(self.gia.get()))

            phim_bus.insert(
                id_phim,
                ten,
                loai,
                gia,
                ""
            )

            messagebox.showinfo("OK", "Thêm phim thành công!")

            self.load()
            self.clear()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== SỬA =====
    def update(self):
        try:
            id_phim = self.id.get().strip()

            if not id_phim:
                raise Exception("Chọn phim cần sửa!")

            ten = self.ten.get().strip()
            loai = self.loai.get().strip()

            gia = int(float(self.gia.get()))

            phim_bus.update(
                id_phim,
                ten,
                loai,
                gia
            )

            messagebox.showinfo("OK", "Cập nhật phim thành công!")

            self.load()
            self.clear()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== XÓA =====
    def delete(self):
        try:
            item = self.tree.selection()[0]

            data = self.tree.item(item)["values"]
            id_phim = data[0]

            confirm = messagebox.askyesno(
                "Xác nhận",
                "Bạn có chắc muốn xóa phim này?"
            )

            if confirm:
                phim_bus.delete(id_phim)

                messagebox.showinfo("OK", "Xóa phim thành công!")

                self.load()
                self.clear()

        except:
            messagebox.showerror("Lỗi", "Vui lòng chọn phim!")

    # ===== CLEAR =====
    def clear(self):
        self.id.delete(0, tk.END)
        self.ten.delete(0, tk.END)
        self.loai.delete(0, tk.END)
        self.gia.delete(0, tk.END)