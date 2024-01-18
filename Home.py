from dependencies import *


def app():

    center_title(60, "#0C2637", "Notes for CSE-Cybersecurity <br>Batch 2022-2026")

    center_title(30, "blacka", "This page is made for downloading the notes for the 4th Semester for the following subjects <br>")
    subs = ["All notes for PQT", "Unit 1 for dbms","All notes for PQT", "Unit 1 for dbms","All notes for PQT", "Unit 1 for dbms"]
    st.header(":red[Recently Added notes]👇")
    with st.container(height=200, border=False):

        for i in subs:
            st.success(i, icon="✅")
