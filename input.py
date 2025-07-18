import streamlit as st
from functions import _, get_results, ensure_defaults

ensure_defaults()
st.markdown(
    """
    <style>
    div.streamlit-expanderHeader {
        font-weight: 600;
        font-size: 1.1rem;
        transition: color 0.2s ease;
    }
    div.streamlit-expanderHeader:hover {
        color: var(--secondary);  /* Theme accent color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Page header ---------------------------------------------------
st.title(_("input_page_title"))
st.text(_("input_page_intro"))
st.divider()

# --- Load saved data ---------------------------------------------------
results = get_results()
prev_wt   = results.get("weight")
prev_ht   = results.get("height")
wtlb      = results.get("weight_lb")
htft      = results.get("height_ft")
htinch    = results.get("height_inch")
prev_sys  = results.get("sys")
prev_dias = results.get("dias")
prev_bg = results.get('bg')
prev_waistinch = results.get('waistinch')
prev_waistcm = results.get('waistcm')
prev_waist_ht_in = results.get('waist_ht_in')
prev_waist_ht_cm = results.get('waist_ht_cm')

st.text('Before you begin, please take the time to convert your height and weight metrics. We highly recommend this' \
'since most health metric calculations are done using the metric system instead of the commonly used imperial system in the ' \
'United States. As such, we would like to help you by providing converters below that will do the hard work for you!')
# --- Converters ---------------------------------------------------
col1, col2 = st.columns(2, border=True)

# • Weight (lb → kg)
col1.text(_("weight_converter_label"))
lb = col1.number_input(
    _("weight_input_label"),
    min_value=0.0,
    key="weight_lb",
    value=float(wtlb) if wtlb is not None else 0.0,
    format="%.1f",
)
newkg = lb / 2.205
if col1.button(_("convert_button"), key="1"):
    col1.warning(f"{round(newkg, 2)} kg")
    st.session_state["results"].update({"weight_lb": lb})

# • Height (ft/in → m)
col2.text(_("height_converter_label"))
ft = col2.number_input(
    _("height_ft_input_label"),
    key="height_ft",
    value=htft if htft is not None else 0,
)
inch = col2.number_input(
    _("height_in_input_label"),
    key="height_inch",
    value=float(htinch) if htinch is not None else 0.0,
)
new_ht = ((ft * 12) + inch) / 39.37
if col2.button(_("convert_button"), key="2"):
    col2.warning(f"{round(new_ht, 2)} m")
    st.session_state["results"].update(
        {"height_ft": ft, "height_inch": inch}
    )
st.divider()

# --- BMI ------------------------------------------------------
with st.expander(_("bmi_expander_label")):
    weight = st.number_input(
        _("weight_input_kg_label"),
        min_value=0.0,
        key="weight",
        value=prev_wt if prev_wt is not None else 0.0,
    )
    height = st.number_input(
        _("height_input_m_label"),
        min_value=0.0,
        key="height",
        value=prev_ht if prev_ht is not None else 0.0,
    )

    if st.button(_("calculate_button"), key="3"):
        bmi = weight / (height**2) if height else 0
        st.session_state["results"].update(
            {"weight": weight, "height": height, "bmi": round(bmi, 2)}
        )
        st.success(_("bmi_result_message").format(bmi=f"{bmi:.1f}"))

    # if "bmi" in st.session_state["results"]:
    #     if st.button(_("interpret_results_button"), key="4"):
    #         st.switch_page("results.py")

st.text(" ")
st.text(" ")

# --- Blood Pressure ---------------------------------
with st.expander(_("blood_pressure_expander_label")):
    left, middle, right = st.columns(3, vertical_alignment="top")
    systole = left.number_input(
        _("systolic_label"),
        step=1,
        value=prev_sys if prev_sys is not None else 0,
    )
    diastole = middle.number_input(
        _("diastolic_label"),
        step=1,
        value=prev_dias if prev_dias is not None else 0,
    )
    right.text("")
    bp = f"{systole}/{diastole}"

    if st.button(_("save_button"), key="5"):
        st.session_state["results"].update(
            {"sys": systole, "dias": diastole, "bp": bp})
        st.toast(_("saved_toast"))

st.text(" ")
st.text(" ")

# -- Blood Glucose --------------------------------------------------------
with st.expander(_("blood_glucose_expander_label")):
    bg = st.number_input(_("blood_glucose_input_label"), 
                         value=prev_bg if prev_bg is not None else 0.0)
    if st.button(_("save_button"), key="6"):
        st.session_state["results"].update({"bg": bg})
        st.toast(_("saved_toast"))
st.text(' ')
st.text(' ')

# -- Waist Circumference --------------------------------------------------------
with st.expander(_("Waist Circumference")):
    col1, col2 = st.columns(2)

    unit_pref = st.session_state.get('unit_pref', 'in')
    units = col1.radio(
        _("Choose your Units:"),
        ['in', 'cm'],                     
        horizontal=True,
        key='unit_pref'
        )
    if units == 'in':
        waistinch = col2.slider(_("Waist (in)"), 20.0, 60.0,
                            value= prev_waistinch if prev_waistinch is not None else 30.0, 
                            step=0.25)
    else:
        waistcm = col2.slider(_("Waist (cm)"), 50.0, 150.0,
                            value= prev_waistcm if prev_waistcm is not None else 80.0, 
                            step= 0.5)

    

    col1, col2 = st.columns(2)
    if units == 'in':
        waist_ht_in = col2.number_input('Height in inches:', 
                                        value=prev_waist_ht_in if prev_waist_ht_in is not None else 0.0,
                                        step=0.5)
        st.session_state['results'].update({'waist_ht_in': waist_ht_in})
    else:
        waist_ht_cm = col2.number_input('Height in cm:', 
                                        value=prev_waist_ht_cm if prev_waist_ht_cm is not None else 0.0,
                                        step=0.25)
        st.session_state['results'].update({'waist_ht_cm': waist_ht_cm})

    # Waist Ratio calculation logic 
    waist = waistinch if units == 'in' else waistcm
    height = waist_ht_in if units == 'in' else waist_ht_cm
    waist_ratio = waist/height if height else None

    # Buttons
    if col2.button('Click Here to Calculate Ratio'):
        st.info(round(waist_ratio, 2))

    if col2.button(_("save_button")):
        if units == 'in':
            st.session_state['results'].update({"waistinch": waistinch})
            st.session_state['results'].update({'final_waist': f'{waistinch} in'})
        else:
            st.session_state['results'].update({'waistcm': waistcm})
            st.session_state['results'].update({'final_waist': f'{waistcm} cm'})
        if waist_ratio:
            st.session_state['results'].update({'waist_ratio': waist_ratio})
        st.toast(_("saved_toast"))

# -- See Results ----------------------------------------------------------------------
st.divider()
col1, col2, col3 = st.columns(3, vertical_alignment='bottom')
if col2.button('Click Here to Interpret Your Numbers!'):
    st.switch_page('results.py')
col2.caption('Note: Make sure you saved all your numbers!')
