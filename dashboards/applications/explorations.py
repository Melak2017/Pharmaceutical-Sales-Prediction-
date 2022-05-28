import streamlit as st
import pandas as pd
import sys
import pickle


def app():

    st.title("Rossmann Pharmaceutical Store Sales")

    st.header("Distribution and Visualization of the pharmaceutical Data")

    st.subheader("Correlation Analysis")
    st.image('screenshots/SalesCustCorr.png')

    st.subheader("Open Stores On Week Days")
    st.image('screenshots/weekendStoreSles.png')

    st.subheader("chrismass sales")
    st.image('screenshots/ChristmasSales13_14.png')
