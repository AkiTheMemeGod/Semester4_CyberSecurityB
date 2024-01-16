from dependencies import *


def app():
    center_title(60, "#0C2637", "21CSE281T<br>Cryptography and Network Security")
    # st.title(":red[21CSC205P] - Database Management Systems")
    data = Database()

    st.header("Notes 👇")
    option = st.selectbox("Select the pdf you want to fetch : ",
                          options=data.doc_list("cns"), label_visibility="hidden",
                          placeholder="Choose the document from here",
                          index=0)

    name, bin_data = data.get_data("cns", option)
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")

    clicked = st.download_button(label="Download >    |" + f":red[{name}]" + "|     < document",
                                 data=bin_data,
                                 file_name=f"{name}.pdf",
                                 mime='application/octet-stream',
                                 use_container_width=True)