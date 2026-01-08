# src/dao/loan_dao.py

from src.db.connection import get_connection

class LoanDAO:

    def find_all_active(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT 
                l.id AS loan_id,
                m.name,
                m.surname,
                b.title,
                c.inventory_code,
                l.loan_date,
                l.due_date
            FROM loans l
            JOIN members m ON m.id = l.member_id
            JOIN copies c ON c.id = l.copy_id
            JOIN books b ON b.id = c.book_id
            WHERE l.return_date IS NULL
            ORDER BY l.due_date
            """
        )

        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def create_loan(self, member_id, copy_id, due_date):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO loans (member_id, copy_id, loan_date, due_date, penalty_paid)
            VALUES (%s, %s, CURDATE(), %s, 0)
            """,
            (member_id, copy_id, due_date)
        )

        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, loan_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM loans WHERE id = %s",
            (loan_id,)
        )

        conn.commit()
        cursor.close()
        conn.close()
