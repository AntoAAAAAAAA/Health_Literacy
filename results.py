import streamlit as st
from functions import _, get_results, ensure_defaults

ensure_defaults()
results = get_results()

# ── Header ───────────────────────────────────────────────────────────
st.title(_("results_title"))
st.text(_("results_intro"))
st.divider()


# ── BMI ──────────────────────────────────────────────────────────────
if results.get("bmi"):
    bmi = results["bmi"]
    with st.expander(_("bmi_expander_label")):
        st.subheader(_("bmi_subheader").format(bmi=bmi), divider="gray")

        if bmi < 18.5:
            st.error(_("bmi_under_msg"))
            st.info(_("bmi_normal_range"))
            st.markdown(_("uw_para1"))
            st.markdown(f"{_('uw_risk_intro')}")
            st.markdown(_("uw_risk_list"))
            st.markdown(f" {_('uw_causes_intro')}")
            st.markdown(_("uw_causes_list"))
            st.markdown(f" {_('uw_actions_intro')}")
            st.markdown(_("uw_actions_list"))
            st.markdown(_("uw_closing"))

        elif 18.5 <= bmi <= 24.9:
            st.success(_("bmi_normal_msg"))

        # Helper for BMI ≥ 25
        def high_bmi_block():
            st.markdown(_("ow_para1"))
            st.markdown(f" {_('ow_risk_intro')}")
            st.markdown(_("ow_risk_list"))
            st.markdown(f" {_('ow_causes_intro')}")
            st.markdown(_("ow_causes_list"))
            st.markdown(f" {_('ow_actions_intro')}")
            st.markdown(_("ow_actions_list"))
            st.markdown(_("ow_closing"))

        if 25 <= bmi <= 29.9:
            st.success(_("bmi_over_msg"))
            st.info(_("bmi_normal_range"))
            high_bmi_block()
        elif 30 <= bmi <= 34.9:
            st.error(_("bmi_ob1_msg"))
            st.info(_("bmi_normal_range"))
            high_bmi_block()
        elif 35 <= bmi <= 39.9:
            st.error(_("bmi_ob2_msg"))
            st.info(_("bmi_normal_range"))
            high_bmi_block()
        elif bmi > 40:
            st.error(_("bmi_ob3_msg"))
            st.info(_("bmi_normal_range"))
            high_bmi_block()
else:
    st.warning(_("no_bmi_input"))



# ── Blood Pressure ───────────────────────────────────────────────────
if results.get("bp"):
    bp   = results["bp"]
    sys  = results.get("sys")
    dias = results.get("dias")

    with st.expander(_("bp_expander_label")):
        st.subheader(_("bp_subheader").format(bp=bp), divider="gray")

        # Helper for high-BP explanations
        def high_bp_details():
            st.markdown(f" {_('highbp_intro')}")
            st.markdown(_("highbp_causes_list"))
            st.markdown(f" {_('highbp_complications_intro')}")
            st.markdown(_("highbp_complications_list"))
            st.markdown(f" {_('highbp_risk_intro')}")
            st.markdown(_("highbp_risk_list"))

        if sys < 90 and dias < 60:
            st.error(_("bp_low_msg"))
            st.info(_("bp_normal_range"))
            st.markdown(f" {_('lowbp_symptoms_intro')}")
            st.markdown(_("lowbp_symptoms_list"))
            st.markdown(f" {_('lowbp_causes_intro')}")
            st.markdown(_("lowbp_causes_list"))
            st.markdown(f" {_('lowbp_treat_intro')}")
            st.markdown(_("lowbp_treat_list"))

        elif sys <= 120 and dias <= 80:
            st.success(_("bp_normal_msg"))

        elif 120 < sys <= 129 and 60 <= dias < 80:
            st.warning(_("bp_elevated_msg"))
            st.info(_("bp_normal_range"))
            st.markdown(_("elevated_para"))
            st.markdown(f" {_('elevated_steps_intro')}")
            st.markdown(_("elevated_steps_list"))
            st.markdown(_("elevated_closing"))

        elif 130 <= sys <= 139 and 80 < dias < 89:
            st.error(_("bp_stage1_msg"))
            st.info(_("bp_normal_range"))
            high_bp_details()
            st.markdown(_("stage1_para"))

        elif sys >= 140 and dias >= 90:
            st.error(_("bp_stage2_msg"))
            st.info(_("bp_normal_range"))
            high_bp_details()
            st.markdown(_("stage2_para"))

        elif sys >= 180 or dias >= 120:
            st.error(_("bp_crisis_msg"))
            st.info(_("bp_normal_range"))
            st.markdown(_("crisis_para"))

        elif sys > dias:
            st.error(_("bp_iso_sys_msg"))
            st.info(_("bp_normal_range"))
            high_bp_details()

        elif sys < dias:
            st.error(_("bp_iso_dia_msg"))
            st.info(_("bp_normal_range"))
            high_bp_details()

