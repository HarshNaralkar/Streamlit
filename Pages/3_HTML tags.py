import streamlit as st
import pandas as pd

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