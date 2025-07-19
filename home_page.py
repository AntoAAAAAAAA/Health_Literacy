import streamlit as st
from functions import ensure_defaults, _, get_results

ensure_defaults()

st.title(_('dashboard_title'))
st.text(_('dashboard_intro'))

with st.expander(_('sources_expander_label')):
    st.markdown('''
    - American Diabetes Association. (n.d.). Low blood glucose (hypoglycemia). American Diabetes Association. https://diabetes.org/living-with-diabetes/hypoglycemia-low-blood-glucose 
                
    - American Heart Association. (2024, January 18). Understanding extreme obesity and what you can do. American Heart Association. https://www.heart.org/en/healthy-living/healthy-eating/losing-weight/extreme-obesity-and-what-you-can-do 

    - British Heart Foundation. (2024, October 16). Why your waist size matters. British Heart Foundation. https://www.bhf.org.uk/informationsupport/heart-matters-magazine/medical/measuring-your-waist 

    - Cleveland Clinic. (2022, May 9). Body mass index (BMI). Cleveland Clinic. https://my.clevelandclinic.org/health/articles/9464-body-mass-index-bmi 

    - Mayo Clinic Staff. (2023, November 11). Prediabetes: Symptoms and causes. Mayo Clinic. https://www.mayoclinic.org/diseases-conditions/prediabetes/symptoms-causes/syc-20355278 

    - Mayo Clinic Staff. (2024a, February 29). High blood pressure (hypertension): Symptoms and causes. Mayo Clinic. https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/symptoms-causes/syc-20373410 

    - Mayo Clinic Staff. (2024b, June 13). Low blood pressure (hypotension): Symptoms and causes. Mayo Clinic. https://www.mayoclinic.org/diseases-conditions/low-blood-pressure/symptoms-causes/syc-20355465 

    - Nall, R. (2023, July 27). What are the risks of being underweight? Medical News Today. https://www.medicalnewstoday.com/articles/321612 

    - National Heart, Lung, and Blood Institute. (2022, March 24). Overweight and obesity: Causes and risk factors. https://www.nhlbi.nih.gov/health/overweight-and-obesity/causes 

    - Yale Medicine. (n.d.). Hyperglycemia: Symptoms, causes, and treatments. Yale Medicine. https://www.yalemedicine.org/conditions/hyperglycemia-symptoms-causes-treatments 
''')

st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')

st.markdown(
    f"""
<div style="background-color:#f9f9f9; padding:1rem; border-left:5px solid #888888;
            border-radius:8px; font-size:0.9rem; font-style:italic; color:#333;">
    {_('disclaimer')}
</div>
""",
    unsafe_allow_html=True,
)