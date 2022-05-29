


import os
import sys
import streamlit as st

sys.path.insert(0, './dashboards')

from applications import explorations
from multiapp import MultiApp

st.set_page_config(page_title="Rossmann Sales Predictions", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Rossmann Sales Predictions
""")
with open('dashboards/applications/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Add all your application here
app.add_app("visualizations", explorations.app)

# The main app
app.run()
