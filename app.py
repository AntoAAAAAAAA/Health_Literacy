import streamlit as st
from functions import ensure_defaults

st.set_page_config(page_title='Health Literacy App',
                   layout='wide')

ensure_defaults()
LANG_OPTS = {'English': 'en', 'Spanish': 'es'}
label = st.sidebar.selectbox(
    'Select a Language',
    list(LANG_OPTS.keys()),
    index = list(LANG_OPTS.values()).index(st.session_state.get('lang', 'en'))
)
st.session_state['lang'] = LANG_OPTS[label]

home_page = st.Page('home_page.py', title='Home')
input_pg = st.Page('input.py', title='Input')
results_pg = st.Page('results.py', title='Results')

pg = st.navigation([home_page, input_pg, results_pg])
pg.run()