import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/profile.jpg', width=600)

with col2:
    st.title("Pampapathi K")
    content = """Hi, I am Pampapathi K A.K.A Pampi, I am a Professional Passionated Programmer. 
    I have worked with companies from various country. 
    I have inbuilt ability to acquire ever changing new technologies in this Era."""
    #st.write(content)
    st.info(content)
