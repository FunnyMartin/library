# src/dao/report_dao.py

from src.db.connection import get_connection

class ReportDAO:

    def book_statistics(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM vw_book_stat"
        )
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result
