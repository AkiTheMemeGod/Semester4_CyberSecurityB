from dependencies import *
import Home
from streamlit_option_menu import option_menu

st.set_page_config(layout="centered", page_title="CSE-CS Notes", page_icon="📚")


class Notes:

    def __init__(self):
        self.apps = []

    @staticmethod
    def run():
        c1, c2, c3 = st.sidebar.columns(3)
        with c1:
            side_title = '<h3 style="font-family:monospace; color:black; font-size: 50px;" align="center">SRM Notes</h3>'
            st.sidebar.markdown(side_title, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        border-radius: 50%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

            st.image("Srmseal.png")

        with st.sidebar:
            option = option_menu(
                menu_title=None,
                options=["Home", "AI", "CNS", "DAA", "DBMS", "PQT"],
                orientation="vertical",
                icons=["house-door", "robot", "key", "code-slash", "database", "percent"],
                default_index=0,
            )

        side_title = '<h1 style="font-family:monospace; color:#0C2637; font-size: 35px;" align="center">👨‍💻Made by : </h1><br>'
        st.sidebar.markdown(side_title, unsafe_allow_html=True)

        st.sidebar.link_button("Made by Akash", url="https://akashportfolio.streamlit.app/",
                               use_container_width=True)
        st.sidebar.link_button("Contact Me", url="https://akashportfolio.streamlit.app/Contact_Me",
                               use_container_width=True)

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

    run()
