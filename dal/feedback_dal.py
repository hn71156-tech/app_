from dal.db import get_conn


# ===== THÊM KHIẾU NẠI =====
def insert(hoten, sdt, noidung):

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO khieunai(hoten, sdt, noidung)
        VALUES (?, ?, ?)
        """,
        (hoten, sdt, noidung)
    )

    conn.commit()
    conn.close()


# ===== LẤY DANH SÁCH =====
def get_all():

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, hoten, sdt, noidung, thoigian
        FROM khieunai
        ORDER BY thoigian DESC
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data