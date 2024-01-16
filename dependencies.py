import sqlite3 as sq
import streamlit as st


def center_title(size, color, title):
    st.markdown(f"""
                <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="center">{title}</h1>
                <br>""",
                unsafe_allow_html=True)


class Database:
    def __init__(self):
        self.connection = sq.connect("sem4.db")

    def get_data(self, subject, fetch):
        what = (fetch, )
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {subject} WHERE name=?", what)
        fetched_data = cursor.fetchone()

        return fetched_data[0], fetched_data[1]

    def doc_list(self, subject):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM {subject}")
        raw_list = cursor.fetchall()
        doc_list = [item[0] for item in raw_list]
        return doc_list


