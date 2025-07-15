import streamlit as st
from functions import ensure_defaults, _, get_results

ensure_defaults()

st.title(_('dashboard_title'))
st.text(_('dashboard_intro'))

with st.expander(_('sources_expander_label')):
    st.markdown(_('insert_sources_placeholder'))

st.markdown(
    f"""
<div style="background-color:#f9f9f9; padding:1rem; border-left:5px solid #888888;
            border-radius:8px; font-size:0.9rem; font-style:italic; color:#333;">
    {_('disclaimer')}
</div>
""",
    unsafe_allow_html=True,
)