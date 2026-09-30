import tkinter as tk


class ChatUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.pack(fill="both", expand=True)

        tk.Label(self,
                 text="💬 CHAT HỖ TRỢ",
                 font=("Arial", 16, "bold"),
                 fg="white",
                 bg="#121212").pack(pady=10)

        # ===== KHUNG CHAT =====
        self.chat_box = tk.Text(self,
                                height=15,
                                bg="#1e1e1e",
                                fg="white",
                                wrap="word")
        self.chat_box.pack(fill="both", padx=10, pady=10)

        self.chat_box.insert(tk.END, "Bot: Xin chào 👋 Bạn cần hỗ trợ gì?\n\n")

        # ===== INPUT =====
        bottom = tk.Frame(self, bg="#121212")
        bottom.pack(fill="x", pady=5)

        self.msg = tk.Entry(bottom)
        self.msg.pack(side="left", fill="x", expand=True, padx=5)
        self.msg.bind("<Return>", lambda e: self.send())  # Enter để gửi

        tk.Button(bottom,
                  text="Gửi",
                  bg="#2ecc71",
                  fg="white",
                  command=self.send).pack(side="right", padx=5)

    # ===== SEND =====
    def send(self):
        text = self.msg.get().strip()

        if not text:
            return

        self.chat_box.insert(tk.END, f"Bạn: {text}\n")

        reply = self.reply(text)

        self.chat_box.insert(tk.END, f"Bot: {reply}\n\n")
        self.chat_box.see(tk.END)  # auto scroll

        self.msg.delete(0, tk.END)

    # ===== BOT LOGIC =====
    def reply(self, text):
        text = text.lower()

        if any(x in text for x in ["xin chào", "hello", "hi"]):
            return "Xin chào 👋 Mình có thể giúp gì cho bạn?"

        elif any(x in text for x in ["giá", "bao nhiêu", "vé bao nhiêu"]):
            return "🎟️ Giá vé từ 50,000 - 120,000 VNĐ."

        elif any(x in text for x in ["phim", "đang chiếu", "có phim gì"]):
            return "🎬 Hiện có phim hành động, kinh dị, tình cảm."

        elif any(x in text for x in ["giờ", "suất chiếu", "mấy giờ"]):
            return "⏰ Có các suất: 08:00 - 21:00."

        elif any(x in text for x in ["ghế", "seat"]):
            return "💺 Bạn có thể chọn ghế trực tiếp khi mua vé."

        elif any(x in text for x in ["bắp", "combo", "nước"]):
            return "🍿 Có bắp (+30k) và nước (+20k)."

        elif any(x in text for x in ["thanh toán", "mua vé"]):
            return "💳 Chọn phim → nhập số lượng → bấm Thanh toán."

        elif any(x in text for x in ["địa chỉ", "ở đâu"]):
            return "📍 Rạp nằm ở trung tâm thành phố."

        elif any(x in text for x in ["hủy", "đổi vé"]):
            return "⚠️ Hiện chưa hỗ trợ hủy hoặc đổi vé."

        elif any(x in text for x in ["cảm ơn", "thanks"]):
            return "😊 Không có gì!"

        elif any(x in text for x in ["bye", "tạm biệt"]):
            return "👋 Hẹn gặp lại bạn!"

        else:
            return "🤖 Mình chưa hiểu. Bạn thử hỏi về giá vé, phim, ghế nhé!"
