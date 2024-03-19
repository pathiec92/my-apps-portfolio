from fpdf import FPDF
import pandas as pd
import streamlit as st
import glob
from pathlib import Path

st.header("Invoice Generation")
button = st.button("Generate Invoice")
files = glob.glob("pages/invoices/excel/*.xlsx")
width = 40
height = 8
if button:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    for file in files:
        print(file)
        df = pd.read_excel(file, sheet_name="Sheet 1")
        print(df)
        file_without_ext = Path(file).stem
        invoice_num, date = file_without_ext.split("-")
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=height, txt=f"Invoice Number: {invoice_num}", align="L", ln=1)
        pdf.cell(w=50, h=height, txt=f"Date: {date}", align="L", ln=1)
        pdf.ln(20)
        columns = df.columns
        columns = [c.replace("_", " ") for c in columns]
        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=width, h=height, txt=columns[0], border=1)
        pdf.cell(w=width, h=height, txt=columns[1], border=1)
        pdf.cell(w=width, h=height, txt=columns[2], border=1)
        pdf.cell(w=width, h=height, txt=columns[3], border=1)
        pdf.cell(w=width, h=height, txt=columns[4], border=1, ln=1)
        total = 0
        for index, row in df.iterrows():
            pdf.set_font(family="Times",  size=10)
            pdf.set_text_color(80,80,80)
            pdf.cell(w=width, h=height, txt=str(row["product_id"]), border=1)
            pdf.cell(w=width, h=height, txt=str(row["product_name"]), border=1)
            pdf.cell(w=width, h=height, txt=str(row["amount_purchased"]), border=1)
            pdf.cell(w=width, h=height, txt=str(row["price_per_unit"]), border=1)
            p = row["total_price"]
            total += p
            pdf.cell(w=width, h=height, txt=str(p), border=1, ln=1)
        pdf.cell(w=width, h=height, txt="", border=1)
        pdf.cell(w=width, h=height, txt="", border=1)
        pdf.cell(w=width, h=height, txt="", border=1)
        pdf.cell(w=width, h=height, txt="Total Amount", border=1)
        pdf.cell(w=width, h=height, txt=str(total), border=1, ln=1)

        pdf.set_font(family="Times", size=10, style="BI")
        pdf.cell(w=width, h=height, txt=f"The total Price is {total}", ln=1)


        pdf.ln(20)
    pdf.output(f"pages/invoices/pdf/all.pdf")
    st.info("Invoice generated successfully")

