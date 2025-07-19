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
            st.markdown(f"### {_('uw_risk_intro')}")
            st.markdown(_("uw_risk_list"))
            st.markdown(f"### {_('uw_causes_intro')}")
            st.markdown(_("uw_causes_list"))
            st.markdown(f"### {_('uw_actions_intro')}")
            st.markdown(_("uw_actions_list"))
            st.markdown(_("uw_closing"))

        elif 18.5 <= bmi <= 24.9:
            st.success(_("bmi_normal_msg"))

        # Helper for BMI ≥ 25
        def high_bmi_block():
            st.markdown(_("ow_para1"))
            st.markdown(f"### {_('ow_risk_intro')}")
            st.markdown(_("ow_risk_list"))
            st.markdown(f"### {_('ow_causes_intro')}")
            st.markdown(_("ow_causes_list"))
            st.markdown(f"### {_('ow_actions_intro')}")
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
            st.markdown(f"### {_('highbp_intro')}")
            st.markdown(_("highbp_causes_list"))
            st.markdown(f"### {_('highbp_complications_intro')}")
            st.markdown(_("highbp_complications_list"))
            st.markdown(f"### {_('highbp_risk_intro')}")
            st.markdown(_("highbp_risk_list"))

        if sys < 90 and dias < 60:
            st.error(_("bp_low_msg"))
            st.info(_("bp_normal_range"))
            st.markdown(f"### {_('lowbp_symptoms_intro')}")
            st.markdown(_("lowbp_symptoms_list"))
            st.markdown(f"### {_('lowbp_causes_intro')}")
            st.markdown(_("lowbp_causes_list"))
            st.markdown(f"### {_('lowbp_treat_intro')}")
            st.markdown(_("lowbp_treat_list"))

        elif sys <= 120 and dias <= 80:
            st.success(_("bp_normal_msg"))

        elif 120 < sys <= 129 and 60 <= dias < 80:
            st.warning(_("bp_elevated_msg"))
            st.info(_("bp_normal_range"))
            st.markdown(_("elevated_para"))
            st.markdown(f"### {_('elevated_steps_intro')}")
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

# ── Blood Glucose placeholder ────────────────────────────────────────
# if results.get("bg"):
#     bg = results.get("bg")
#     with st.expander(_("bg_placeholder")):
#         st.subheader(_("bmi_subheader").replace("BMI", "blood glucose").format(bmi=bg), divider="gray")

#         if bg < 70:
#             st.error("Your blood sugar is LOW")
#             st.info('A normal blood sugar is between 70 to 99 mg/dL')
#             st.text("A low blood sugar can be dangerous. If you have low blood glucose, you may experience:")
#             st.markdown('''
#             -	Feeling shaky
#             -	Being nervous or anxious
#             -	Sweating, chills, and clamminess
#             -	Irritability or impatience
#             -	Confusion
#             -	Fast heartbeat
#             -	Feeling lightheaded or dizzy
#             -	Hunger
#             -	Nausea
#             -	Color draining from the skin (pallor)
#             -	Feeling sleepy
#             -	Feeling weak or having no energy
#             -	Blurred/impaired vision
#             -	Tingling or numbness in the lips, tongue, or cheeks
#             -	Headaches
#             -	Coordination problems or clumsiness
#             -	Nightmares or crying out during sleep
#             ''')
#             st.markdown('You might wonder why you blood sugar is lower than normal. Here are a few reasons why it might be: ')
#             st.markdown('''
#             -	Diabetes
#             -	Issues with adrenal glands
#             -	Pancreas problems
#             -	Hyperthyroidism
#             -	Significant stress (trauma or surgery)
#             -	Certain medications, especially corticosteroids
#             ''')
#             st.markdown('Now that you are aware of your low blood sugar, beginning treatment for it is necessary. ' \
#             'Untreated low blood sugar is very dangerous and can lead to a variety of other problematic health issues. ' \
#             'So what can you do to treat it?: ')
#             st.markdown('''
#             -	15/15 rule – 15 g of fast acting carbs every 15 minutes to treat low blood sugar
#                 -	Fast acting carbs include: glucose tablets, glucose gel tube, ½ cup (4 ounces) of juice or regular soda, 1 tablespoon of sugar or corn syrup, or honey, hard candy, jellybeans 
#                 -	note: Foods like chocolate or peanut butter are NOT the best choice 
#             -	Consult a doctor (they may prescribe medications or give injectable glucagon)
#             ''')
#             st.markdown("Low blood sugar is very common among diabetics. Ask your doctor to find more ways to manage low blood sugar. It is " \
#             "good practice to keep a blood sugar monitor with you at home to track you blood sugar. Eating a healthy, carb-loaded diet and " \
#             "possibly taking medication are both common ways of managing low blood sugar. Be patient with yourself, talk to your healthcare provider, " \
#             "and follow a treatment plan to help hopefully bring your blood sugar back up.")

