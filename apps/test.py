import streamlit as st
import numpy as np

## Animation test
import time
import yfinance as yf

## Beta Container and Background Image
import base64
from string import ascii_uppercase, digits
from random import choices

## Bootstrap Components
import streamlit.components.v1 as components

## Data Stats
from data.create_data import create_table


def app():

    ###########################################################
    ## Testing streamlits beta_container and Background Image
    ###########################################################
    st.title('Testing streamlits beta_container and Background Image')
    img_base = "https://www.htmlcsscolor.com/preview/128x128/{0}.png"
    text = ['Webscraping', 'EDA', 'Visualization', 'Machine Learning', 'Layouting', 'Design', 'Data Crunching']
    colors = (''.join(choices(ascii_uppercase[:6] + digits, k=6)) for _ in range(100))

    with st.beta_container():
        count = 0
        for col in st.beta_columns(3):
            col.image(img_base.format(next(colors)), use_column_width=True)
            col.write(text[count])
            count += 1
    with st.beta_container():
        count = 3
        for col in st.beta_columns(4):
            col.image(img_base.format(next(colors)), use_column_width=True)

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

    set_png_as_page_bg('assets/bg1.jpg')

    ###########################################################
    ## Testing Bootstraps Elements
    ###########################################################
    st.title('bootstrap 4 collapse example')
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div id="accordion">
        <div class="card">
            <div class="card-header" id="headingOne">
            <h5 class="mb-0">
                <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                Collapsible Group Item #1
                </button>
            </h5>
            </div>
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #1 content
            </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header" id="headingTwo">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                Collapsible Group Item #2
                </button>
            </h5>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #2 content
            </div>
            </div>
        </div>
        </div>
        """,
        height=600,
    )

    ###########################################################
    ## Animation Test with Stock Data
    ###########################################################

    st.title("Animation Test")
    st.write(""" Test """)
    
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")

    ###########################################################
    ## Data Stats
    ###########################################################
    st.title('Data Stats')

    st.write("This is a sample data stats in the mutliapp.")
    st.write("See `apps/data_stats.py` to know how to use it.")

    st.markdown("### Plot Data")
    df = create_table()
    
    st.line_chart(df)