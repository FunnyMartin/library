# src/dao/loan_dao.py

from src.db.connection import get_connection

class LoanDAO:

    def find_all_active(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM loans WHERE return_date IS NULL"
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
