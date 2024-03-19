from fpdf import FPDF
import pandas
import streamlit as st

st.header("Invoice Generation")
button = st.button("Generate Invoice")

if button:
    print("Generating Invoice")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    df = pandas.read_csv("pages/pdf/topics.csv")
    for index, row in df.iterrows():
        pdf.add_page()
        #Set header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100,100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
        #Set footer
        pdf.ln(256)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10,txt=row["Topic"], align="R")
        for i in range(row["Pages"] - 1):
            pdf.add_page()
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)
            # Set footer
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    pdf.output("invoice.pdf")
    st.info("Invoice generated successfully")

