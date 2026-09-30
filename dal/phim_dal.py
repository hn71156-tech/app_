from dal.db import get_conn


# ===== LẤY DANH SÁCH =====
def get_all():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM phim")

    data = cursor.fetchall()

    conn.close()

    return data


# ===== THÊM =====
def insert(id, ten, loai, gia, hinhanh):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO phim
        VALUES (?, ?, ?, ?, ?)
    """, (id, ten, loai, gia, hinhanh))

    conn.commit()
    conn.close()


# ===== SỬA =====
def update(id, ten, loai, gia):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE phim
        SET tenphim = ?,
            theloai = ?,
            gia = ?
        WHERE id = ?
    """, (ten, loai, gia, id))

    conn.commit()
    conn.close()


# ===== XÓA =====
def delete(id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM phim
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()