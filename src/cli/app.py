# src/cli/app.py

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


def choose_file(files):
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    choice = input("Select file: ")

    if not choice.isdigit():
        raise Exception("Invalid input")

    index = int(choice) - 1
    if index < 0 or index >= len(files):
        raise Exception("Invalid selection")

    return files[index]


def main():
    member_dao = MemberDAO()
    book_dao = BookDAO()
    loan_dao = LoanDAO()
    service = LibraryService()
    importer = ImportService()

    while True:
        print_menu()
        choice = input("Select option: ")

        if choice == "1":
            for m in member_dao.find_all():
                print(f"{m['id']} | {m['name']} {m['surname']} | {m['email']}")

        elif choice == "2":
            for b in book_dao.find_all():
                print(f"{b['id']} | {b['title']} | {b['genre']}")

        elif choice == "3":
            try:
                member_id = int(input("Member ID: "))
                copy_id = int(input("Copy ID: "))
                due_date = input("Due date (YYYY-MM-DD): ")
                service.borrow_book(member_id, copy_id, due_date)
                print("Book borrowed successfully")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                loan_id = int(input("Loan ID: "))
                service.return_book(loan_id)
                print("Book returned successfully")
            except Exception as e:
                print(f"Error: {e}")

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
            try:
                print("\nSelect entity:")
                print("1. Members")
                print("2. Books")

                ent = input("Choice: ")
                entity = "members" if ent == "1" else "books"

                files = importer.list_files()
                if not files:
                    raise Exception("No import files found")

                filename = choose_file(files)
                importer.import_data(entity, filename)

                print("Import completed")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == "0":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
