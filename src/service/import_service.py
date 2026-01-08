# src/service/import_service.py
import csv
import json
import os

from src.dao.member_dao import MemberDAO
from src.dao.book_dao import BookDAO
from src.dao.copy_dao import CopyDAO


class ImportService:

    DATA_DIR = "data"

    def __init__(self):
        self.member_dao = MemberDAO()
        self.book_dao = BookDAO()
        self.copy_dao = CopyDAO()


    def list_files(self):
        if not os.path.exists(self.DATA_DIR):
            return []

        return [
            f for f in os.listdir(self.DATA_DIR)
            if f.endswith(".csv") or f.endswith(".json")
        ]

    def import_data(self, entity, filename):
        if entity not in ("members", "books", "copies"):
            raise Exception("Unsupported entity")

        path = os.path.join(self.DATA_DIR, filename)

        if not os.path.exists(path):
            raise Exception("File not found")

        if filename.endswith(".csv"):
            self._import_csv(entity, path)
        elif filename.endswith(".json"):
            self._import_json(entity, path)
        else:
            raise Exception("Unsupported file format")

    # ---------------- PRIVATE ----------------

    def _import_csv(self, entity, path):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames is None:
                return

            for row in reader:
                try:
                    if entity == "members":
                        if not self._valid_member(row):
                            continue

                        self.member_dao.create(
                            name=row["name"].strip(),
                            surname=row["surname"].strip(),
                            email=row["email"].strip(),
                            membership_type=row["membership_type"].strip(),
                            active=True
                        )

                    elif entity == "books":
                        if not self._valid_book(row):
                            continue

                        self.book_dao.create(
                            title=row["title"].strip(),
                            genre=row["genre"].strip(),
                            isbn=row.get("isbn"),
                            published_year=row.get("published_year")
                        )

                    elif entity == "copies":
                        if not self._valid_copy(row):
                            continue

                        self.copy_dao.create(
                            book_id=int(row["book_id"]),
                            inventory_code=row["inventory_code"].strip(),
                            status=row["status"].strip(),
                            price=float(row["price"])
                        )

                except Exception:
                    continue

    def _import_json(self, entity, path):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return

        if not isinstance(data, list):
            return

        for item in data:
            try:
                if entity == "members":
                    if not self._valid_member(item):
                        continue

                    self.member_dao.create(
                        name=item["name"].strip(),
                        surname=item["surname"].strip(),
                        email=item["email"].strip(),
                        membership_type=item["membership_type"].strip(),
                        active=True
                    )

                elif entity == "books":
                    if not self._valid_book(item):
                        continue

                    self.book_dao.create(
                        title=item["title"].strip(),
                        genre=item["genre"].strip(),
                        isbn=item.get("isbn"),
                        published_year=item.get("published_year")
                    )

                elif entity == "copies":
                    if not self._valid_copy(item):
                        continue

                    self.copy_dao.create(
                        book_id=int(item["book_id"]),
                        inventory_code=item["inventory_code"].strip(),
                        status=item["status"].strip(),
                        price=float(item["price"])
                    )


            except Exception:
                continue

    # ---------------- VALIDATORS ----------------

    def _valid_member(self, data):
        required = ["name", "surname", "email", "membership_type"]
        return all(k in data and str(data[k]).strip() for k in required)

    def _valid_book(self, data):
        required = ["title", "genre"]
        return all(k in data and str(data[k]).strip() for k in required)
    
    def _valid_copy(self, data):
        required = ["book_id", "inventory_code", "status", "price"]
        return all(k in data and str(data[k]).strip() for k in required)

