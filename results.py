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
    with st.expander(label='BMI'):
        st.subheader(f"Your calculated BMI is {bmi}", divider='gray')

        if bmi < 18.5:
            st.error("Your BMI is considered UNDERWEIGHT.")
            st.info('A normal BMI is between 18.5 and 25')
            st.markdown("First off . . . Don't worry! Being underweight is not the end of the world." \
            " BMI is not the perfect health metric in all cases and should not be used as the sole number to determine " \
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them." \
            " Let's look a little further into what might be causing your low BMI and what you could do to help.")
            st.markdown('First off, why is having a low BMI possibly dangerous? Well it increases your chances of:')
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
            " BMI is not the perfect health metric in all cases and should not be used as the sole number to determine " \
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them." \
            " Let's look a little further into what might be causing your high BMI and what you could do to help.")
            st.markdown('First off, why is having a high BMI possibly dangerous? Well it increases your chances of:')
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
            st.info('A normal BMI is between 18.5 and 25')
            high_bmi_text()
        elif 30 <= bmi <= 34.9:
            st.error("Your BMI is considered Class I OBESE")
            st.info('A normal BMI is between 18.5 and 25')
            high_bmi_text()
        elif 35 <= bmi <= 39.9:
            st.error("Your BMI is considered Class II OBESE")
            st.info('A normal BMI is between 18.5 and 25')
            high_bmi_text()
        elif bmi > 40:
            st.error("Your BMI is considered Class III OBESE")
            st.info('A normal BMI is between 18.5 and 25')
            high_bmi_text()
else:
    st.subheader('No BMI Input')

# --Blood Pressure-------------------------------------------------
if results.get('bp'):
    bp = results.get('bp')
    sys = results.get('sys')
    dias = results.get('dias')
    with st.expander('Blood Pressure'):
        st.subheader(f'Your blood pressure is {bp}', divider='gray')

        # Low BP
        if sys < 90 and dias < 60:
            st.error("Your blood pressure is LOW")
            st.info('A normal blood pressure is between 90/60 and 120/80')
            st.text("Having a consistently low blood pressure can be dangerous. You might be experiencing some of these symptoms:")
            st.text('''
            -	Blurred or fading vision
            -	Dizzy or lightheaded feelings
            -	Fainting
            -	Fatigue
            -	Trouble concentrating
            -	Upset stomach
            ''')
            st.markdown('''
            So what might be causing such a low blood pressure? A few things may be:
             -	Pregnancy
            -	Heart and heart valve conditions 
            -	Hormone-related issues
            -	Dehydration (very common)
            -	Blood loss
            -	Severe infection
            -	Severe allergic reaction (anaphylaxis)
            -	Lack of essential nutrients in diet 
            -	Medications 
            ''')
            st.markdown('A few ways this can be treated is by:')
            st.markdown('''
            - Use more salt
                - Salt helps raise blood pressure, but too much is dangerous. Talk to a doctor to determine amount
            - Drink more water 
            - Wear compression stockings
                - Relieve pain and swelling in legs from varicose veins (if applicable)
            - Medicines 
                - Consult your doctor for medication recommendations 
                - Midodrine (Orvaten) is a common medicine that could be prescribed
            ''')
        # Normal BP
        elif sys <= 120 and dias <= 80:
            st.success('Your blood pressure is normal')

        # Elevated BP
        elif 120 < sys <= 129 and 60 <= dias < 80:
            st.warning('Your blood pressure is ELEVATED')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            st.text("Your blood pressure is a little elevated. Not to worry however, because this is completely normal. " \
            "Its not uncommon to see a slightly elevated blood pressure. Elevated blood pressure can creep up over time though, " \
            "raising your chances of heart failure, stroke, and other serious health problems. " \
            "The upside is you’ve spotted it now, so you can start making steady changes to bring those numbers back into a healthy range.")
            st.text('Some ways to lower your blood pressure:')
            st.markdown('''
            - Healthier diet
                - Removing excess fats and salts 
            - Exercise more frequently
            - Limit alcohol and smoking
            - Find ways to lower stress in your life
            ''')
            st.text('You are in a good spot. Knowing that your blood pressure is low before it gets into hypertensive levels ' \
            'helps give you time to lower it naturally without serious medical intervention. Focusing on a heart-healthy diet, exercising ' \
            'regularly, and tracking your blood pressure at home should be goals now. Good luck!')

        def high_bp():
            st.text('Your blood pressure is quite high and needs to be lowered. Lets look at some of the main causes of a ' \
            'high blood pressure:')
            st.markdown('''
            -	**Primary hypertension**: No identifiable cause. A general increase over the years due to gradual buildup of plaque in the arteries. Expected with age
            -	**Secondary hypertension**: There is some sort of underlying condition
                -	Adrenal gland tumors
                -	Blood vessel problems present at birth (ex. congenital heart defects)
                -	Cough and cold medicines, pain relievers, birth control pills, or other prescription drugs
                -	Illegal drugs (ex. amphetamines)
                -	Kidney disease
                -	Obstructive sleep apnea 
                -	Thyroid problems 
            -	**White coat hypertension**: A high blood pressure that only occurs in clinical settings (ex. doctors offices). This is 
                        usually causes by the stress of going to a doctor, and not something health-related.
            ''')
            st.markdown('''
            If left untreated, high blood pressure can possibly lead to:
            -	Heart problems
            -	Aneurysm
            -	Kidney problems
            -	Metabolic syndrome
            -	Dementia 
            -	Changes in memory or understanding 
                        
            Some things that can increase your risk of having high blood pressure include:
            -	Age
            -	Sex (more common in men)
            -	Family history
            -	Race (most common in African Americans)
            -	Obesity or being overweight
            -	Lack of exercise
            -	Tobacco use or vaping
            -	Too much salt
            -	Low potassium
            -	Too much alcohol
            -	Stress
            -	Pregnancy
            ''')
        
        if 130 <= sys <= 139 and 80 < dias < 89:
            st.error('Your blood pressure shows that you are in STAGE 1 HYPERTENSION')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            high_bp()
            st.text('There is such thing as Stage II hypertension as well. Right now, you are in Stage I. This means ' \
            'that your blood pressure can be controlled with a change in lifestyle and that you are not in immediate ' \
            'need of medication. Once your hypertension goes past a certain point, you will be recommended medication to help control it. As such, ' \
            'please take precaution and continue to care for your blood pressure.')

        elif sys >= 140 and dias >= 90:
            st.error('Your blood pressure shows that you are in STAGE 2 HYPERTENSION')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            high_bp()
            st.text('As someone in Stage II Hypertension, it is important to note that you need to see a healthcare professional ' \
            'immediately to help control your blood pressure. Your provider will most likey help you by providing prescription ' \
            'medications. With increased exercise, a controlled diet, and some medicine, hopefully you can lower your blood ' \
            'pressure back to a safe range.')

        elif sys >=180 or dias >= 120:
            st.error('HYPERTENSIVE CRISIS: PLEASE CONSULT A DOCTOR IMMEDIATELY')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            st.text('Your blood pressure is dangerously high. Please see a healthcare professional immediately!')

        elif sys > dias:
            st.error('Isolated Systolic Hypertension')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            high_bp()

        elif sys < dias:
            st.error('Isolated Diastolic Hypertension')
            st.info('A normal blood pressure is between 90/60 and 120/80')
            high_bp()

else:
    st.subheader('No Blood Pressure input')

#--Blood Glucose-------------------------------------------------
if results.get('bg'):
    with st.container(border=True):
        st.text('Blood Glucose')
else:
    st.subheader('***No Blood Glucose input***')

#--Waist Ratio-------------------------------------------------
if results.get('waist_ratio'):
    with st.container(border=True):
        st.text('Waist Ratio')
else:
    st.subheader('***No Waist Ratio input***')


st.text(results)