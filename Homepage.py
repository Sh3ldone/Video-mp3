import json
import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(
        page_title="My Webpage",
        page_icon=":musical_notes:",
        layout="wide",
    )

    st.title("Introduction")
    st.sidebar.success("Select a page above.")

    with st.container():
        st.header("Hi, I am Sheldone R. Dacuya :wave:")
        st.subheader("A BSCpE Student In SURIGAO DEL NORTE STATE UNIVERSITY 🏫")

    with st.container():
        st.markdown("<h1 style='text-align: right;'>Homepage</h1>", unsafe_allow_html=True)
        st.markdown("------")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""
            Good day, everyone! Thank you for visiting my page. I am Sheldone Dacuya, the creator of this website. 
            I am grateful because I have learned a lot, especially in programming. On this website, 
            I share my passion for technology, coding, and various projects that I've worked on
            Explore the different sections to find insightful articles, tutorials, and updates on the latest in the tech world.
            Whether you're a fellow programmer or someone curious about the world of coding, I hope you find valuable information and inspiration here.
            Feel free to navigate through the projects I've created, each with its unique story and purpose. 
            From programming challenges to innovative solutions, I strive to showcase the endless possibilities that coding offers
            If you have any questions, feedback, or just want to say hello, don't hesitate to reach out. 
            Your support means a lot to me, and I look forward to connecting with you on this exciting journey of exploration and learning
            """)
            st.write(" Thank you once again for being a part of this community. Happy coding! [Click here](https://www.w3schools.com/python/)")

    st.write("Lottie Animation Example:")
    
    script_dir = os.path.dirname(__file__)
    lottie_file_path = os.path.join(script_dir, "lottiefiles", "don.json")
    
    lottie_coding = load_lottie_file(lottiefiles\don.json)  # replace link to local lottie file
    lottie_hello = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        height=None,
        width=None,
        key=None,
    )

if __name__ == "__main__":
    main()




    


 
