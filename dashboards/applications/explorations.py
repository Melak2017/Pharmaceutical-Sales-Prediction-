import streamlit as st
import pandas as pd
import sys
import pickle


def app():

    st.title("Rossmann Pharmaceutical Store Sales")

    st.header("Distribution and Visualization of the pharmaceutical Data")

    st.subheader("Sales on school holidays")
    st.image('screenshots/SchoolHolidaySales.png')

    st.subheader("Sales and Customer behavior on state holidays")
    st.image('screenshots/SalesOnStateHoliday.png')

    st.subheader("Effect of promotion on sales behavior of different stores")
    st.image('screenshots/effectPromoStore.png')

    st.subheader(
        "Effect of promotion on customer  behavior of  different stores")
    st.image('screenshots/effCust.PNG')

    st.subheader("chrismass sales")
    st.image('screenshots/ChristmasSales13_14.png')

    st.subheader("Open Stores On Week Days")
    st.image('screenshots/weekendStoreSles.png')

    st.subheader("Sales and Costumer behavior Store Assortment type")
    st.image('screenshots/SalesCustAssort2.png')
