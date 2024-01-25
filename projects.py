import streamlit as st
from streamlit_lottie import st_lottie
import json
def list_projects():
    st.title("projects")
    col1,col2=st.columns(2)
    with col1:
        st.markdown("""
                    E-mail : ravindra.kr.py@gmail.com
                    linkedin: 
                    """,unsafe_allow_html=True)
    with col2:
        st_lottie(json.load(open("assests/contact.json", "r")),key="animation_container")
    