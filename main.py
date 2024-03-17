import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/profile.jpg')

with col2:
    st.title("Pampapathi K")
    content = """Hi, I am Pampapathi K A.K.A Pampi, I am a Professional Passionated Programmer. 
    I have worked with companies from various country. 
    I have inbuilt ability to acquire ever changing new technologies in this Era."""
    #st.write(content)
    st.info(content)
    content2 = """Below is my contact details. Contact me if you have any requirement to develop any apps right from 
    Android mobile to web app applications"""
st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}")
        st.info(row['description'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}")
        st.info(row['description'])
        st.write(f"[Source Code]({row['url']})")