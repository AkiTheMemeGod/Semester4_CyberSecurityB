import sqlite3 as sq
import streamlit as st
import os


def center_title(size, color, title):
    st.markdown(f"""
                <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="center">{title}</h1>
                <br>""",
                unsafe_allow_html=True)


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
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM {subject}")
        raw_list = cursor.fetchall()
        doc_list = [item[0] for item in raw_list if item[0] is not None]
        return doc_list

    def ass_list(self, subject):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name_a FROM {subject}")
        raw_list = cursor.fetchall()
        ass_list = [item[0] for item in raw_list if item[0] is not None]
        return ass_list


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
        option = st.selectbox("Select the pdf you want to fetch : ",
                              options=opts, label_visibility="hidden",
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
