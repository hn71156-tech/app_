from dal import phim_dal


# ===== LẤY DANH SÁCH PHIM =====
def get_list():
    return phim_dal.get_all()


# ===== THÊM PHIM =====
def insert(id, ten, loai, gia, hinhanh):
    try:
        if not ten:
            raise Exception("Chưa nhập tên phim!")

        if not loai:
            raise Exception("Chưa nhập thể loại!")

        if gia <= 0:
            raise Exception("Giá vé phải > 0!")

        phim_dal.insert(id, ten, loai, gia, hinhanh)

    except Exception as e:
        raise Exception(str(e))


# ===== SỬA PHIM =====
def update(id, ten, loai, gia):
    try:
        if not id:
            raise Exception("Chưa chọn phim!")

        if not ten:
            raise Exception("Chưa nhập tên phim!")

        if not loai:
            raise Exception("Chưa nhập thể loại!")

        if gia <= 0:
            raise Exception("Giá vé phải > 0!")

        phim_dal.update(id, ten, loai, gia)

    except Exception as e:
        raise Exception(str(e))


# ===== XÓA PHIM =====
def delete(id):
    try:
        if not id:
            raise Exception("Chưa chọn phim!")

        phim_dal.delete(id)

    except Exception as e:
        raise Exception(str(e))