

import csv
import os

class FileHandler:
    USER_FILE = "data/users.csv"

    @staticmethod
    def add_user(login, password):
        if not os.path.exists(FileHandler.USER_FILE):
            with open(FileHandler.USER_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["login", "password"])

        with open(FileHandler.USER_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["login"] == login:
                    return False

        with open(FileHandler.USER_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([login, password])
        return True

    @staticmethod
    def validate_user(login, password):
        if not os.path.exists(FileHandler.USER_FILE):
            return False
        with open(FileHandler.USER_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["login"] == login and row["password"] == password:
                    return True
        return False
