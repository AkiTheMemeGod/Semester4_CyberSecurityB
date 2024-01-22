import os
import sqlite3 as sq
import subprocess
from dependencies import update_log


class Upload:
    def __init__(self):
        self.connection = sq.connect("sem4.db")

    def upload_notes(self, table):
        cursor = self.connection.cursor()
        for i in os.listdir("upload"):
            byt = open(f"upload/{i}", "rb").read()
            data = (i, byt)
            cursor.execute(f"INSERT INTO {table} (name, docs) VALUES (?,?)", data)
            update_log(f"{table.upper()} - {i}")
            os.remove(f"upload/{i}")
        self.connection.commit()

    def upload_assignments(self, table):
        cursor = self.connection.cursor()
        for i in os.listdir("upload"):
            byt = open(f"upload/{i}", "rb").read()
            data = (i, byt)
            cursor.execute(f"INSERT INTO {table} (name_a, assignment) VALUES (?,?)", data)
            update_log(f"{table.upper()} - {i}")
            os.remove(f"upload/{i}")
        self.connection.commit()


option = input("Notes or Assignment?\n1 - For Notes.\n2 - For Assignments.\nEnter the option : ")
subject = input("Enter the subject name (dbms/daa/cns/pqt/ai) : ")
subject = subject.lower()
u = Upload()
try:
    if option == "1":
        u.upload_notes(subject)
    if option == "2":
        u.upload_assignments(subject)
    else:
        exit("WRONG INPUT")

    def commit_and_push(commit_message, branch='master'):
        try:

            subprocess.run(['git', 'add', 'sem4.db upload_log.txt'])
            subprocess.run(['git', 'commit', '-m', commit_message])
            subprocess.run(['git', 'push', 'origin', branch])

            print("Changes committed and pushed successfully.")
        except Exception as e:
            print(f"Error: {e}")

    commit_mesg = f"Updated database for {subject}"
    # commit_and_push(commit_mesg)

except Exception as e:
    print("An error occurred in uploading files", e)
