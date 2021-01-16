######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


# create object for multipage display (import in app.py)
def app():

    ######################
    # Page Title
    ######################

    image = Image.open('lab1.jpg')

    st.image(image,use_column_width=True)
    st.write("""
    # DNA Nucleotide Count Web App

    counting the nucleotide composition of DNA - layouting in streamlit
    """)
