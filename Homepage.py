import streamlit as st

# Set dark theme using custom CSS
dark_theme = """
<style>
body {
    background-color: #1E1E1E;
    color: #FFFFFF;
}
.sidebar {
    background-color: #333333;
}
</style>
"""

st.markdown(dark_theme, unsafe_allow_html=True)

st.set_page_config(
    page_title="My Music Webpage",
    page_icon=":musical_notes:",
    layout="wide",
)

st.title("Introduction")
st.sidebar.success("Select a page above.")

with st.container():
    st.header("Hi I am Sheldone R. Dacuya :wave:")
    st.subheader("A BSCpE Student In SURIGAO DEL NORTE STATE UNIVERSITY 🏫")

with st.container():
    st.markdown("<h1 style='text-align: right;'>Homepage</h1>", unsafe_allow_html=True)
    st.markdown("------")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Hi there welcome to my webpage please feel free to explore my webpage ")


    


 
