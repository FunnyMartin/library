# src/dao/copy_dao.py

from src.db.connection import get_connection

class CopyDAO:

    def find_available(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT 
                c.id,
                c.inventory_code,
                b.title
            FROM copies c
            JOIN books b ON b.id = c.book_id
            WHERE c.status = 'available'
            ORDER BY b.title
            """
        )

        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    
    def create(self, book_id, inventory_code, status, price):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO copies (book_id, inventory_code, status, price)
            VALUES (%s, %s, %s, %s)
            """,
            (book_id, inventory_code, status, price)
        )

        conn.commit()
        cursor.close()
        conn.close()
