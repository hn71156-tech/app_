from dal import feedback_dal


# ===== THÊM KHIẾU NẠI =====
def insert(hoten, sdt, noidung):

    if not hoten:
        raise Exception("Chưa nhập họ tên!")

    if not sdt:
        raise Exception("Chưa nhập số điện thoại!")

    if not noidung:
        raise Exception("Chưa nhập nội dung!")

    feedback_dal.insert(
        hoten,
        sdt,
        noidung
    )


# ===== LẤY DANH SÁCH =====
def get_all():
    return feedback_dal.get_all()