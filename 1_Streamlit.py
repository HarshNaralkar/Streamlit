import streamlit as st
import json
import requests
# from streamlit_lottie import st_lottie
import time

st.markdown("# Streamlit Library")

st.text("Streamlit is an Open-Source Python framework for data scientists and AI/ML \nengineers to deliver dynamic data apps with only a few lines of code. Build \nand Deploy powerful data apps in minutes. Let's get started! ")

st.markdown("## **How to download or install streamlit in system ?**")
st.text("Open CMD on your system and write this command")
pipcode = "pip install streamlit"
st.code(pipcode,language="python")
st.markdown("---")
st.markdown("**Import Statement**")
importcode ="import streamlit as st"
st.code(importcode,language="Python")
st.markdown("---")

st.markdown("### How to write program ?")

firstprogram = '''import streamlit as st
st.text("This is First Program of Streamlit")'''
st.code(firstprogram,language="python")
st.write("---")

st.markdown("### How to run the program ?")
st.write("Step 1: Compile your program")
st.write("Step 2: open Cmd ")
st.write("Step 3: Write this statement on your command line")

runcommand = '''streamlit run filename.py'''
st.code(runcommand,language="python")

st.markdown("**Note :** while using this command crosscheck that you python file present in same directory")
st.write("---")

button_style = """<style>
                        .stButton > button { 
                                background-color: #4caf50;}
                        .stButton > button:hover{
                        background-color: #f0f0f0;
                        color: #4caf50;
                        cursor: pointer;}
                    </style>"""

st.markdown(button_style,unsafe_allow_html=True)

col1, col2, col3 =  st.columns(3)
with col1:
    if st.button("Previous Page"):
        st.write("Previous Button Clicked!!!")
with col3:
    if st.button("Next Page"):
        st.write("Next Button Clicked!!!")
