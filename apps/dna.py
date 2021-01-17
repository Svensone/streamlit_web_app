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
    image = Image.open('assets/lab1.jpg')

    st.image(image,use_column_width=True)
    st.write("""
    # DNA Nucleotide Count Web App

    counting the nucleotide composition of DNA - layouting in streamlit
    """)

    # Input Text Box
    ######################

    st.header("Enter DNA sequence")
    sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
    sequence = st.text_area("Sequence input", sequence_input, height= 200 )
    sequence = sequence.splitlines()
    sequence = sequence[1:]
    sequence = ''.join(sequence)

    # st.header('INPUT (DNA QUERY)')
    # sequence

    def DNA_seq_count(seq):
        d = dict([
            ("A", seq.count('A')),
            ('T', seq.count("T")),
            ('G', seq.count('G')),
            ('C', seq.count('C')),
        ])
        return d
    
    X = DNA_seq_count(sequence)

    # Display the results in various ways
    ######################

    c1, c2, c3, c4 = st.beta_columns([1, 1, 2, 2])

    c1.subheader('1. Print Dictionary')
    c1.write(X)

    c2.subheader('2. Print text')
    c2.write('There are  ' + str(X['A']) + ' adenine (A)')
    c2.write('There are  ' + str(X['T']) + ' thymine (T)')
    c2.write('There are  ' + str(X['G']) + ' guanine (G)')
    c2.write('There are  ' + str(X['C']) + ' cytosine (C)')

    c3.subheader('3. Dataframe')
    df = pd.DataFrame.from_dict(X, orient='index')
    df =df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename({'index': 'nucleotide'}, axis='columns')
    c3.write(df)

    c4.subheader('4. Display Bar graph w. Altair')
    p = alt.Chart(df).mark_bar().encode(
        x= 'nucleotide',
        y = 'count'
    )

    p = p.properties(
        width = alt.Step(60)
    )
    c4.write(p)