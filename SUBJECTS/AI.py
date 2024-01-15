from dependencies import *


def app():

    center_title(60, "red", "21CSC206T<br>Artificial Intelligence")
    # st.title(":red[21CSC206T] - Artificial Intelligence")
    data = Database()

    st.header("Notes 👇")
    option = st.selectbox("Select the pdf you want to fetch : ",
                          options=data.doc_list("ai"), label_visibility="hidden",
                          placeholder="Choose the document from here",
                          index=0)

    name, bin_data = data.get_data("ai", option)
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")

    clicked = st.download_button(label="Download >    |" + f":red[{name}]" + "|     < document",
                                 data=bin_data,
                                 file_name=f"{name}.pdf",
                                 mime='application/octet-stream',
                                 use_container_width=True)