#         elif 70 <= bg <= 99:
#             st.success("Your blood sugar is normal")
#             st.info('A normal blood sugar is between 70 to 99 mg/dL')
#         elif 100 <= bg <= 125:
#             st.error("Your blood sugar shows that you are PRE-DIABETIC")
#             st.info('A normal blood sugar is between 70 to 99 mg/dL')
#             st.text("A slightly elevated blood sugar like yours indicates that you are on the path to being diabetic. Currently, your " \
#             "blood sugar is within a range that can hopefully be brought down with lifestyle changes and minimal medical intervention. Let's " \
#             "first look at what some common symptoms are for pre-diabetes. ")
#             st.markdown('''
#             Prediabetes actually doesn't usually have any signs of symptoms associated with it. 
#             However, one possible sign is darkedn skin on cetain parts of the body. Affected areas can include the neck, armpits and groin. 
#             ''')
#             st.markdown("Some common causes of pre-diabetes include: ")
#             st.markdown('''
#             -	Issue with insulin in your body
#             -	Family history and genetics plays an important role 
#             ''')
#             st.text('What are some good ways to treat pre-diabetes? Here are a few: ')
#             st.markdown('''
#             -	Eating healthy foods
#             -	Getting active
#             -	Losing excess weight
#             -	Controlling your blood pressure and cholesterol
#             -	Not smoking
#             ''')
#             st.text('It is important to recognize that being pre-diabetes is something that can be managed with pure lifestyle changes. ' \
#             'Making changes to your diet, improving physical activity, and consulting a doctor for management are all great ways to prevent ' \
#             'your blood sugar from increasing into diabetic ranges.')


#         elif bg >= 126:
#             st.error("Your blood sugar shows that you are DIABETIC")
#             st.info('A normal blood sugar is between 70 to 99 mg/dL')
#             st.text('Your blood sugar is high enough that you are considered a diabetic. Not to worry however. Diabetes is ' \
#             'something that has been studied and treated for decades. This means there are plenty of resources (including your ' \
#             'primary care physician) that can help you manage your blood sugar and help you live a healthy life. First, lets start with ' \
#             'some common symptoms that you might be experiencing as a result of your high blood sugar: ')
#             st.markdown('''
#             -	Urinating large amounts
#             -	Excessive thirst
#             -	Feeling tired
#             -	Frequent hunger
#             -	Dry mouth
#             -	Weight loss
#             -	Blurred vision
#             -	Recurrent infections (e.g., urinary infections, skin infections)
#             -	Wounds (cuts, scrapes) that heal slowly
#             ''')
#             st.text('Experiencing any of the above symptoms is totally normal. So now lets get into what might be causing your ' \
#             'blood sugar to stay at such high levels. Here are a few common causes: ')
#             st.markdown('''
#             -	Eating too many carbohydrates
#             -	Not exercising enough
#             -	Not taking enough insulin medication (for type 1 diabetes) or other medications that regulate blood glucose levels
#             -	Medications such as corticosteroids, thiazide diuretics, beta-blockers, and antipsychotics
#             -	Certain conditions that affect the pancreas, which produces insulin
#             -	Medical conditions that can cause insulin resistance, such as Cushing’s syndrome and acromegaly
#             -	Pregnancy
#             -	Stress
#             ''')
#             st.text("Now that you are aware of your high blood sugar, let's get to some treatment options that you have " \
#             "at your disposal: ")
#             st.markdown('''
#             -	Insulin
#                 - For people with type 1 diabetes, insulin is the main treatment for hyperglycemia. In some cases, it may also be used to treat people with type 2 diabetes.
#             -	Glucose-lowering medications
#                 - Various drugs such as metformin may be used to lower blood glucose levels.
#             -	Glucose monitoring
#                 - People with diabetes should monitor their blood glucose levels as instructed by their doctor.
#             -	Lifestyle changes
#                 - People with diabetes can reduce the risk of developing hyperglycemia or treat existing hyperglycemia by getting regular exercise, following a nutritious diet, and maintaining a healthy weight.                 
#             ''')
#             st.text("Diabetes is a common condition across the world. Don't feel alone in your diagnosis. Always be sure that you are using " \
#             "an approved blood sugar monitor to track you blood sugar and keep in contact with you healthcare provider to help manage your " \
#             "symptoms. Having diabetes doesn't mean your life is forever changed. Lots of diabetics live normal, happy lives while being " \
#             "able to maintain their blood sugar. The most important step in your treatment is seeing a doctor and putting together a plan " \
#             "that works with your life. Personalized treatment plans are the hallmark of effective diabetes treatment.")
# else:
#     st.warning(_("no_bg_input"))

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
    with st.expander(_("waist_ratio_placeholder")):
        st.text("")
else:
    st.warning(_("no_waist_input"))

# Debug (remove in prod)
st.text(results)
