import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Tesla and Bitcoin in USD!

""")

#define the ticker symbol
tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(
    period='1d',
    start= '2020-1-01',
    end= '2020-12-31' )

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume Price
""")

st.line_chart(tickerDf.Volume)

tickerSymbol2 = 'BTC-USD'

tickerData2 = yf.Ticker(tickerSymbol2)

tickerDf2 = tickerData.history(
    period='1d',
    start= '2020-1-01',
    end= '2020-12-31' )

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)