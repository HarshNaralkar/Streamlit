import streamlit as st

st.write("# | Layout Widgets")
st.text("Layout widgets")

st.write("---")

st.write("- Columns(Tables)")
col1 , col2 = st.columns(2)

with col1:
    st.write("#### **Numbers**")
    st.text(1)
    st.text(2)
    st.text(3)
    st.text(4)
    st.text(5)

with col2:
    st.write("#### **Text**")
    st.text("One")
    st.text("Two")
    st.text("Three")
    st.text("Four")
    st.text("Five")

st.write(":orange[Code👇]")

tablecode = '''col1 , col2 = st.columns(2)

with col1:
    st.write("#### **Numbers**")
    st.text(1)
    st.text(2)
    st.text(3)
    st.text(4)
    st.text(5)

with col2:
    st.write("#### **Text**")
    st.text("One")
    st.text("Two")
    st.text("Three")
    st.text("Four")
    st.text("Five")
'''

st.code(tablecode,language="python")

st.write("---")

st.write("- Expander")

with st.expander(':green[See More]'):
    st.write("Expanded Content")

st.write(":orange[Code👇]")

expandercode = '''with st.expander(':green[See More]'):
    st.write("Expanded Content")
'''

st.code(expandercode,language="python")


st.write("---")

st.write("- Container")

with st.container():
    st.write("Container Content")

st.write("---")

st.write("## | Other Widgets")

camera_input = st.camera_input("take a Picture")

st.write(":orange[Code👇]")
camerainput = '''camera_input = st.camera_input("take a Picture")'''
st.code(camerainput,language="python")
images = st.file_uploader("Upload a File here")