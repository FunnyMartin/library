# src/cli/app.py

from datetime import datetime

from src.dao.member_dao import MemberDAO
from src.dao.book_dao import BookDAO
from src.dao.loan_dao import LoanDAO
from src.service.library_service import LibraryService
from src.service.import_service import ImportService


def print_menu():
    print("\n=== Library Management System ===")
    print("1. List members")
    print("2. List books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Show active loans")
    print("6. Import data")
    print("0. Exit")


def read_int(prompt):
    value = input(prompt).strip()
    if not value.isdigit():
        raise Exception("Expected number")
    return int(value)


def read_date(prompt):
    value = input(prompt).strip()
    try:
        datetime.strptime(value, "%Y-%m-%d")
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
                member_id = read_int("Member ID: ")
                copy_id = read_int("Copy ID: ")
                due_date = read_date("Due date (YYYY-MM-DD): ")

                service.borrow_book(member_id, copy_id, due_date)
                print("Book borrowed successfully")

            elif choice == "4":
                loan_id = read_int("Loan ID: ")
                service.return_book(loan_id)
                print("Book returned successfully")

            elif choice == "5":
                loans = loan_dao.find_all_active()
                if not loans:
                    print("No active loans")
                else:
                    for l in loans:
                        print(
                            f"{l['id']} | {l['member_id']} | "
                            f"{l['copy_id']} | {l['loan_date']} | {l['due_date']}"
                        )

            elif choice == "6":
                print("\nSelect entity:")
                print("1. Members")
                print("2. Books")

                ent = read_int("Choice: ")
                entity = "members" if ent == 1 else "books"

                files = importer.list_files()
                if not files:
                    print("No import files found")
                    continue

                filename = choose_file(files)
                importer.import_data(entity, filename)
                print("Import completed")

            elif choice == "0":
                break

            else:
                print("Invalid option")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
