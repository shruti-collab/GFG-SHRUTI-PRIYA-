import streamlit as st
import pandas as pd
import preprocessor

df = preprocessor.preprocess()

st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall analysis', 'Athlete wise analysis', 'country-wise analysis')
)

st.dataframe(df)
