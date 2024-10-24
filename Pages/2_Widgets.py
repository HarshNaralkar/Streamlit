import streamlit as st

st.title("| Widgets")
st.write("Streamlit gives you a so many widgets ")

st.write("- Button")

#Button
if st.button(":blue[Click me]"):
    st.write("Button is clicked!!!")

code ='''if st.button("Click me"):
    st.write("Button is clicked!!!")'''
st.write(":orange[Code👇]")
st.code(code,language="python")

st.write("---")

# =======================================================================================

st.write("- CheckBox")

agree = st.checkbox("I agree!!")

if agree:
    st.write(":green[Terms and conditions Accepted!!]")
else:
    st.write(":red[Terms and Conditions Are Not Accepted !!!]")

checkboxcode ='''agree = st.checkbox("I agree!!")
if agree:
    st.write(":green[Terms and conditions Accepted!!]")
else:
    st.write(":red[Terms and Conditions Are Not Accepted !!!]")'''

st.write(":orange[Code👇]")
st.code(checkboxcode,language="python")

# ==========================================================================

st.write("---")
st.write("- Toggle")


activated =  st.toggle("Activate")

if activated:
    st.write(":green[Toggle is Activated !!!!]")
else:
    st.write(":red[Toogle is Not Activated !!!]")

st.write(":orange[Code👇]")
togglecode = ('''activated =  st.toggle("Activate")
    if activated:
        st.write(":green[Toggle is Activated !!!!]")
    else:
        st.write(":red[Toogle is Not Activated !!!]")''')

st.code(togglecode,language="python")


# =========================================================
st.write("---")
st.write("- Radio")

choice = st.radio("Is this Website is Helpful For you ?",["Yes","No","Make Another Website"])
if (choice=="Yes"):
    st.write("Thank You for Your Respons")
elif (choice=="No"):
    st.write("Ok Thank you For Comming here don't come back!!!")
else:
    st.write("Ok i will make Another Website Soon")

st.write(":orange[Code👇]")
radiocode = '''choice = st.radio("Is this Website is Helpful For you ?",["Yes","No","Make Another Website"])
if (choice=="Yes"):
    st.write("Thank You for Your Respons")
elif (choice=="No"):
    st.write("Ok Thank you For Comming here don't come back!!!")
else:
    st.write("Ok i will make Another Website Soon")'''

st.code(radiocode,language="python")

st.write("---")
st.write("- SelectBox")
option = st.selectbox("Rate Me",["","❤❤❤❤❤","❤❤❤❤","❤❤❤","❤❤","❤"])

st.write(":orange[Code👇]")
selectboxcode= '''option = st.selectbox("Rate Me",["","❤❤❤❤❤","❤❤❤❤","❤❤❤","❤❤","❤"])'''
st.code(selectboxcode,language="python")

st.write("---")
# =======================================================================
st.write("- MultiSelect")

options = st.multiselect("Multiple Select",["","❤❤❤❤❤","❤❤❤❤","❤❤❤","❤❤","❤"])

st.write(":orange[Code👇]")
multiselectcode = '''options = st.multiselect("Multiple Select",["","❤❤❤❤❤","❤❤❤❤","❤❤❤","❤❤","❤"])
'''
st.code(multiselectcode,language="python")

st.write("---")
# ===========================================================

st.write("- Slider")
value = st.slider("Select a Value",0,100,50)
st.write(":orange[Code👇]")

slidercode = '''st.write("- Slider")
value = st.slider("Select a Value",0,100,50)'''
st.code(slidercode,language="python")

# =====================================
st.write("---")

st.write("- Select Slider")
size =  st.select_slider("pick a Size",['S','M','L'])

st.write(":orange[Code👇]")
selectslidercode = '''st.write("- Select Slider")
size =  st.select_slider("pick a Size",['S','M','L'])'''

st.code(selectslidercode,language="python")
# ===================================================

st.write("---")
st.write("- Text Input")
name = st.text_input("Name",placeholder="Enter Your Name Here")
st.write(":orange[Code👇]")
textinputcode = '''st.write("- Text Input")
name = st.text_input("Name",placeholder="Enter Your Name Here")'''

st.code(textinputcode,language="python")


st.write("---")
# ==========================================================================================
st.write("- Number Input")

numbers =  st.number_input("Question Here",placeholder="Enter Your Answer Here")
st.write(":orange[Code👇]")
numinputcode = '''numbers =  st.number_input("Question Here",placeholder="Enter Your Answer Here")''' 
st.code(numinputcode,language="python")

# ==========================================
st.write("---")
st.write("- Text  Area")

textarea= st.text_area("This is the Text Area",placeholder="Enter Your FeedBack Here")
st.write(":orange[Code👇]")
textareacode = '''textarea= st.text_area("This is the Text Area",placeholder="Enter Your FeedBack Here")'''
st.code(textareacode,language="python")

# ==================================
st.write("----")
st.write("- Date Input")
date =  st.date_input("Shedule Your Lecture")
st.write(":orange[Code👇]")
dateinputcode = '''date =  st.date_input("Shedule Your Lecture")'''
st.code(dateinputcode,language="python")

# ===========================================
st.write("---")
st.write("- Time Input")

time = st.time_input("Pick Time Here")
st.write(":orange[Code👇]")
timeinputcode ='''time = st.time_input("Pick Time Here")'''
st.code(timeinputcode,language="python")
# ===============================================================================
st.write("---")

st.write("- File Uploader")

file = st.file_uploader("Upload a File here")
st.write(":orange[Code👇]")
fileuploadcode = '''file = st.file_uploader("Upload a File here")'''
st.code(fileuploadcode,language="python")