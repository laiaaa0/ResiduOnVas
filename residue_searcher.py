import csv
import os
import requests
from translator import EnglishTranslator, CatalanTranslator


class ResidueSearcher:
    def __init__(self):
        self.database_name = "database.csv"
        self.download_if_not_exist()
        self.db = self.read_db()
        self.translator = CatalanTranslator()

    def download_if_not_exist(self):
        url = r"https://analisi.transparenciacatalunya.cat/api/views/2w5u-e2nn/rows.csv?accessType=DOWNLOAD"

        if os.path.exists(self.database_name):
            print("File already exists / not redownloading")
            return

        r = requests.get(url, allow_redirects=True)
        if r.status_code != 200:
            raise Exception("Could not get URL")

        open(self.database_name, "wb").write(r.content)

    def read_db(self):
        db = {}
        with open(self.database_name, newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            for row in csvreader:
                if len(row) > 2:
                    if "_" in row[1] or "_" in row[2]:
                        continue

                    db[row[1].lower()] = row[2]
                else:
                    print(f"Invalid row {row}")
                    break
        return db

    def closest_key(self, value):
        print("Finding closest key....")
        # return any match first
        if value in self.db.keys():
            return value

        message_in_catalan = self.translator.translate(value)
        print(f"Translating {value} to catalan: {message_in_catalan}")
        if message_in_catalan in self.db.keys():
            print(f"Found key {message_in_catalan}!")
            return message_in_catalan

        if len(value) > 3:
            # return all that start with
            all_start_with = [x for x in self.db.keys() if x.startswith(value)]
            if len(all_start_with):
                return min(all_start_with, key=len)

            all_contains_text = [x for x in self.db.keys() if value in x]
            if len(all_contains_text):
                return min(all_contains_text, key=len)

        raise Exception(f"Could not find {value}")

    def search(self, name):
        key_to_use = self.closest_key(name.lower())
        return key_to_use, self.db[key_to_use]
