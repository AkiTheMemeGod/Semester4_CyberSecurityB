from dependencies import *
import Home
from streamlit_option_menu import option_menu

st.set_page_config(layout="centered", page_title="Carry My Notes", page_icon="📚")
pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/6NwtL8l.png");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
background-color: rgba(255,255,243,0.50);
}}
</style>
"""

st.markdown(pg_bg_img, unsafe_allow_html=True)


class Notes:

    def __init__(self):
        self.apps = []

    @staticmethod
    def run():

        c1, c2, c3 = st.sidebar.columns(3)
        with c1:
            side_title = '<h3 style="font-family:monospace; color:black; font-size: 40px;" align="center">CarryMyNotes</h3><br>'
            st.sidebar.markdown(side_title, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        border-radius: 50%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

            st.image("Srmseal.png")  # Logo and the title "SRM notes"

        with st.sidebar:
            option = option_menu(
                menu_title=None,
                options=["Home", "AI", "CNS", "DAA", "DBMS", "PQT", "CCTS"],
                orientation="vertical",
                icons=["house-door", "robot", "key", "code-slash", "database", "percent", "lightbulb"],
                default_index=0,
            )

        side_title = '<h1 style="font-family:monospace; color:#0C2637; font-size: 30px;" align="center">👨‍💻Made by : </h1><br>'
        st.sidebar.markdown(side_title, unsafe_allow_html=True)

        st.sidebar.link_button("Made by Akash", url="https://akashportfolio.streamlit.app/",
                               use_container_width=True)
        st.sidebar.link_button("Contact Me", url="https://akashportfolio.streamlit.app/Contact_Me",
                               use_container_width=True)  # Made by section

        with st.sidebar:  # Follow me on section
            side_title = '<br><h1 style="font-family:monospace; color:#0C2637; font-size: 30px;" align="center">📲Follow me on : </h1><br>'
            st.sidebar.markdown(side_title, unsafe_allow_html=True)
            st.link_button("Linked-In",
                           url="https://www.linkedin.com/in/akash-k-8b2132251/",
                           use_container_width=True,
                           type="secondary",
                           help="Linked-In Profile")

            st.link_button("Twitter",
                           url="https://twitter.com/AkiTheMemeGod1",
                           use_container_width=True,
                           type="secondary",
                           help="My Twitter")
            st.link_button("GitHub",
                           url="https://github.com/AkiTheMemeGod",
                           use_container_width=True,
                           type="secondary",
                           help="My GitHub")

        if option == "Home":
            Home.app()

        if option == "AI":
            ai = Subject("21CSC206T<br>Artificial Intelligence", option)
            ai.app()

        if option == "CNS":
            cns = Subject("21CSE281T<br>Cryptography and Network Security", option)
            cns.app()

        if option == "DAA":
            daa = Subject("21CSC204J<br>Design and Analysis of Algorithms", option)
            daa.app()

        if option == "DBMS":
            dbms = Subject("21CSC205P<br>Database Management Systems", option)
            dbms.app()

        if option == "PQT":
            pqt = Subject("21MAB204T<br>Probability and Queueing Theory", option)
            pqt.app()

        if option == "CCTS":
            ccts = Subject("21PDM202L<br>Critical and Creative Thinking Skills", option)
            ccts.app()

    run()
