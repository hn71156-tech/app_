from dal.db import get_conn

def login(user, pw):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role FROM nhanvien
        WHERE username=? AND password=?
    """, (user, pw))

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None
