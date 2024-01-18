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
    import subprocess


    def commit_and_push(commit_message, branch='master'):
        try:
            # Stage all changes
            subprocess.run(['git', 'add', '.'])

            # Commit changes
            subprocess.run(['git', 'commit', '-m', commit_message])

            # Push changes to the specified branch
            subprocess.run(['git', 'push', 'origin', branch])

            print("Changes committed and pushed successfully.")
        except Exception as e:
            print(f"Error: {e}")


    # Example usage
    commit_mesg = "Automated commit to upload files"
    commit_and_push(commit_mesg)

except Exception as e:
    print("An error occurred in uploading files", e)
