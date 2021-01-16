import streamlit as st
import pandas as pd
import numpy as np
import base64

from string import ascii_uppercase, digits
from random import choices

from data.create_data import create_table

def app():


    img_base = "https://www.htmlcsscolor.com/preview/128x128/{0}.png"

    colors = (''.join(choices(ascii_uppercase[:6] + digits, k=6)) for _ in range(100))

    with st.beta_container():
        for col in st.beta_columns(3):
            col.image(img_base.format(next(colors)), use_column_width=True)


    with st.beta_container():
        for col in st.beta_columns(4):
            col.image(img_base.format(next(colors)), use_column_width=True)

    # Set Background Image *local file" - heroku ?
    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        body {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

    set_png_as_page_bg('bg1.jpg')


