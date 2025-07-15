import streamlit as st
from translations import T

def _(key):
    lang = st.session_state.get('lang','en')
    return T[key][lang]


def ensure_defaults():
    if 'lang' not in st.session_state:
        st.session_state['lang'] = 'en'
    if 'results' not in st.session_state:
        st.session_state['results'] = {}

def get_results():
    ensure_defaults()
    return st.session_state['results']