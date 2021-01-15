import streamlit as st
import base64

from multiapp import MultiApp
from apps import home, data_stats, stock_price_ticker, test # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Stock Price Ticker", stock_price_ticker.app)
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Test", test.app)


# Background Image for Sidebar and Home Screen
main_bg = "bg2.jpg"
main_bg_ext = "jpg"

side_bg = "bg2.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover;

    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# The main app
app.run()