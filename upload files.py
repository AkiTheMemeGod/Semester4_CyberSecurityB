import os
import sqlite3 as sq


class Upload:
    def __init__(self):
        self.connection = sq.connect("sem4.db")

    def upload_from_folder(self, table):
        cursor = self.connection.cursor()
        for i in os.listdir("upload"):
            byt = open(f"upload/{i}", "rb").read()
            data = (i, byt)
            cursor.execute(f"INSERT INTO {table} VALUES (?,?)", data)
        self.connection.commit()


subject = input("Enter the subject name (dbms/daa/cns/pqt/ai) : ")
subject = subject.lower()

try:
    u = Upload()
    u.upload_from_folder(subject)

except Exception as e:
    print("An error occurred in uploading files", e)
