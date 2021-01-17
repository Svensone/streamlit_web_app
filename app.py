import streamlit as st
import base64

from multiapp import MultiApp
from apps import basketball, home, data_stats, stock_price_ticker, test, dna # import your app modules here

app = MultiApp()
### set Layout Wide (needs to be first thing in app)
#################################
st.set_page_config(
        page_title = "Streamlit App",
        page_icon='🧊',
        layout="wide",
        initial_sidebar_state='collapsed'
        )


### Background Image for Sidebar - not working yet
#################################
side_bg = "bg2.jpg"
side_bg_ext = "jpg"

st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
#stSidebar {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: blue;
}
</style>
""",
    unsafe_allow_html=True,
)


# Add all your application here
app.add_app('Basketball', basketball.app)
app.add_app("Stock Price Ticker", stock_price_ticker.app)
app.add_app("Overview", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Test", test.app)
app.add_app("DNA", dna.app)


# The main app
app.run()