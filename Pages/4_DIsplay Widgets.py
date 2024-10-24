import streamlit as st
import datetime
import time 

st.write("# | Display Widgets")

st.text("There are diffrent types of display widgets")

st.write("---")

st.write("- Map")

st.map( latitude= 40.7128, longitude=-74.0060)

st.write(":orange[Code👇]")
mapcode = '''st.map( latitude= 40.7128, longitude=-74.0060)'''
st.code(mapcode,language="python")
st.write("---")

st.write("- Progress Bar")
progress=  st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

st.write(":orange[Code👇]")

progrescode= '''progress=  st.progress(0)
for i in range(100):
    time.sleep(0.1) #Time You Can Adjust as per your requirment
    progress.progress(i+1)
'''
st.code(progrescode,language="python")
st.write("---")

st.write("- Spinner")

with st.spinner('Loading.......'):
    time.sleep(5)
    st.success('Done!')

st.write(":orange[Code👇]")

spinnercode = '''with st.spinner('Loading.......'):
    time.sleep(5)
    st.success('Done!')
'''
st.code(spinnercode,language="python")
st.write("---")

st.write("- Importing Image")
img =(r'C:\Users\admin\Desktop\First Year Work\chat box\images\doremon2.png')
st.image(img,width=100)
st.write(":orange[Code👇]")

imgcode = '''img =('example.png')'''
st.code(imgcode,language="python")


st.write("---")

st.write("- Audio")


st.write("---")

st.write("- Video")

st.write("---")