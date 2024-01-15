from dependencies import center_title, st
from SUBJECTS import Home, AI, CNS, DAA, DBMS, PQT
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")


class Notes:

    @staticmethod
    def run():
        c1, c2, c3 = st.sidebar.columns(3)
        with c2:
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        width: 100%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

            st.image("Srmseal.png", width=50)
            st.markdown("###")
            st.markdown("###")
        with st.sidebar:
            option = option_menu(
                menu_title=None,
                options=["Home", "AI", "CNS", "DAA", "DBMS", "PQT"],
                orientation="vertical",
                default_index=0,
            )

        if option == "Home":
            Home.app()

        if option == "AI":
            AI.app()

        if option == "CNS":
            CNS.app()

        if option == "DAA":
            DAA.app()

        if option == "DBMS":
            DBMS.app()

        if option == "PQT":
            PQT.app()
        # st.session_state
    run()
