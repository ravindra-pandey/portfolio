import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
st.set_page_config(layout="wide",page_title="Home",page_icon='🏠')

def css_loader(url):
    with open(url,"r") as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
css_loader("styles/style.css")
def empty():
    return " "
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
        st.write("##")
        st.write("##")
        st.header("I am RAVINDRA PANDEY")
        st.title("Data Science Postgraduate")
    with col2:
        st_lottie(json.load(open("assests/animation_laptop.json","r")))
        pass
    st.write("---")
    col3,col4 = st.columns(2)
    with col3:
        st.markdown(f""" 
                    ## Education
                    ----------
                    ### MCA Data Science
                        ☼ Dev Sanskriti Vishwavidyalaya
                        ☼ 7.62 SGPA, 8.4 SGPA, 8.33 SGPA, _
                        ☼ 2022 - pusuing
                        
                    ### BSC Applied Mathematics
                        ☼ Dev Sanskriti Vishwavidyalaya
                        ☼ 7.2 CGPA
                        ☼ 2019 - 2022
                    ### 12th
                        ☼ Inter Science College , Hazaribagh
                        ☼ 51.4%
                        ☼ 2017 - 2019
                    ### 10th
                        ☼ St. Stephen School
                        ☼ 9.6 CGPA
                        ☼ 2017
                     """ ,unsafe_allow_html=True)      
    with col4:
        st.markdown("""
                    ## Work Experiences
                    -------------------
                    ### Machine Learning Mentor
                    ##### National Institute of Electronics and Information Technology, Haridwar
                        ☼ Training JNV students in Tehri Garhwal on Python and ML.
                        
                        ☼ Increased student engagement & practical knowledge: hands-on coding, 
                        interactive notebooks, project simulations (data analysis, prediction models).

                        ☼ Bridged academic-real world gap: dynamically tailored curriculum.

                        ☼ Expanding to NLP & Deep Learning modules.
                    ### Computer Vision Intern
                    ##### Center of Artificial Intelligence & Research
                        ☼ Engineered an automated Optical Character Recognition (OCR) application 
                        utilizing Python and Google Vision API to extract data from legacy student forms,
                        resulting in a 75% reduction in manual data entry time.

                        ☼ Proactively resolved a critical text extraction issue, ensuring 97% accuracy and 
                        completeness of data capture from diverse document formats.
                        """,unsafe_allow_html=True)
        
        # st_lottie(json.load(open("assests/animation_looking_ahead.json","r")))
        
if selected=="Projects":
    st.balloons()