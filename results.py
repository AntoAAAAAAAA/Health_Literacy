import streamlit as st
from functions import _, get_results, ensure_defaults
from fractions import Fraction

ensure_defaults()
results = get_results()

st.text(results)