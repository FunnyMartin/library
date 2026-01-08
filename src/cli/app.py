# src/cli/app.py

from datetime import date, datetime

from src.dao.member_dao import MemberDAO
from src.dao.book_dao import BookDAO
from src.dao.loan_dao import LoanDAO
from src.service.library_service import LibraryService
from src.service.import_service import ImportService
from src.dao.report_dao import ReportDAO
from src.dao.copy_dao import CopyDAO


def print_menu():
    print("\n=== Library Management System ===")
    print("1. List members")
    print("2. List books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Show active loans")
    print("6. Import data")
    print("7. Cancel loan (delete)")
    print("8. Show book statistics report")
    print("0. Exit")



def read_int(prompt):
    value = input(prompt).strip()
    if not value.isdigit():
        raise Exception("Expected number")
    return int(value)


def read_date(prompt):
    value = input(prompt).strip()
    try:
        due = datetime.strptime(value, "%Y-%m-%d").date()
        today = date.today()

        if due < today:
            raise Exception("Date cannot be in the past")

        return value

    except ValueError:
        raise Exception("Invalid date format, expected YYYY-MM-DD")


def choose_file(files):
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    idx = read_int("Select file: ") - 1
    if idx < 0 or idx >= len(files):
        raise Exception("Invalid selection")

    return files[idx]


def main():
    member_dao = MemberDAO()
    book_dao = BookDAO()
    loan_dao = LoanDAO()
    service = LibraryService()
    importer = ImportService()
    report_dao = ReportDAO()
    copy_dao = CopyDAO()

    while True:
        try:
            print_menu()
            choice = input("Select option: ").strip()

            if choice == "1":
                for m in member_dao.find_all():
                    print(f"{m['id']} | {m['name']} {m['surname']} | {m['email']}")

            elif choice == "2":
                for b in book_dao.find_all():
                    print(f"{b['id']} | {b['title']} | {b['genre']}")

            elif choice == "3":
                print("\nAvailable members:")
                for m in member_dao.find_all():
                    print(f"{m['id']} | {m['name']} {m['surname']}")

                member_id = read_int("Select Member ID: ")

                print("\nAvailable copies:")
                copies = copy_dao.find_available()
                if not copies:
                    print("No available copies")
                    continue

                for c in copies:
                    print(f"{c['id']} | {c['title']} | {c['inventory_code']}")

                copy_id = read_int("Select Copy ID: ")
                due_date = read_date("Due date (YYYY-MM-DD): ")

                service.borrow_book(member_id, copy_id, due_date)
                print("Book borrowed successfully")


            elif choice == "4":
                print("\nActive loans:")
                loans = loan_dao.find_all_active()
                if not loans:
                    print("No active loans")
                    continue

                for l in loans:
                    print(
                        f"{l['loan_id']} | {l['name']} {l['surname']} | "
                        f"{l['title']} | due: {l['due_date']}"
                    )

                loan_id = read_int("Select Loan ID to return: ")
                service.return_book(loan_id)
                print("Book returned successfully")

            elif choice == "5":
                loans = loan_dao.find_all_active()

                if not loans:
                    print("No active loans")
                else:
                    print("\nActive loans:")
                    for l in loans:
                        print(
                            f"Loan ID: {l['loan_id']} | "
                            f"{l['name']} {l['surname']} | "
                            f"Book: {l['title']} | "
                            f"Copy: {l['inventory_code']} | "
                            f"From: {l['loan_date']} | "
                            f"Due: {l['due_date']}"
                        )


            elif choice == "6":
                print("\nSelect entity:")
                print("1. Members")
                print("2. Books")
                print("3. Copies")

                ent = read_int("Choice: ")

                if ent == 1:
                    entity = "members"
                elif ent == 2:
                    entity = "books"
                elif ent == 3:
                    entity = "copies"
                else:
                    raise Exception("Invalid choice")

                files = importer.list_files()
                if not files:
                    print("No import files found")
                    continue

                filename = choose_file(files)
                importer.import_data(entity, filename)
                print("Import completed")


            elif choice == "7":
                print("\nActive loans:")
                loans = loan_dao.find_all_active()
                if not loans:
                    print("No active loans")
                    continue

                for l in loans:
                    print(
                        f"{l['loan_id']} | {l['name']} {l['surname']} | "
                        f"{l['title']} | due: {l['due_date']}"
                    )

                loan_id = read_int("Select Loan ID to cancel: ")
                service.cancel_loan(loan_id)
                print("Loan cancelled successfully")

            
            elif choice == "8":
                stats = report_dao.book_statistics()
                if not stats:
                    print("No statistics available")
                else:
                    for row in stats:
                        print(f"{row['title']} | total loans: {row['amount_of_loans']}")


            elif choice == "0":
                break

            else:
                print("Invalid option")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
