# src/service/library_service.py
from src.db.connection import get_connection
from datetime import date


class LibraryService:

    def borrow_book(self, member_id, copy_id, due_date):
        if member_id <= 0 or copy_id <= 0:
            raise Exception("Invalid ID")

        if not due_date:
            raise Exception("Due date required")

        today = date.today()
        due = date.fromisoformat(due_date)

        if due < today:
            raise Exception("Due date cannot be in the past")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT status FROM copies WHERE id = %s FOR UPDATE",
                (copy_id,)
            )
            row = cursor.fetchone()

            if row is None:
                raise Exception("Copy not found")

            if row[0] != "available":
                raise Exception("Copy is not available")

            cursor.execute(
                """
                INSERT INTO loans (member_id, copy_id, loan_date, due_date, penalty_paid)
                VALUES (%s, %s, CURDATE(), %s, 0)
                """,
                (member_id, copy_id, due_date)
            )

            cursor.execute(
                "UPDATE copies SET status = 'borrowed' WHERE id = %s",
                (copy_id,)
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def return_book(self, loan_id):
        if loan_id <= 0:
            raise Exception("Invalid loan ID")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT copy_id FROM loans WHERE id = %s FOR UPDATE",
                (loan_id,)
            )
            row = cursor.fetchone()

            if row is None:
                raise Exception("Loan not found")

            copy_id = row[0]

            cursor.execute(
                "UPDATE loans SET return_date = CURDATE() WHERE id = %s",
                (loan_id,)
            )

            cursor.execute(
                "UPDATE copies SET status = 'available' WHERE id = %s",
                (copy_id,)
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def cancel_loan(self, loan_id):
        if loan_id <= 0:
            raise Exception("Invalid loan ID")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT copy_id FROM loans WHERE id = %s FOR UPDATE",
                (loan_id,)
            )
            row = cursor.fetchone()

            if row is None:
                raise Exception("Loan not found")

            copy_id = row[0]

            cursor.execute(
                "DELETE FROM loans WHERE id = %s",
                (loan_id,)
            )

            cursor.execute(
                "UPDATE copies SET status = 'available' WHERE id = %s",
                (copy_id,)
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()
