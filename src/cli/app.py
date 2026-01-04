# src/cli/app.py

from src.dao.member_dao import MemberDAO
from src.dao.book_dao import BookDAO
from src.dao.loan_dao import LoanDAO
from src.service.library_service import LibraryService

def print_menu():
    print("\n=== Library Management System ===")
    print("1. List members")
    print("2. List books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Show active loans")
    print("0. Exit")

def main():
    member_dao = MemberDAO()
    book_dao = BookDAO()
    loan_dao = LoanDAO()
    service = LibraryService()

    while True:
        print_menu()
        choice = input("Select option: ")

        if choice == "1":
            members = member_dao.find_all()
            for m in members:
                print(f"{m['id']} | {m['name']} {m['surname']} | {m['email']}")

        elif choice == "2":
            books = book_dao.find_all()
            for b in books:
                print(f"{b['id']} | {b['title']} | {b['genre']}")

        elif choice == "3":
            member_id = int(input("Member ID: "))
            copy_id = int(input("Copy ID: "))
            due_date = input("Due date (YYYY-MM-DD): ")

            try:
                service.borrow_book(member_id, copy_id, due_date)
                print("Book borrowed successfully")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            loan_id = int(input("Loan ID: "))
            try:
                service.return_book(loan_id)
                print("Book returned successfully")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            loans = loan_dao.find_all_active()

            if not loans:
                print("No active loans")
                continue

            print("\nID | Member ID | Copy ID | Loan date | Due date")
            print("-----------------------------------------------")

            for l in loans:
                print(
                    f"{l['id']} | "
                    f"{l['member_id']} | "
                    f"{l['copy_id']} | "
                    f"{l['loan_date']} | "
                    f"{l['due_date']}"
                )


        elif choice == "0":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
