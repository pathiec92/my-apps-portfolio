import streamlit as st
import pandas
st.set_page_config(layout="wide")
st.header("Code Blue")

content = """
Welcome to <b>Code Blue</b>, where innovation meets functionality in the world of web and mobile application development!

At <b>Code Blue</b>, we specialize in crafting cutting-edge web and mobile applications that revolutionize the way
 businesses engage with their customers. With expertise in Streamlit Python for web apps and the Android framework for 
 mobile apps, we are your go-to partner for bringing your digital vision to life.

Why Choose Us?

Tailored Solutions: We understand that every business is unique. That's why we take a personalized approach to development, ensuring that each app we create is perfectly tailored to meet your specific needs and objectives.

User-Centric Design: User experience is at the heart of everything we do. Our team of designers and developers collaborate seamlessly to create intuitive, user-friendly interfaces that captivate and engage your audience.

E-commerce Expertise: Whether you're looking to launch an online store or optimize your existing e-commerce platform, we have the expertise and experience to help you succeed in the competitive world of online retail.

Utility Apps: From productivity tools to lifestyle applications, we develop versatile utility apps that simplify tasks, enhance efficiency, and enrich the lives of your users.

Quality Assurance: Our commitment to quality is unwavering. We rigorously test each app across multiple devices and platforms to ensure flawless performance and seamless functionality.

Continuous Support: Our relationship with our clients doesn't end at deployment. We provide ongoing support and maintenance to ensure that your app remains up-to-date, secure, and responsive to evolving market demands.

Whether you're a startup looking to make a splash or an established enterprise seeking to stay ahead of the curve, [Your Company Name] is your trusted partner for digital success. Let's embark on a journey of innovation together!

Get in touch with us today to discuss your project and discover how we can help you achieve your goals. Let's turn your ideas into reality!
"""

st.write(content, unsafe_allow_html=True)

st.title("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("pages/about/data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.title(f"{row['last name']} {row['first name']}")
        st.info(row['role'])
        st.image(f"pages/about/images/{row['image']}")
with col2:
    for index, row in df[4:8].iterrows():
        st.title(f"{row['last name']} {row['first name']}")
        st.info(row['role'])
        st.image(f"pages/about/images/{row['image']}")
with col3:
    for index, row in df[8:12].iterrows():
        st.title(f"{row['last name']} {row['first name']}")
        st.info(row['role'])
        st.image(f"pages/about/images/{row['image']}")


