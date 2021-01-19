import streamlit as streamlit
import pandas as pd
from PIL import Image
import requests

from fastai import *
from fastai.vision import *

def app():

    st.title('Fastai Batik Classification')

    image = Image.open(requests.get(url, stream=True).raw)
    st.image(image, use_column_width=True)

    # get data

    path_img = Path('data/Batik300')
    st.write(path_img.ls())
    