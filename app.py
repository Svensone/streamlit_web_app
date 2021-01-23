import streamlit as st
import base64

from multiapp import MultiApp
from apps import basketball, iris_ml, stock_price_ticker, test, dna # import your app modules here
# batik_clf,
from helper import local_css

 
app = MultiApp()
### set Layout Wide (needs to be first thing in app)
#################################
st.set_page_config(
        page_title = "Streamlit App",
        page_icon='🧊',
        layout="wide",
        initial_sidebar_state='collapsed'
        )

## test local css
##################
local_css("style.css")

### Background Image for Sidebar - not working yet
#################################
# side_bg = "assets/bg-side.jpg"
# side_bg_ext = "jpg"

# st.markdown(
#     f"""
#     <style>
#     .css-1mazlfv {{
#             background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Add all your application here
# app.add_app('Batik Cloth Classification', batik_clf.app)
app.add_app('Iris Classification', iris_ml.app)
app.add_app("DNA", dna.app)
app.add_app('Basketball', basketball.app)
app.add_app("Stock Price Ticker", stock_price_ticker.app)
app.add_app("Test", test.app)

# The main app
app.run()