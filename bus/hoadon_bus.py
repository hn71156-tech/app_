from dal import hoadon_dal


# ===== THANH TOÁN =====
def thanh_toan(tenphim, soluong, gia, ghe=""):
    try:
        if not tenphim:
            raise Exception("Chưa chọn phim!")

        if soluong <= 0:
            raise Exception("Số lượng phải > 0!")

        tong = soluong * gia

        # lưu DB
        hoadon_dal.insert(tenphim, soluong, tong, ghe)

        return tong

    except Exception as e:
        raise Exception(f"Lỗi thanh toán: {str(e)}")


# ===== THỐNG KÊ =====
def thong_ke():
    try:
        return hoadon_dal.thong_ke()
    except:
        return []


# ===== LẤY TẤT CẢ =====
def get_all():
    try:
        return hoadon_dal.get_all()
    except:
        return []


# ===== TỔNG DOANH THU =====
def get_doanhthu():
    try:
        data = thong_ke()
        return sum(i[2] for i in data) if data else 0
    except:
        return 0


# ===== GHẾ ĐÃ BÁN =====
def get_ghe_daban(tenphim):
    try:
        return hoadon_dal.get_ghe_daban(tenphim)
    except:
        return set()


# ===== TOP PHIM =====
def top_phim():
    try:
        return hoadon_dal.top_phim()
    except:
        return []


# ===== DOANH THU THEO NGÀY =====
def doanhthu_theo_ngay():
    try:
        return hoadon_dal.doanhthu_theo_ngay()
    except:
        return []
