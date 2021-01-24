import streamlit as streamlit
import pandas as pd
from PIL import Image
import requests
import os

from fastai import *
from fastai.vision import *

def app():

    st.title('Fastai Batik Classification')
    st.markdown("""
    This app performs Image Recognition on pretrained fastai-CNN
    * **Python libraries:** fastai.vision, pandas, requests
    """)
    image = Image.open(requests.get(url, stream=True).raw)
    st.image(image, use_column_width=True)

    # get data
    path_img = Path('data/Batik300')
    st.write(os.listdir(path_img)

    #batch size
    bs = 64
    file_names = get_image_files(path_img)
    
    ## Load Data // get classes from file names (regex), size images to 224, 
    data = ImageDataBunch.from_name_re(path_img, file_names, r'/([^/]+)_d+.jpg$', ds_tfms = get_transforms(), size = 224, bs=bs)
    data.normalize(imagenet_stats)

    st.image(data.show_batch(row=3, figsize=(7,6)))

    ## create learner

    learn = create_cnn(data, models.resnet34, metrics=error_rate)
    learn.fit_one_cycle(4)
    learn.save('resnet34-stage-1')
 
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_top_losses(9, figsize=(15,11))
    interp.plot_confusion_matrix(figsize=(12,12), dpi=60)

    ## Unfreeze, fine-tune and adjust learning-rates

    learn.unfreeze()
    learn.fit_one_cycle(2)
    learn.load('resnet34-stage-1')
    learn.lr_find()
    learn.recorder.plot()
    learn.unfreeze()
    learn.fit_one_cycle(8, max_lr=slice(1e-5, 6e-3))
    learn.save('resnet34-stage-2') 