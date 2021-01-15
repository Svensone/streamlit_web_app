import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, stock_price_ticker, test # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Stock Price Ticker", stock_price_ticker)
app.add_app("Test", test)

# The main app
app.run()