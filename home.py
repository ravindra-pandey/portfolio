import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import projects

st.set_page_config(layout="wide", page_title="Ravindra", page_icon="🏡")


def css_loader(url):
    with open(url, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


javascript = """
<script type="text/javascript">
document.getElementById('linkedin-animation').onclick = function() {
    window.open('https://www.linkedin.com/in/ravindra-pandey-989a75195', '_blank');
};
</script>
"""

css_loader("styles/style.css")
st.title("#")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects"],
        icons=["person", "code-slash"],
        orientation="horizontal",
    )
if selected == "About":
    col1, col2 = st.columns(2)
    with col1:
    # Code to initiate download will run when button is clicked

        st.write("##")
        st.markdown(
            f"""
                    # I am <span style='color: #ef2929;font-family:cursive;font-weight:1500;font-style: bold;'>RAVINDRA PANDEY</span> 
                    ## <span style="color:#f2bebe;">Data Science Postgraduate</span>
                    ##### <span style="color:#f2bebe;">From raw data to real solutions: Your trusted data science partner.</span> 
                    #### Find Me here:
                    <div style="text-decoration:none">ravindra.kr.py@gmail.com</div>
                    <div class="contact_container">
                    <div class="lottie-container">
                    <a href="https://www.linkedin.com/in/ravindra-pandey-989a75195">
                        <button class="lottie-button"></button>
                        <iframe class="lottie-iframe" src="https://lottie.host/embed/2cab57e3-dcf2-4db2-93ec-e46f198ab45c/KeNYZUdMti.json"></iframe>
                    </a>
                    </div>
                    <div class="lottie-container">
                    <a href="https://www.github.com/ravindra-pandey">
                        <button class="lottie-button"></button>
                        <iframe class="lottie-iframe" src="https://lottie.host/embed/e91f663b-67a3-4135-ab98-b0218738f50d/FJHs1stK9R.json"></iframe>
                    </a>
                    </div>
                    </div>
                    
                    """,
            unsafe_allow_html=True,
        )

        with open("assests/ravindra_pandey_resume.pdf", "rb") as f:
            resume = f.read()
        downloaded = st.download_button(
            label="My Resume ",
            data=resume,  # Use pdf_data if available, otherwise read directly from file
            file_name="ravindra_resume.pdf",  # Adjust filename as needed
            mime="application/pdf",
        )
        if downloaded:
            st.balloons()
    with col2:
        st_lottie(
            json.load(open("assests/data_scientist.json", "r")),
            key="animation_container",
        )

    col3, col4 = st.columns(2)
    with col3:
        st.write("##")
        st.markdown("""# <span style="color:#ef2929">Education</span>""", unsafe_allow_html=True)
    with col4:
        st.markdown(
            
            """<iframe src="https://lottie.host/embed/b8e84b33-db28-40f8-912d-7d37b9357a3a/YNFoBS5CQX.json" style="width:6vw;hieght:6vw;float:right"></iframe>""",
            unsafe_allow_html=True,
        )
    st.write("---")
    col5, col6 = st.columns(2)
    with col5:
        st.markdown(
            f""" 
                    ### <span style="color:#f2bebe">MCA Data Science</span>
                        ☼ Dev Sanskriti Vishwavidyalaya
                        ☼ 7.62 SGPA, 8.4 SGPA, 8.33 SGPA, _
                        ☼ 2022 - pusuing
                        
                    ### <span style="color:#f2bebe">BSC Applied Mathematics</span>
                        ☼ Dev Sanskriti Vishwavidyalaya
                        ☼ 7.2 CGPA
                        ☼ 2019 - 2022
            """,
            unsafe_allow_html=True,
        )
    with col6:
        st.markdown(
            f""" 
                    ### <span style="color:#f2bebe">12th</span>
                        ☼ Inter Science College , Hazaribagh
                        ☼ 51.4%
                        ☼ 2017 - 2019
                    ### <span style="color:#f2bebe">10th</span>
                        ☼ St. Stephen School
                        ☼ 9.6 CGPA
                        ☼ 2017
                     """,
            unsafe_allow_html=True,
        )
    col7, col8 = st.columns(2)
    with col7:
        st.write("##")
        st.write("##")
        st.markdown(
            """
            ## <span style="color:#ef2929;">Work Experiences</span>
        """,unsafe_allow_html=True
        )
    with col8:
        st.markdown(
            """<iframe src="https://lottie.host/embed/85eaad1e-f322-43b5-b62f-059773c66219/w4LZWqelTf.json" style="float:right;"></iframe>""",
            unsafe_allow_html=True,
        )
    st.write("----")
    st.markdown(
        """
        ### <span style="color:#f2bebe">Machine Learning Mentor</span>  
        ##### <div class="container"><div>National Institute of Electronics and Information Technology, Haridwar</div> <div><span style="color:#f2bebe">Jan 2024-Ongoing</span><div></div>
            ☼ Training JNV students in Tehri Garhwal on Python and ML.
            
            ☼ Increased student engagement & practical knowledge: hands-on coding, 
            interactive notebooks, project simulations (data analysis, prediction models).

            ☼ Bridged academic-real world gap: dynamically tailored curriculum.

            ☼ Expanding to NLP & Deep Learning modules.
        ### <span style="color:#f2bebe">Computer Vision Intern</span> 
        ##### <div class="container"><div>Center of Artificial Intelligence & Research</div> <div><span style="color:#f2bebe">May-Aug 2023</span><div></div>
            ☼ Engineered an automated Optical Character Recognition (OCR) application 
            utilizing Python and Google Vision API to extract data from legacy student forms,
            resulting in a 75% reduction in manual data entry time.

            ☼ Proactively resolved a critical text extraction issue, ensuring 97% accuracy and 
            completeness of data capture from diverse document formats.
            """,
        unsafe_allow_html=True,
    )

if selected == "Projects":
    projects.list_projects()

st.components.v1.html(javascript, height=0, width=0)
