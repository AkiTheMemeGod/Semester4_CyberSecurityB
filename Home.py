from dependencies import *


def app():
    updates = ["All notes for PQT"]
    center_title(60, "#0C2637", "Notes for CSE-Cybersecurity <br>Batch 2022-2026")

    center_title(30, "black", "This page is made for downloading the notes for the 4th Semester for the following subjects <br>")

    st.header(":red[Recently Added notes]👇")
    st.markdown("###")
    with st.container(height=250, border=False):

        for i in updates:
            st.success(i, icon="✅")