else:
    st.warning(_("no_bp_input"))



# ── Blood Glucose ────────────────────────────────────────────────────
if results.get("bg"):
    bg = results["bg"]
    with st.expander(_("bg_placeholder")):
        st.subheader(_("bg_subheader").format(bg=bg), divider="gray")

        if bg < 70:
            st.error(_("bg_low_msg"))
            st.info(_("bg_normal_range"))
            st.markdown(_("bg_low_para1"))
            st.markdown(_("bg_low_symptoms"))
            st.markdown(_("bg_low_causes_intro"))
            st.markdown(_("bg_low_causes"))
            st.markdown(_("bg_low_treat_intro"))
            st.markdown(_("bg_low_treat"))
            st.markdown(_("bg_low_close"))

        elif 70 <= bg <= 99:
            st.success(_("bg_normal_msg"))
            st.info(_("bg_normal_range"))

        elif 100 <= bg <= 125:
            st.error(_("bg_pre_msg"))
            st.info(_("bg_normal_range"))
            st.markdown(_("bg_pre_para1"))
            st.markdown(_("bg_pre_symptom_note"))
            st.markdown(_("bg_pre_causes_intro"))
            st.markdown(_("bg_pre_causes"))
            st.markdown(_("bg_pre_treat_intro"))
            st.markdown(_("bg_pre_treat"))
            st.markdown(_("bg_pre_close"))

        elif bg >= 126:
            st.error(_("bg_diab_msg"))
            st.info(_("bg_normal_range"))
            st.markdown(_("bg_diab_para1"))
            st.markdown(_("bg_diab_symptoms"))
            st.markdown(_("bg_diab_causes_intro"))
            st.markdown(_("bg_diab_causes"))
            st.markdown(_("bg_diab_treat_intro"))
            st.markdown(_("bg_diab_treat"))
            st.markdown(_("bg_diab_close"))
else:
    st.warning(_("no_bg_input"))



# ── Waist Ratio placeholder ─────────────────────────────────────────-
if results.get("waist_ratio"):
    wr = results["waist_ratio"]
    with st.expander(_("waist_ratio_placeholder")):
        st.subheader(_("wr_subheader").format(wr=wr), divider="gray")

        # UNDERWEIGHT
        if wr < 0.4:
            st.warning(_("wr_low_msg"))
            st.info(_("wr_healthy_range"))
            st.markdown(_("wr_low_para1"))
            st.markdown(_("wr_under_risk_intro"))
            st.markdown(_("uw_risk_list"))
            st.markdown(_("wr_under_causes_intro"))
            st.markdown(_("uw_causes_list"))
            st.markdown(_("wr_under_actions_intro"))
            st.markdown(_("uw_actions_list"))
            st.markdown(_("wr_under_close"))

        # NORMAL
        elif 0.4 <= wr <= 0.49:
            st.success(_("wr_normal_msg"))
            st.info(_("wr_healthy_range"))

        # INCREASED RISK
        elif 0.5 <= wr <= 0.59:
            st.warning(_("wr_increased_msg"))
            st.info(_("wr_healthy_range"))
            st.markdown(_("wr_over_para1"))
            st.markdown(_("ow_risk_list"))
            st.markdown(_("wr_over_causes_intro"))
            st.markdown(_("ow_causes_list"))
            st.markdown(_("wr_over_plan_intro"))
            st.markdown(_("ow_actions_list"))
            st.markdown(_("wr_over_close"))

        # HIGH RISK
        elif wr >= 0.60:
            st.error(_("wr_high_msg"))
            st.info(_("wr_healthy_range"))
            st.markdown(_("wr_over_para1"))
            st.markdown(_("ow_risk_list"))
            st.markdown(_("wr_over_causes_intro"))
            st.markdown(_("ow_causes_list"))
            st.markdown(_("wr_over_plan_intro"))
            st.markdown(_("ow_actions_list"))
            st.markdown(_("wr_over_close"))
else:
    st.warning(_("no_waist_input"))