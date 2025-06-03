"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import PyPDF2 
import re

uploaded_pdf = st.file_uploader("Choose a file")

def find_sales_price_page(uploaded_pdf):
        if uploaded_pdf is not None:
            # Can be used wherever a "file-like" object is accepted:
            pdf_read = PyPDF2.PdfReader(uploaded_pdf)
            for page in range(len(pdf_read.pages)): 
                page_text = pdf_read.pages[page].extract_text()

                if "Copyright" in page_text and page == 0: 
                     st.write("Text Found on: Copyright", page, "\n")
                     adjusted_text = page_text.replace(',', '')
                     adjusted_text_split_copyright = adjusted_text.split("Copyright")[0]
                     address_detection = re.search("^.*?(=-|[0-9][0-9][0-9][0-9])",adjusted_text_split_copyright)
                     address = address_detection.group(0)
                     st.write(address)

                if "Property Summary" in page_text: 
                     st.write("Text Found on: Property Summary Text", page, "\n")
                     adjusted_text = page_text.replace(',', '')
                     st.write( page_text )            

                if "Sold for" in page_text: 
                     st.write("Text Found on: Direct Sale Info", page, "\n")
                     adjusted_text = page_text.replace(',', '')
                     found_prices = re.findall("(Sold for\$[0-9]+)|(Sold for \$[0-9]+)",adjusted_text)
                     st.write( found_prices[0] )

find_sales_price_page(uploaded_pdf)



# if uploaded_pdf is not None:
#     # Can be used wherever a "file-like" object is accepted:
#     pdf_read = PyPDF2.PdfReader(uploaded_pdf)
#     # Extract content from PDF file
#     content = ""
#     for page in range(len(pdf_read.pages)): 
#         content = content + pdf_read.pages[page].extract_text()
#     st.write(content)



