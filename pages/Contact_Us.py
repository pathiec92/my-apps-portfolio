import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='email'):
    email = st.text_input("Your Email Address")
    topic = st.selectbox(
        'Which topic you want discuss',
        ('Projects', 'Research', 'Artificial Intelligence')
    )
    raw_message = st.text_area("Your Message..")
    message = f"""\
Subject: New email from {email}

from: {email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(email, message)
        print("pressed!")
        st.info("Mail sent successfully!!")
