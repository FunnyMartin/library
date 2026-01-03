# src/dao/member_dao.py

from src.db.connection import get_connection

class MemberDAO:

    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM members")
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result

    def find_by_email(self, email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM members WHERE email = %s",
            (email,)
        )
        result = cursor.fetchone()

        cursor.close()
        conn.close()
        return result

    def create(self, name, surname, email, membership_type, active):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO members (name, surname, email, membership_type, active, created_at)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """,
            (name, surname, email, membership_type, active)
        )

        conn.commit()
        cursor.close()
        conn.close()
