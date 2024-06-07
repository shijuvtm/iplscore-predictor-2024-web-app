import streamlit as st
import os
from streamlit_option_menu import option_menu

import home,login,predictor,Contact


st.set_page_config(page_title='IPL_Score_Predictor 2024',layout="centered",page_icon="image.jpg")

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='IPL_Score_Predictor 2024',
                options=['Home','Login','Predictor','Contact'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill'],
                menu_icon='apple',
                default_index=0,
                styles={
                    "container":{"padding":"5!important","background-color":"black"},
                    "icon":{"color":"white","font-size":"23px"},
                    "nav-link":{"color":"white","font-size":"20px","text-align":"left"},
                    "nav-link-selected":{"background-color":"#02ab21"},}
                            
                            
                            
             )
            
        if app=='Home':
            home.app()
        if app=='Login':
            login.app()
        if app=='Predictor':
            predictor.app() 
        if app=='Contact':
            Contact.app()
    run()

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color:#0E1117;
color: black;
text-align: center;
}

</style>
<div class="footer">
<p style='color:white'>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/shiju-a-800572273/" target="_blank">SHIJU A</a></p>
<a style='display: block; text-align: center;' href="https://github.com/Shijuprozz/iplscore-predictor-2024-web-app/" target="_blank">gitHub</a>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)