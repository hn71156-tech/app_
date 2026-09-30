import pyodbc

def get_conn():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};" # Dùng bản 17 hoặc 18 sẽ ổn định hơn
            "SERVER=DESKTOP-S3394Q7;"
            "DATABASE=CinemaDB;"
            "UID=sa;"
            "PWD=chien2k5"
        )
        return conn
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return None