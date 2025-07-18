import streamlit as st
from functions import _, get_results, ensure_defaults
from fractions import Fraction

ensure_defaults()
results = get_results()

st.title('Results')
st.text('Use this page to interpret the results you inputted. Learn more about each category. ')
st.divider()

# --BMI---------------------------------------------------------------
if results.get('bmi'):
    bmi = results.get('bmi')
    with st.container(border=True):
        st.subheader('BMI')
        st.text(f"Your calculated BMI is {bmi}")

        if bmi < 18.5:
            st.warning("Your BMI is considered UNDERWEIGHT")
            st.markdown("First off . . . Don't worry! Being underweight is not the end of the world." \
            " BMI is not the perfect health metric in all cases and should be used as the sole number to determine " \
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them." \
            " Let's look a little further into what might be causing your low BMI and what you could do to help.")
            st.markdown('First off, why is having a low BMI possibly dangerous? Well it increases your chances of any of these:')
            st.markdown('''
            - Osteoporosis
            -	More sick frequently
            -	Fatigue
            -	Anemia
            -	Irregular preiods and premature births in women
            -	Slow or impaired growth 
            ''')
            st.markdown('Common causes of low BMI include:')
            st.markdown('''
            -   Family history 
            -	High metabolism
            -	Frequent physical activity (frequent runner, athlete, etc.)
            -	Potential physical illness or chronic diseases 
            -	Mental illness 
            -	Possible Eating disorder (**Very important to see a doctor if you think you have this**)
                        ''')
            st.markdown('Thankfully, being underweight is not uncommon. There are lots of ' \
            'easy, doable ways to help bring up your BMI! Some ways include:')
            st.markdown('''
            -	High protein and whole-grain snacks (carbs! carbs! carbs!)
                -   Peanut butter crackers, protein bars, trail mix, pita chips with hummus, a handful of almonds 
            -	Eat several small meals a day as opposed to a set number of big meals
            -	Add toppings or additional food to current meals
                -   Ex. adding nuts to yogurt, seeds to salad or soup, putting nut butter on whole-grain toast
            -   Decreasing intense cardio workouts and shifting more towards weight-lifting
            ''')
            st.markdown("Finding out that you're underweight is a great start to figuring out what to do. Making changes to " \
            "your diet and emphasizing weight training are good ways to start. At the end of the day, seeing your primary care " \
            "physician or a dietician will make fundamental differences in your journey. Take time to see a professional. " \
            "Good luck on your journey!")           

        elif 18.5 <= bmi <= 24.9:
            st.warning("Your BMI is considered NORMAL")

        def high_bmi_text():
            st.markdown("First off . . . Don't worry! Being overweight is not the end of the world." \
            " BMI is not the perfect health metric in all cases and should be used as the sole number to determine " \
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them." \
            " Let's look a little further into what might be causing your high BMI and what you could do to help.")
            st.markdown('First off, why is having a high BMI possibly dangerous? Well it increases your chances of any of these:')
            st.markdown('''
            - Heart Disease
            - Type II diabetes
            - High Blood Pressure
            - Certain cancers 
            - Liver Disease
            - Breathing/Respiratory Issues
            - Fertility Problems
            - Mental Health Issues
            ''')
            st.markdown('Common causes of high BMI include:')
            st.markdown('''
            -	Lack of physical activity
                -	Adults need 150 min of aerobic activity a week, Children need 60 minutes each day 
                -	Muscle-strengthening activities (like lifting weights) is recommended for major muscles groups 2 or more days each week
            -	Calorie excess (eating too many calories)
                -	2000 calories is recommended per day. Anything above may be dangerous
            -	Too much saturated fat
                -	For a 2000 calorie day, no more than about 22g of saturated fats
            -	Eating foods high in added sugar		
            -	Bad-quality sleep
                -	Consistently getting less than 7 hours of sleep is considered below recommended
            -	Stress
            -	Specific medical conditions (please see a doctor to determine this)
            -	Genetics
            -	Medications 
                        ''')
            st.markdown('Thankfully, being underweight is not uncommon. There are lots of ' \
            'easy, doable ways to help bring up your BMI! Some ways include:')
            st.markdown('''
            -	Physical activity
                -	Start playing a sport
                -   Go on walks a few times a week (10 minutes is better than nothing)
                -	Find long-form content you can watch/listen to while exercising or walking
                -	Get a workout buddy
                -	Start going to the gym (or start going more consistently/more frequently)
            -	Start tracking calories using online applications (mobile applications are best)
            -	Eat healthier (more fruits and vegetables, heart healthy meals)
            -	Medication 
            -	Surgery (last solution to consider. Need to see a doctor)
            ''')
            st.markdown("Finding out that you're overweight is a great start to figuring out what to do. Making changes to " \
            "your diet and emphasizing exercise are good ways to start. At the end of the day, seeing your primary care " \
            "physician or a dietician will make fundamental differences in your journey. Take time to see a professional. " \
            "Good luck on your journey!")           
            st.markdown('')
        if 25 <= bmi <= 29.9:
            st.success("Your BMI is considered OVERWEIGHT")
            high_bmi_text()
        elif 30 <= bmi <= 34.9:
            st.error("Your BMI is considered Class I OBESE")
            high_bmi_text()
        elif 35 <= bmi <= 39.9:
            st.error("Your BMI is considered Class II OBESE")
            high_bmi_text()
        elif bmi > 40:
            st.error("Your BMI is considered Class III OBESE")
            high_bmi_text()


else:
    st.subheader('No BMI input')


# --Blood Pressure-------------------------------------------------
if results.get('bp'):
    with st.container(border=True):
        st.text('Blood Pressure')
else:
    st.subheader('No Blood Pressure input')

#--Blood Glucose-------------------------------------------------
if results.get('bg'):
    with st.container(border=True):
        st.text('Blood Glucose')
else:
    st.subheader('No Blood Glucose input')

#--Waist Ratio-------------------------------------------------
if results.get('waist_ratio'):
    with st.container(border=True):
        st.text('Waist Ratio')
else:
    st.subheader('No Waist Ratio input')




st.text(results)