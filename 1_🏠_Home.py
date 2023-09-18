import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
st.set_page_config(layout="wide",page_title="Home",page_icon='🏠')

def css_loader(url):
    with open(url,"r") as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
css_loader("styles/style.css")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=["About","Projects","Contact"],
        icons=["person","code-slash","chat"],
        orientation='horizontal'
        )
if selected =="About":
    col1,col2=st.columns(2)
    with col1:
        st.write("##")
        st.subheader("I am RAVINDRA PANDEY")
        st.title("ML Engineer")
    with col2:
        st_lottie(json.load(open("assests/animation_laptop.json","r")))
    st.write("---")
    col3,col4 = st.columns(2)
    with col3:
        st.subheader("""
                    Education
                    - MCA Data Science
                        - Dev Sanskriti Vishwavidyalaya
                        - 2022 - pusuing
                    - BSC Applied Mathematics
                        - Dev Sanskriti Vishwavidyalaya
                        - 2019 - 2022
                    - 12th
                        - Inter Science College , Hazaribagh
                        - 2017 - 2019
                    - 10th
                        - St. Stephen School
                        - 2017
                     """)      
    with col4:
        st.subheader("""
                    Experiences
                    - No experience in any company but gained experience from building projects which you can check out in projects section. 
                    - lokking for oportunities .....
                     """)
        st_lottie(json.load(open("assests/animation_looking_ahead.json","r")))
        
if selected=="Projects":
    st.balloons()