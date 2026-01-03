# src/dao/book_dao.py

from src.db.connection import get_connection

class BookDAO:

    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result

    def find_by_title(self, title):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM books WHERE title = %s",
            (title,)
        )
        result = cursor.fetchone()

        cursor.close()
        conn.close()
        return result
