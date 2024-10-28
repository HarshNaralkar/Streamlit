import streamlit as st
import time
import pandas as pd


# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 1

# Function to update the page number
def set_page(page_number):
    st.session_state.page = page_number
    st.rerun()

# Page functions
def page_1():
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

        
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Page"):
            st.write("You are already on the first page.")
    with col3:
        if st.button("Next Page"):
            set_page(2)

def page_2():
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

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Page"):
            set_page(1)
    with col3:
        if st.button("Next Page"):
            set_page(3)

def page_3():

    st.title("| HTMl tags")
    st.write("Streamlit, While Primarily a Python library, offers a unique capability to render HTML directly within your app. This flexibility is achived through the :orange[st.markdown()] function, which intreprets markdown syntax and can also render raw HTML when the :orange[unsafe_allow_html] parameter is set to :orange[True]. ")

    st.write("---")

    st.markdown("## How Streamlit Hanndles HTML")
    st.markdown("1. **Parsing:** When Streamlit encounters HTML code within a st.markdown block, it parses the HTML into a DOM like structure, similar to how a web browser would. \n2. **Rendering:** Streamlit then render this DOM structure into the app's interface. This process involves converting HTML elements into corresponding Streamlit components or directly into the underlying HTML structure of the app. \n3. **Limitations:** While Streamlit can render most of the elements, there might be limitation or differences in behavior compared to a standard web browser. Some HTML elements or attributes might not be fully supposed or might produce unexpected results. ")

    data = {
        'Elements in HTML':["1. Headings","2. Bold","3. Italic","4. Link"],
        'Markdown Code' : ["# H1 \n## H2 \n### H3 \n#### H4 \n##### H5 \n###### H6","**Bold Text**","*Italic Tex*","['Click here']('link here')"]
    }

    df= pd.DataFrame(data)
    st.dataframe(df)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Page"):
            set_page(2)
    with col3:
        if st.button("Next Page"):
            set_page(4)


def page_4():
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

    # st.write("- Importing Image")
    # img =(r'C:\Users\admin\Desktop\First Year Work\chat box\images\doremon2.png')
    # st.image(img,width=100)
    # st.write(":orange[Code👇]")

    # imgcode = '''img =('example.png')'''
    # st.code(imgcode,language="python")


    # st.write("---")

    st.write("- Audio")


    st.write("---")

    st.write("- Video")

    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Page"):
            set_page(3)
    with col3:
        if st.button("Next Page"):
            set_page(5)

def page_5():
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
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Page"):
            set_page(4)

# Display the appropriate page based on session state
if st.session_state.page == 1:
    page_1()
elif st.session_state.page == 2:
    page_2()
elif st.session_state.page == 3:
    page_3()
elif st.session_state.page == 4:
    page_4()
elif st.session_state.page == 5:
    page_5()
