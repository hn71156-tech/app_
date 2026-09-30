from dal.db import get_conn


# ===== THÊM HÓA ĐƠN =====
def insert(tenphim, soluong, tongtien, ghe=""):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO hoadon (tenphim, soluong, tongtien, ghe, thoigian)
        VALUES (?, ?, ?, ?, GETDATE())
    """, (tenphim, soluong, tongtien, ghe))

    conn.commit()
    conn.close()


# ===== LẤY TẤT CẢ HÓA ĐƠN (FIX LỖI CHÍNH Ở ĐÂY) =====
def get_all():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, tenphim, soluong, tongtien, ghe, thoigian
        FROM hoadon
        ORDER BY thoigian DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# ===== THỐNG KÊ =====
def thong_ke():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tenphim, SUM(soluong) AS soluong, SUM(tongtien) AS tongtien
        FROM hoadon
        GROUP BY tenphim
        ORDER BY tongtien DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# ===== LẤY GHẾ ĐÃ BÁN =====
def get_ghe_daban(tenphim):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ghe FROM hoadon
        WHERE tenphim = ?
    """, (tenphim,))

    rows = cursor.fetchall()
    conn.close()

    ds = set()

    for row in rows:
        if row[0]:
            ghe_list = [g.strip() for g in row[0].split(",")]
            ds.update(ghe_list)

    return ds


# ===== TOP 3 PHIM =====
def top_phim():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TOP 3 tenphim, SUM(tongtien) AS doanhthu
        FROM hoadon
        GROUP BY tenphim
        ORDER BY doanhthu DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data


# ===== DOANH THU THEO NGÀY =====
def doanhthu_theo_ngay():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT CAST(thoigian AS DATE) AS ngay, SUM(tongtien) AS doanhthu
        FROM hoadon
        GROUP BY CAST(thoigian AS DATE)
        ORDER BY ngay
    """)

    data = cursor.fetchall()
    conn.close()

    return data
