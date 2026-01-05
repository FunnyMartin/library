import csv
import json
import os

from src.dao.member_dao import MemberDAO
from src.dao.book_dao import BookDAO


class ImportService:

    DATA_DIR = "data"

    def __init__(self):
        self.member_dao = MemberDAO()
        self.book_dao = BookDAO()

    def list_files(self):
        if not os.path.exists(self.DATA_DIR):
            raise Exception("Data directory not found")

        return [
            f for f in os.listdir(self.DATA_DIR)
            if f.endswith(".csv") or f.endswith(".json")
        ]

    def import_data(self, entity, filename):
        path = os.path.join(self.DATA_DIR, filename)

        if filename.endswith(".csv"):
            self._import_csv(entity, path)
        elif filename.endswith(".json"):
            self._import_json(entity, path)
        else:
            raise Exception("Unsupported file format")


    def _import_csv(self, entity, path):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    if entity == "members":
                        self.member_dao.create(
                            name=row["name"],
                            surname=row["surname"],
                            email=row["email"],
                            membership_type=row["membership_type"],
                            active=True
                        )

                    elif entity == "books":
                        self.book_dao.create(
                            title=row["title"],
                            genre=row["genre"],
                            isbn=row.get("isbn"),
                            published_year=row.get("published_year")
                        )

                except Exception:
                    continue

    def _import_json(self, entity, path):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

            for item in data:
                try:
                    if entity == "members":
                        self.member_dao.create(
                            name=item["name"],
                            surname=item["surname"],
                            email=item["email"],
                            membership_type=item["membership_type"],
                            active=True
                        )

                    elif entity == "books":
                        self.book_dao.create(
                            title=item["title"],
                            genre=item["genre"],
                            isbn=item.get("isbn"),
                            published_year=item.get("published_year")
                        )

                except Exception:
                    continue
