import yfinance as yf
import base64
import streamlit as st
from datetime import date

def app():
    st.title('Stock Price Ticker')
    st.write("""
    # Simple Stock Price App

    Shown are the stock **closing price** and ***volume*** of Tesla and Bitcoin in USD!

    """)

    ### for TESLA
    #####################
    tickerSymbol = 'TSLA'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(
        period='1d',
        start= '2020-1-01',
        end= '2021-01-21' )

    st.write("""
    ## Closing Price Tesla
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ### Volume Price Tesla
    """)

    st.line_chart(tickerDf.Volume)

    ### BITCOIN
    #####################
    tickerSymbol2 = 'BTC-USD'
    tickerData2 = yf.Ticker(tickerSymbol2)
    end = date.today().strftime("%Y-%m-%d")
    tickerDf2 = tickerData2.history(
        period='1d',
        start= '2017-1-01',
        end= end )

    st.write("""
    ## Closing Price Bitcoin
    """)
    st.line_chart(tickerDf2.Close)

    st.write("""
    ### Volume Price Bitcoin
    """)
    st.line_chart(tickerDf2.Volume)

    # Set Background Image *local file" - heroku ? working
    ###################################################
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

    set_png_as_page_bg('assets/pig_money.jpg')