import sqlite3
import sqlite3 as sq
import streamlit as st
import os
import random as rd
import smtplib as sm
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time


def center_title(size, color, title):
    st.markdown(f"""
                <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="center">{title}</h1>
                <br>""",
                unsafe_allow_html=True)  # , help="Subject Code and Title"


def fetch_log(filepath="upload_log.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def update_log(update, filepath="upload_log.txt"):
    with open(filepath, 'a+') as file:
        file.writelines(update + "\n")


class Database:
    def __init__(self):
        self.connection = sq.connect("sem4.db")

    def get_data(self, subject, fetch, ass):
        what = (fetch, )
        cursor = self.connection.cursor()
        if ass == "Notes":
            cursor.execute(f"SELECT * FROM {subject} WHERE name=?", what)
        else:
            cursor.execute(f"SELECT * FROM {subject} WHERE name_a=?", what)
        fetched_data = cursor.fetchone()
        try:
            return fetched_data[0], fetched_data[1], fetched_data[2], fetched_data[3]
        except TypeError:
            pass

    def notes_list(self, subject):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT name FROM {subject}")
            raw_list = cursor.fetchall()
            doc_list = [item[0] for item in raw_list if item[0] is not None]
            return doc_list
        except Exception:
            pass

    def ass_list(self, subject):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT name_a FROM {subject}")
            raw_list = cursor.fetchall()
            ass_list = [item[0] for item in raw_list if item[0] is not None]
            return ass_list
        except Exception:
            pass

    @staticmethod
    def otp_gen():
        otp = ""
        for i in range(0, 6):
            z = str(rd.randint(0, 9))
            otp += z
        return otp

    def email(self, email, name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT email FROM email_notification")
        em_list = [item[0] for item in cursor.fetchall()]
        if email not in em_list:
            data = (email, name)
            cursor.execute(f"INSERT INTO email_notification (email, name) VALUES (?,?)", data)
            self.connection.commit()
            return st.success("Now you will be notified for any new notes update")
        else:
            return st.error("Email Already Subscribed !")

    def send_mail(self, To):

        msg = MIMEMultipart()
        msg['Subject'] = 'Carry My Notes'
        msg['From'] = 'e@mail.cc'
        msg['To'] = 'e@mail.cc'
        otp = self.otp_gen()

        text = MIMEText(f"Your one-time password for CarryMyNotes.streamlit.app is : *{otp}*")
        msg.attach(text)

        s = sm.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("akis.pwdchecker@gmail.com", password="tjjqhaifdobuluhg")
        s.sendmail("akis.pwdchecker@gmail.com", To, msg.as_string())
        s.quit()
        return otp


class Subject(Database):

    def __init__(self, title, sub):
        super().__init__()
        self.title = title
        self.sub = sub

    def app(self):
        # c1, c2, c3 = st.columns
        center_title(60, "#0C2637", self.title)

        r = st.radio(label="Choose",
                     options=["Notes", "Assignments"],
                     label_visibility="hidden",
                     horizontal=True,
                     index=0)

        if r == "Notes":
            opts = self.notes_list(self.sub)
        else:
            opts = self.ass_list(self.sub)
        center_title(50, "black", f"<br>📚 {r}")
        option = st.selectbox("Select the Document : ",
                              options=opts,
                              placeholder="Choose the document from here",
                              index=0)
        try:
            name, bin_data, ass_name, assignment = self.get_data(self.sub, option, r)
            if r == "Assignments":
                name = ass_name
                bin_data = assignment

            st.markdown("###")
            st.markdown("###")
            st.markdown("###")

            st.download_button(label="Download >    |" + f":red[{name}]" + "|     < document",
                               data=bin_data,
                               file_name=f"{name}",
                               mime='application/octet-stream',
                               use_container_width=True)
        except Exception as e:
            st.error(f"{r} are currently unavailable")
            # st.write(e)
