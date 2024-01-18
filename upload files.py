import os
import sqlite3 as sq
import subprocess


class Upload:
    def __init__(self):
        self.connection = sq.connect("sem4.db")

    def upload_from_folder(self, table):
        cursor = self.connection.cursor()
        for i in os.listdir("upload"):
            byt = open(f"upload/{i}", "rb").read()
            data = (i, byt)
            cursor.execute(f"INSERT INTO {table} VALUES (?,?)", data)
            os.remove(f"upload/{i}")
        self.connection.commit()


subject = input("Enter the subject name (dbms/daa/cns/pqt/ai) : ")
subject = subject.lower()

try:
    u = Upload()
    u.upload_from_folder(subject)

# checking

    def commit_and_push(commit_message, branch='master'):
        try:

            subprocess.run(['git', 'add', 'sem4.db'])
            subprocess.run(['git', 'commit', '-m', commit_message])
            subprocess.run(['git', 'push', 'origin', branch])

            print("Changes committed and pushed successfully.")
        except Exception as e:
            print(f"Error: {e}")


    # Example usage
    commit_mesg = "Updated database"
    commit_and_push(commit_mesg)

except Exception as e:
    print("An error occurred in uploading files", e)
