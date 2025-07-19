import streamlit as st

T = {
    # --- Home Page ----------------------------------------------------
    "dashboard_title": {
        "en": "Health Literacy Dashboard",
        "es": "Panel de Alfabetización en Salud",
    },
    "dashboard_intro": {
        "en": (
            "This dashboard provides bilingual health information to patients "
            "who need quick, accessible health-related guidance. We use reliable "
            "and accredited sources for this project. Our hope is that individuals "
            "seeking metrics about their BMI, blood pressure, blood sugar, or other "
            "common health markers can come to this page and learn valuable "
            "information about their personal health."
        ),
        "es": (
            "Este panel ofrece información sanitaria bilingüe a los pacientes que "
            "necesitan orientación de salud rápida y accesible. Para este proyecto "
            "utilizamos fuentes confiables y acreditadas. Nuestro objetivo es que "
            "las personas que busquen métricas sobre su IMC, presión arterial, "
            "glucosa en sangre u otros indicadores comunes puedan usar esta página "
            "para obtener información valiosa sobre su salud personal."
        ),
    },
    "sources_expander_label": {
        "en": "See a list of sources we used:",
        "es": "Ver la lista de fuentes utilizadas:",
    },
    "insert_sources_placeholder": {
        "en": "**Insert sources here**",
        "es": "**Inserte las fuentes aquí**",
    },
    "disclaimer": {
        "en": (
            "⚠️ **Disclaimer:** This tool is for general educational purposes only "
            "and does not provide medical advice. Please consult a healthcare "
            "provider for personalized guidance."
        ),
        "es": (
            "⚠️ **Aviso:** Esta herramienta tiene fines educativos generales y no "
            "constituye asesoramiento médico. Consulte a un profesional de la salud "
            "para obtener orientación personalizada."
        ),
    },

    # --- Inputs Page --------------------------------------------------
    "input_page_title": {
        "en": "Input your Health Metrics!",
        "es": "¡Introduce tus Métricas de Salud!",
    },
    "input_page_intro": {
        "en": (
            "In this section, you can input your personal health data and learn "
            "more about what it means."
        ),
        "es": (
            "En esta sección, puedes introducir tus datos personales de salud y "
            "aprender más sobre lo que significan."
        ),
    },

    # Converters -------------------------------------------------------

    "converter_explanation": {
        "en": (
            "Before you begin, please take the time to convert your height and weight metrics. "
            "We highly recommend this since most health metric calculations are done using the metric system "
            "instead of the commonly used imperial system in the United States. As such, we would like to help you "
            "by providing converters below that will do the hard work for you!"
        ),
        "es": (
            "Antes de comenzar, por favor, tómese el tiempo para convertir sus medidas de altura y peso. "
            "Le recomendamos encarecidamente que lo haga, ya que la mayoría de los cálculos de medidas de salud se "
            "realizan utilizando el sistema métrico decimal en lugar del sistema imperial, comúnmente utilizado en Estados Unidos. "
            "Por ello, le ayudamos con los conversores a continuación que le facilitarán el trabajo."
        ),
    },

    "weight_converter_label": {
        "en": "Convert weight in pounds (lb) into kilograms (kg) here",
        "es": "Convierte el peso en libras (lb) a kilogramos (kg) aquí",
    },
    "weight_input_label": {
        "en": "Input weight here:",
        "es": "Introduce el peso aquí:",
    },
    "height_converter_label": {
        "en": "Convert height in feet (ft) into meters (m) here",
        "es": "Convierte la estatura en pies (ft) a metros (m) aquí",
    },
    "height_ft_input_label": {
        "en": "Input ft here:",
        "es": "Introduce pies aquí:",
    },
    "height_in_input_label": {
        "en": "Input inches here:",
        "es": "Introduce pulgadas aquí:",
    },
    "convert_button": {
        "en": "Convert",
        "es": "Convertir",
    },

    # BMI (inputs) -----------------------------------------------------
    "bmi_expander_label": {
        "en": "BMI (Body Mass Index)",
        "es": "IMC (Índice de Masa Corporal)",
    },
    "weight_input_kg_label": {
        "en": "Input your weight in **kilograms** here:",
        "es": "Introduce tu peso en **kilogramos** aquí:",
    },
    "height_input_m_label": {
        "en": "Input your height in **meters** here:",
        "es": "Introduce tu estatura en **metros** aquí:",
    },
    "calculate_button": {
        "en": "Calculate",
        "es": "Calcular",
    },
    "bmi_result_message": {
        "en": "Your BMI is {bmi}.",
        "es": "Tu IMC es {bmi}.",
    },
    "interpret_results_button": {
        "en": "Click to interpret your results!",
        "es": "¡Haz clic para interpretar tus resultados!",
    },

    # Blood-pressure (inputs) -----------------------------------------
    "blood_pressure_expander_label": {
        "en": "Blood Pressure",
        "es": "Presión Arterial",
    },
    "systolic_label": {
        "en": "Systolic (top number):",
        "es": "Sistólica (número superior):",
    },
    "diastolic_label": {
        "en": "Diastolic (bottom number):",
        "es": "Diastólica (número inferior):",
    },
    "save_button": {
        "en": "Save",
        "es": "Guardar",
    },
    "saved_toast": {
        "en": "Saved!",
        "es": "¡Guardado!",
    },

    # Blood-glucose (inputs) ------------------------------------------
    "blood_glucose_expander_label": {
        "en": "Blood Glucose",
        "es": "Glucosa en Sangre",
    },
    "blood_glucose_input_label": {
        "en": "Please enter blood glucose (mg/dL):",
        "es": "Por favor, introduce la glucosa en sangre (mg/dL):",
    },

    # Waist-to-height (inputs) ----------------------------------------
    "Waist Circumference": {
        "en": "Waist Circumference",
        "es": "Circunferencia de la cintura",
    },
    "Choose your Units:": {
        "en": "Choose your Units:",
        "es": "Elige tus unidades:",
    },
    "Waist (in)": {
        "en": "Waist (in)",
        "es": "Cintura (pulg)",
    },
    "Waist (cm)": {
        "en": "Waist (cm)",
        "es": "Cintura (cm)",
    },

    # ---------- PAGE HEADER --------------------------------------------------
    "results_title": {
        "en": "Results",
        "es": "Resultados",
    },
    "results_intro": {
        "en": "Use this page to interpret the results you inputted. Learn more about each category.",
        "es": "Usa esta página para interpretar los resultados que ingresaste. Conoce más sobre cada categoría.",
    },

    # ---------- BMI SECTION --------------------------------------------------
    "bmi_expander_label": {
        "en": "BMI",
        "es": "IMC",
    },
    "bmi_subheader": {
        "en": "Your calculated BMI is {bmi}",
        "es": "Tu IMC calculado es {bmi}",
    },
    "bmi_under_msg": {
        "en": "Your BMI is considered UNDERWEIGHT.",
        "es": "Tu IMC se considera BAJO PESO.",
    },
    "bmi_normal_msg": {
        "en": "Your BMI is considered NORMAL",
        "es": "Tu IMC se considera NORMAL",
    },
    "bmi_over_msg": {
        "en": "Your BMI is considered OVERWEIGHT",
        "es": "Tu IMC se considera SOBREPESO",
    },
    "bmi_ob1_msg": {
        "en": "Your BMI is considered Class I OBESE",
        "es": "Tu IMC se considera OBESIDAD Clase I",
    },
    "bmi_ob2_msg": {
        "en": "Your BMI is considered Class II OBESE",
        "es": "Tu IMC se considera OBESIDAD Clase II",
    },
    "bmi_ob3_msg": {
        "en": "Your BMI is considered Class III OBESE",
        "es": "Tu IMC se considera OBESIDAD Clase III",
    },
    "bmi_normal_range": {
        "en": "A normal BMI is between 18.5 and 25",
        "es": "Un IMC normal está entre 18.5 y 25",
    },

    # paragraphs (UNDERWEIGHT)
    "uw_para1": {
        "en": (
            "First off . . . Don't worry! Being underweight is not the end of the world. "
            "BMI is not the perfect health metric in all cases and should not be used as the sole number to determine "
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them. "
            "Let's look a little further into what might be causing your low BMI and what you could do to help."
        ),
        "es": (
            "Para empezar… no te preocupes. Tener bajo peso no es el fin del mundo. "
            "El IMC no es la métrica perfecta en todos los casos y no debería usarse como único indicador de salud. "
            "Hay muchas formas de medir el bienestar y el IMC es solo una de ellas. "
            "Veamos con más detalle qué podría estar causando tu IMC bajo y qué podrías hacer al respecto."
        ),
    },
    "uw_risk_intro": {
        "en": "First off, why is having a low BMI possibly dangerous? Well it increases your chances of:",
        "es": "Primero, ¿por qué puede ser peligroso tener un IMC bajo? Aumenta tus probabilidades de:",
    },
    "uw_risk_list": {   # bullet block kept as-is
        "en": (
            "- Osteoporosis\n"
            "- More sick frequently\n"
            "- Fatigue\n"
            "- Anemia\n"
            "- Irregular periods and premature births in women\n"
            "- Slow or impaired growth"
        ),
        "es": (
            "- Osteoporosis\n"
            "- Enfermar con más frecuencia\n"
            "- Fatiga\n"
            "- Anemia\n"
            "- Menstruaciones irregulares y partos prematuros en mujeres\n"
            "- Crecimiento lento o deteriorado"
        ),
    },
    "uw_causes_intro": {
        "en": "Common causes of low BMI include:",
        "es": "Las causas comunes de un IMC bajo incluyen:",
    },
    "uw_causes_list": {
        "en": (
            "- Family history\n"
            "- High metabolism\n"
            "- Frequent physical activity (frequent runner, athlete, etc.)\n"
            "- Potential physical illness or chronic diseases\n"
            "- Mental illness\n"
            "- Possible eating disorder (**Very important to see a doctor if you think you have this**)"
        ),
        "es": (
            "- Antecedentes familiares\n"
            "- Metabolismo acelerado\n"
            "- Actividad física frecuente (corredor habitual, atleta, etc.)\n"
            "- Enfermedades físicas o crónicas\n"
            "- Problemas de salud mental\n"
            "- Posible trastorno alimentario (**muy importante consultar al médico si lo sospechas**)"
        ),
    },
    "uw_actions_intro": {
        "en": (
            "Thankfully, being underweight is not uncommon. There are lots of "
            "easy, doable ways to help bring up your BMI! Some ways include:"
        ),
        "es": (
            "Por suerte, el bajo peso no es algo raro. Hay muchas formas sencillas "
            "de subir tu IMC. Algunas ideas son:"
        ),
    },
    "uw_actions_list": {
        "en": (
            "- High protein and whole-grain snacks (carbs! carbs! carbs!)\n"
            "    - Peanut butter crackers, protein bars, trail mix, pita chips with hummus, a handful of almonds\n"
            "- Eat several small meals a day as opposed to a set number of big meals\n"
            "- Add toppings or additional food to current meals\n"
            "    - Ex. adding nuts to yogurt, seeds to salad or soup, putting nut butter on whole-grain toast\n"
            "- Decreasing intense cardio workouts and shifting more towards weight-lifting"
        ),
        "es": (
            "- Tentempiés ricos en proteínas y cereales integrales (¡carbohidratos!)\n"
            "    - Galletas con mantequilla de cacahuete, barritas proteicas, trail mix, chips de pita con hummus, un puñado de almendras\n"
            "- Comer varias comidas pequeñas al día en lugar de pocas comidas grandes\n"
            "- Añadir toppings o comidas extra a tus platos actuales\n"
            "    - Ej.: frutos secos en el yogur, semillas en la ensalada o la sopa, crema de frutos secos sobre pan integral\n"
            "- Reducir el cardio intenso y pasar a más entrenamiento de fuerza"
        ),
    },
    "uw_closing": {
        "en": (
            "Finding out that you're underweight is a great start to figuring out what to do. Making changes to "
            "your diet and emphasizing weight training are good ways to start. At the end of the day, seeing your primary care "
            "physician or a dietitian will make fundamental differences in your journey. Take time to see a professional. "
            "Good luck on your journey!"
        ),
        "es": (
            "Descubrir que tienes bajo peso es un gran primer paso. Cambiar la alimentación y dar prioridad al entrenamiento "
            "de fuerza son buenos comienzos. Al final, tu médico de cabecera o una dietista marcarán la diferencia. "
            "Tómate el tiempo de acudir a un profesional. ¡Éxitos en tu camino!"
        ),
    },

    # paragraphs (OVERWEIGHT / OBESE)
    "ow_para1": {
        "en": (
            "First off . . . Don't worry! Being overweight is not the end of the world. "
            "BMI is not the perfect health metric in all cases and should not be used as the sole number to determine "
            "if you are healthy or not. There are lots of things that can track health, and BMI is just one of them. "
            "Let's look a little further into what might be causing your high BMI and what you could do to help."
        ),
        "es": (
            "Para empezar… no te preocupes. Tener sobrepeso no es el fin del mundo. "
            "El IMC no es la métrica perfecta en todos los casos y no debería usarse como único indicador de salud. "
            "Hay muchas formas de medir el bienestar y el IMC es solo una de ellas. "
            "Veamos qué podría estar causando tu IMC alto y qué podrías hacer al respecto."
        ),
    },
    "ow_risk_intro": {
        "en": "First off, why is having a high BMI possibly dangerous? Well it increases your chances of:",
        "es": "Primero, ¿por qué puede ser peligroso tener un IMC alto? Aumenta tus probabilidades de:",
    },
    "ow_risk_list": {
        "en": (
            "- Heart Disease\n"
            "- Type II diabetes\n"
            "- High Blood Pressure\n"
            "- Certain cancers\n"
            "- Liver Disease\n"
            "- Breathing/Respiratory Issues\n"
            "- Fertility Problems\n"
            "- Mental Health Issues"
        ),
        "es": (
            "- Enfermedad cardíaca\n"
            "- Diabetes tipo II\n"
            "- Hipertensión arterial\n"
            "- Ciertos cánceres\n"
            "- Enfermedad hepática\n"
            "- Problemas respiratorios\n"
            "- Problemas de fertilidad\n"
            "- Problemas de salud mental"
        ),
    },
    "ow_causes_intro": {
        "en": "Common causes of high BMI include:",
        "es": "Las causas comunes de un IMC alto incluyen:",
    },
    "ow_causes_list": {
        "en": (
            "- Lack of physical activity\n"
            "    - Adults need 150 min of aerobic activity a week, Children need 60 minutes each day\n"
            "    - Muscle-strengthening activities (like lifting weights) are recommended for major muscle groups 2 or more days each week\n"
            "- Calorie excess (eating too many calories)\n"
            "    - 2000 calories is recommended per day. Anything above may be dangerous\n"
            "- Too much saturated fat\n"
            "    - For a 2000 calorie day, no more than about 22 g of saturated fats\n"
            "- Eating foods high in added sugar\n"
            "- Bad-quality sleep\n"
            "    - Consistently getting less than 7 hours of sleep is considered below recommended\n"
            "- Stress\n"
            "- Specific medical conditions (please see a doctor to determine this)\n"
            "- Genetics\n"
            "- Medications"
        ),
        "es": (
            "- Falta de actividad física\n"
            "    - Los adultos necesitan 150 min de actividad aeróbica por semana; los niños, 60 min diarios\n"
            "    - Se recomiendan ejercicios de fuerza (por ejemplo, levantar pesas) para los principales grupos musculares 2 o más días por semana\n"
            "- Exceso de calorías (comer demasiadas)\n"
            "    - Se recomiendan 2000 calorías al día; más podría ser perjudicial\n"
            "- Demasiada grasa saturada\n"
            "    - En una dieta de 2000 calorías, no más de unos 22 g de grasas saturadas\n"
            "- Consumir alimentos ricos en azúcares añadidos\n"
            "- Sueño de mala calidad\n"
            "    - Dormir menos de 7 horas de forma constante se considera insuficiente\n"
            "- Estrés\n"
            "- Ciertas afecciones médicas (consulta al médico)\n"
            "- Genética\n"
            "- Medicamentos"
        ),
    },
    "ow_actions_intro": {
        "en": (
            "Thankfully, being overweight is not uncommon. There are lots of "
            "easy, doable ways to help bring down your BMI! Some ways include:"
        ),
        "es": (
            "Por suerte, el sobrepeso no es raro. Hay muchas formas sencillas "
            "de bajar tu IMC. Algunas ideas son:"
        ),
    },
    "ow_actions_list": {
        "en": (
            "- Physical activity\n"
            "    - Start playing a sport\n"
            "    - Go on walks a few times a week (10 minutes is better than nothing)\n"
            "    - Find long-form content you can watch/listen to while exercising or walking\n"
            "    - Get a workout buddy\n"
            "    - Start going to the gym (or start going more consistently/more frequently)\n"
            "- Start tracking calories using online applications (mobile applications are best)\n"
            "- Eat healthier (more fruits and vegetables, heart healthy meals)\n"
            "- Medication\n"
            "- Surgery (last solution to consider. Need to see a doctor)"
        ),
        "es": (
            "- Actividad física\n"
            "    - Empieza a practicar un deporte\n"
            "    - Sal a caminar varias veces por semana (10 min son mejor que nada)\n"
            "    - Busca contenido largo para ver o escuchar mientras te ejercitas o caminas\n"
            "    - Consigue un compañero de entrenamiento\n"
            "    - Empieza a ir al gimnasio (o ve con más constancia/frecuencia)\n"
            "- Controla las calorías con apps (las móviles son ideales)\n"
            "- Come más sano (más frutas y verduras, comidas cardioprotectoras)\n"
            "- Medicación\n"
            "- Cirugía (último recurso; consulta con un médico)"
        ),
    },
    "ow_closing": {
        "en": (
            "Finding out that you're overweight is a great start to figuring out what to do. Making changes to "
            "your diet and emphasizing exercise are good ways to start. At the end of the day, seeing your primary care "
            "physician or a dietitian will make fundamental differences in your journey. Take time to see a professional. "
            "Good luck on your journey!"
        ),
        "es": (
            "Descubrir que tienes sobrepeso es un gran primer paso. Cambiar la alimentación y dar prioridad al ejercicio "
            "son buenos comienzos. Al final, tu médico de cabecera o una dietista marcarán la diferencia. "
            "Tómate el tiempo de acudir a un profesional. ¡Éxitos en tu camino!"
        ),
    },

    # ---------- BLOOD PRESSURE SECTION --------------------------------------
    "bp_expander_label": {
        "en": "Blood Pressure",
        "es": "Presión Arterial",
    },
    "bp_subheader": {
        "en": "Your blood pressure is {bp}",
        "es": "Tu presión arterial es {bp}",
    },
    "bp_low_msg": {
        "en": "Your blood pressure is LOW",
        "es": "Tu presión arterial es BAJA",
    },
    "bp_normal_msg": {
        "en": "Your blood pressure is normal",
        "es": "Tu presión arterial es normal",
    },
    "bp_elevated_msg": {
        "en": "Your blood pressure is ELEVATED",
        "es": "Tu presión arterial está ELEVADA",
    },
    "bp_stage1_msg": {
        "en": "Your blood pressure shows that you are in STAGE 1 HYPERTENSION",
        "es": "Tu presión arterial indica que estás en HIPERTENSIÓN ETAPA 1",
    },
    "bp_stage2_msg": {
        "en": "Your blood pressure shows that you are in STAGE 2 HYPERTENSION",
        "es": "Tu presión arterial indica que estás en HIPERTENSIÓN ETAPA 2",
    },
    "bp_crisis_msg": {
        "en": "HYPERTENSIVE CRISIS: PLEASE CONSULT A DOCTOR IMMEDIATELY",
        "es": "CRISIS HIPERTENSIVA: CONSULTA A UN MÉDICO INMEDIATAMENTE",
    },
    "bp_iso_sys_msg": {
        "en": "Isolated Systolic Hypertension",
        "es": "Hipertensión Sistólica Aislada",
    },
    "bp_iso_dia_msg": {
        "en": "Isolated Diastolic Hypertension",
        "es": "Hipertensión Diastólica Aislada",
    },
    "bp_normal_range": {
        "en": "A normal blood pressure is between 90/60 and 120/80",
        "es": "Una presión arterial normal está entre 90/60 y 120/80",
    },

    # LOW-BP detail lines
    "lowbp_symptoms_intro": {
        "en": "Having a consistently low blood pressure can be dangerous. You might be experiencing some of these symptoms:",
        "es": "Tener la presión arterial constantemente baja puede ser peligroso. Podrías experimentar estos síntomas:",
    },
    "lowbp_symptoms_list": {
        "en": (
            "- Blurred or fading vision\n"
            "- Dizzy or lightheaded feelings\n"
            "- Fainting\n"
            "- Fatigue\n"
            "- Trouble concentrating\n"
            "- Upset stomach"
        ),
        "es": (
            "- Visión borrosa o desvanecida\n"
            "- Mareos o sensación de aturdimiento\n"
            "- Desmayos\n"
            "- Fatiga\n"
            "- Dificultad para concentrarse\n"
            "- Malestar estomacal"
        ),
    },
    "lowbp_causes_intro": {
        "en": "So what might be causing such a low blood pressure? A few things may be:",
        "es": "¿Qué podría causar una presión arterial tan baja? Algunas posibilidades son:",
    },
    "lowbp_causes_list": {
        "en": (
            "- Pregnancy\n"
            "- Heart and heart valve conditions\n"
            "- Hormone-related issues\n"
            "- Dehydration (very common)\n"
            "- Blood loss\n"
            "- Severe infection\n"
            "- Severe allergic reaction (anaphylaxis)\n"
            "- Lack of essential nutrients in diet\n"
            "- Medications"
        ),
        "es": (
            "- Embarazo\n"
            "- Problemas cardíacos y de las válvulas del corazón\n"
            "- Problemas hormonales\n"
            "- Deshidratación (muy común)\n"
            "- Pérdida de sangre\n"
            "- Infección grave\n"
            "- Reacción alérgica grave (anafilaxia)\n"
            "- Falta de nutrientes esenciales en la dieta\n"
            "- Medicamentos"
        ),
    },
    "lowbp_treat_intro": {
        "en": "A few ways this can be treated are:",
        "es": "Algunas formas de tratarlo son:",
    },
    "lowbp_treat_list": {
        "en": (
            "- Use more salt\n"
            "    - Salt helps raise blood pressure, but too much is dangerous. Talk to a doctor to determine amount\n"
            "- Drink more water\n"
            "- Wear compression stockings\n"
            "    - Relieve pain and swelling in legs from varicose veins (if applicable)\n"
            "- Medicines\n"
            "    - Consult your doctor for medication recommendations\n"
            "    - Midodrine (Orvaten) is a common medicine that could be prescribed"
        ),
        "es": (
            "- Consumir más sal\n"
            "    - La sal ayuda a subir la presión, pero en exceso es peligrosa. Consulta con un médico la cantidad adecuada\n"
            "- Beber más agua\n"
            "- Usar medias de compresión\n"
            "    - Alivian dolor e hinchazón en las piernas por varices (si aplica)\n"
            "- Medicamentos\n"
            "    - Consulta a tu médico sobre qué fármacos usar\n"
            "    - Midodrina (Orvaten) es un medicamento común que podría recetarse"
        ),
    },

    # ELEVATED-BP lines
    "elevated_para": {
        "en": (
            "Your blood pressure is a little elevated. Not to worry however, because this is completely normal. "
            "It's not uncommon to see a slightly elevated blood pressure. Elevated blood pressure can creep up over time though, "
            "raising your chances of heart failure, stroke, and other serious health problems. "
            "The upside is you’ve spotted it now, so you can start making steady changes to bring those numbers back into a healthy range."
        ),
        "es": (
            "Tu presión está un poco elevada. No te preocupes: es algo bastante común. "
            "Sin embargo, puede aumentar con el tiempo y elevar el riesgo de insuficiencia cardíaca, ictus y otros problemas graves. "
            "La ventaja es que lo has detectado ahora, de modo que puedes empezar a hacer cambios constantes para volver a un rango saludable."
        ),
    },
    "elevated_steps_intro": {
        "en": "Some ways to lower your blood pressure:",
        "es": "Algunas formas de reducir tu presión arterial:",
    },
    "elevated_steps_list": {
        "en": (
            "- Healthier diet\n"
            "    - Removing excess fats and salts\n"
            "- Exercise more frequently\n"
            "- Limit alcohol and smoking\n"
            "- Find ways to lower stress in your life"
        ),
        "es": (
            "- Dieta más saludable\n"
            "    - Reducir grasas y sal\n"
            "- Hacer ejercicio con más frecuencia\n"
            "- Limitar el alcohol y el tabaco\n"
            "- Buscar maneras de reducir el estrés"
        ),
    },
    "elevated_closing": {
        "en": (
            "You are in a good spot. Knowing that your blood pressure is elevated before it gets into hypertensive levels "
            "helps give you time to lower it naturally without serious medical intervention. Focusing on a heart-healthy diet, exercising "
            "regularly, and tracking your blood pressure at home should be goals now. Good luck!"
        ),
        "es": (
            "Estás en buen momento. Saber que tu presión está elevada antes de llegar a niveles hipertensivos "
            "te da tiempo de bajarla de forma natural y sin intervenciones médicas importantes. "
            "Concéntrate en una dieta cardiosaludable, ejercicio regular y control en casa. ¡Éxitos!"
        ),
    },

    # HIGH-BP helper blocks
    "highbp_intro": {
        "en": "Your blood pressure is quite high and needs to be lowered. Let's look at some of the main causes of a high blood pressure:",
        "es": "Tu presión arterial es bastante alta y debe reducirse. Veamos algunas de las principales causas:",
    },
    "highbp_causes_list": {
        "en": (
            "- **Primary hypertension**: No identifiable cause. A general increase over the years due to gradual buildup of plaque in the arteries. Expected with age\n"
            "- **Secondary hypertension**: There is some sort of underlying condition\n"
            "    - Adrenal gland tumors\n"
            "    - Blood vessel problems present at birth (ex. congenital heart defects)\n"
            "    - Cough and cold medicines, pain relievers, birth control pills, or other prescription drugs\n"
            "    - Illegal drugs (ex. amphetamines)\n"
            "    - Kidney disease\n"
            "    - Obstructive sleep apnea\n"
            "    - Thyroid problems\n"
            "- **White coat hypertension**: A high blood pressure that only occurs in clinical settings (ex. doctors offices). This is "
            "usually caused by the stress of going to a doctor, and not something health-related."
        ),
        "es": (
            "- **Hipertensión primaria**: Sin causa identificable. Aumento general con los años por acumulación de placa en las arterias; se espera con la edad.\n"
            "- **Hipertensión secundaria**: Hay una afección subyacente\n"
            "    - Tumores de las glándulas suprarrenales\n"
            "    - Problemas vasculares congénitos (p. ej., cardiopatías congénitas)\n"
            "    - Medicamentos para el resfriado, analgésicos, anticonceptivos u otros fármacos\n"
            "    - Drogas ilegales (p. ej., anfetaminas)\n"
            "    - Enfermedad renal\n"
            "    - Apnea obstructiva del sueño\n"
            "    - Problemas de tiroides\n"
            "- **Hipertensión de bata blanca**: Presión alta que solo aparece en consultas médicas, "
            "usualmente causada por el estrés de la visita y no por un problema de salud."
        ),
    },
    "highbp_complications_intro": {
        "en": "If left untreated, high blood pressure can possibly lead to:",
        "es": "Si no se trata, la hipertensión puede derivar en:",
    },
    "highbp_complications_list": {
        "en": (
            "- Heart problems\n"
            "- Aneurysm\n"
            "- Kidney problems\n"
            "- Metabolic syndrome\n"
            "- Dementia\n"
            "- Changes in memory or understanding"
        ),
        "es": (
            "- Problemas cardíacos\n"
            "- Aneurisma\n"
            "- Problemas renales\n"
            "- Síndrome metabólico\n"
            "- Demencia\n"
            "- Cambios en la memoria o el entendimiento"
        ),
    },
    "highbp_risk_intro": {
        "en": "Some things that can increase your risk of having high blood pressure include:",
        "es": "Factores que pueden aumentar tu riesgo de hipertensión:",
    },
    "highbp_risk_list": {
        "en": (
            "- Age\n"
            "- Sex (more common in men)\n"
            "- Family history\n"
            "- Race (most common in African Americans)\n"
            "- Obesity or being overweight\n"
            "- Lack of exercise\n"
            "- Tobacco use or vaping\n"
            "- Too much salt\n"
            "- Low potassium\n"
            "- Too much alcohol\n"
            "- Stress\n"
            "- Pregnancy"
        ),
        "es": (
            "- Edad\n"
            "- Sexo (más común en hombres)\n"
            "- Antecedentes familiares\n"
            "- Raza (más común en afroamericanos)\n"
            "- Obesidad o sobrepeso\n"
            "- Falta de ejercicio\n"
            "- Consumo de tabaco o vapeo\n"
            "- Demasiada sal\n"
            "- Poco potasio\n"
            "- Exceso de alcohol\n"
            "- Estrés\n"
            "- Embarazo"
        ),
    },

    "stage1_para": {
        "en": (
            "There is such thing as Stage II hypertension as well. Right now, you are in Stage I. This means "
            "that your blood pressure can be controlled with a change in lifestyle and that you are not in immediate "
            "need of medication. Once your hypertension goes past a certain point, you will be recommended medication to help control it. As such, "
            "please take precaution and continue to care for your blood pressure."
        ),
        "es": (
            "También existe la hipertensión de etapa II. Por ahora estás en la etapa I, lo que significa que "
            "puede controlarse con cambios de estilo de vida y no necesitas medicación inmediata. "
            "Si la presión sigue subiendo, te recomendarán medicamentos para controlarla. "
            "Toma precauciones y sigue cuidando tu presión."
        ),
    },
    "stage2_para": {
        "en": (
            "As someone in Stage II Hypertension, it is important to note that you need to see a healthcare professional "
            "immediately to help control your blood pressure. Your provider will most likely help you by providing prescription "
            "medications. With increased exercise, a controlled diet, and some medicine, hopefully you can lower your blood "
            "pressure back to a safe range."
        ),
        "es": (
            "Si tienes hipertensión de etapa II, es esencial acudir a un profesional de salud de inmediato para controlar la presión. "
            "Lo más probable es que te receten medicamentos. Con más ejercicio, dieta controlada y fármacos, "
            "esperamos que puedas volver a un rango seguro."
        ),
    },
    "crisis_para": {
        "en": "Your blood pressure is dangerously high. Please see a healthcare professional immediately!",
        "es": "Tu presión arterial es peligrosamente alta. ¡Consulta a un profesional de salud de inmediato!",
    },

    # ---------- PLACEHOLDERS / FALLBACKS ------------------------------------
    "no_bmi_input": {
        "en": "***No BMI Input***",
        "es": "***Sin entrada de IMC***",
    },
    "no_bp_input": {
        "en": "***No Blood Pressure input***",
        "es": "***Sin entrada de presión arterial***",
    },
    "bg_placeholder": {
        "en": "Blood Glucose",
        "es": "Glucosa en sangre",
    },
    "no_bg_input": {
        "en": "***No Blood Glucose input***",
        "es": "***Sin entrada de glucosa en sangre***",
    },
    "waist_ratio_placeholder": {
        "en": "Waist Ratio",
        "es": "Relación cintura-altura",
    },
    "no_waist_input": {
        "en": "***No Waist Ratio input***",
        "es": "***Sin entrada de relación cintura-altura***",
    },


    # --Blood Sugar---------------------------------------------
    "bg_placeholder": {
        "en": "Blood Glucose",
        "es": "Glucosa en sangre",
    },
    "bg_subheader": {
        "en": "Your blood glucose is {bg}",
        "es": "Tu glucosa en sangre es {bg}",
    },
    "bg_normal_range": {
        "en": "A normal blood sugar is between 70 to 99 mg/dL",
        "es": "Una glucemia normal está entre 70 y 99 mg/dL",
    },

    # --- Status messages ---------------------------------------
    "bg_low_msg":   {"en": "Your blood sugar is LOW",                                            "es": "Tu glucemia está BAJA"},
    "bg_normal_msg":{"en": "Your blood sugar is normal",                                         "es": "Tu glucemia es normal"},
    "bg_pre_msg":   {"en": "Your blood sugar shows that you are PRE-DIABETIC",                   "es": "Tu glucemia indica que eres PREDIABÉTICO/A"},
    "bg_diab_msg":  {"en": "Your blood sugar shows that you are DIABETIC",                       "es": "Tu glucemia indica que eres DIABÉTICO/A"},

    # --- LOW BG ------------------------------------------------
    "bg_low_para1": {
        "en": "A low blood sugar can be dangerous. If you have low blood glucose, you may experience:",
        "es": "Una glucemia baja puede ser peligrosa. Si tienes la glucosa baja, puedes experimentar:",
    },
    "bg_low_symptoms": {
        "en": (
            "- Feeling shaky\n"
            "- Being nervous or anxious\n"
            "- Sweating, chills, and clamminess\n"
            "- Irritability or impatience\n"
            "- Confusion\n"
            "- Fast heartbeat\n"
            "- Feeling lightheaded or dizzy\n"
            "- Hunger\n"
            "- Nausea\n"
            "- Color draining from the skin (pallor)\n"
            "- Feeling sleepy\n"
            "- Feeling weak or having no energy\n"
            "- Blurred/impaired vision\n"
            "- Tingling or numbness in the lips, tongue, or cheeks\n"
            "- Headaches\n"
            "- Coordination problems or clumsiness\n"
            "- Nightmares or crying out during sleep"
        ),
        "es": (
            "- Temblor\n"
            "- Nerviosismo o ansiedad\n"
            "- Sudoración, escalofríos y piel húmeda\n"
            "- Irritabilidad o impaciencia\n"
            "- Confusión\n"
            "- Latido cardíaco rápido\n"
            "- Mareo o sensación de desmayo\n"
            "- Hambre\n"
            "- Náuseas\n"
            "- Palidez\n"
            "- Somnolencia\n"
            "- Debilidad o falta de energía\n"
            "- Visión borrosa o alterada\n"
            "- Hormigueo o entumecimiento en labios, lengua o mejillas\n"
            "- Dolor de cabeza\n"
            "- Problemas de coordinación o torpeza\n"
            "- Pesadillas o gritos durante el sueño"
        ),
    },
    "bg_low_causes_intro": {
        "en": "You might wonder why your blood sugar is lower than normal. Here are a few reasons why it might be:",
        "es": "Quizás te preguntes por qué tu glucemia está por debajo de lo normal. Estas pueden ser algunas razones:",
    },
    "bg_low_causes": {
        "en": (
            "- Diabetes\n"
            "- Issues with adrenal glands\n"
            "- Pancreas problems\n"
            "- Hyperthyroidism\n"
            "- Significant stress (trauma or surgery)\n"
            "- Certain medications, especially corticosteroids"
        ),
        "es": (
            "- Diabetes\n"
            "- Problemas en las glándulas suprarrenales\n"
            "- Problemas del páncreas\n"
            "- Hipertiroidismo\n"
            "- Estrés significativo (trauma o cirugía)\n"
            "- Ciertos medicamentos, especialmente corticosteroides"
        ),
    },
    "bg_low_treat_intro": {
        "en": (
            "Now that you are aware of your low blood sugar, beginning treatment for it is necessary. "
            "Untreated low blood sugar is very dangerous and can lead to a variety of other problematic health issues. "
            "So what can you do to treat it?:"
        ),
        "es": (
            "Ahora que sabes que tu glucemia está baja, es necesario iniciar el tratamiento. "
            "La hipoglucemia sin tratar es muy peligrosa y puede causar otros problemas de salud. "
            "¿Qué puedes hacer para tratarla?:"
        ),
    },
    "bg_low_treat": {
        "en": (
            "- 15/15 rule – 15 g of fast acting carbs every 15 minutes to treat low blood sugar\n"
            "    - Fast acting carbs include: glucose tablets, glucose gel tube, ½ cup (4 ounces) of juice or regular soda, 1 tablespoon of sugar or corn syrup, or honey, hard candy, jellybeans\n"
            "    - note: Foods like chocolate or peanut butter are NOT the best choice\n"
            "- Consult a doctor (they may prescribe medications or give injectable glucagon)"
        ),
        "es": (
            "- Regla 15/15 – 15 g de carbohidratos de acción rápida cada 15 minutos\n"
            "    - Carbohidratos de acción rápida: tabletas de glucosa, gel de glucosa, ½ taza (120 ml) de zumo o refresco normal, 1 cda de azúcar o jarabe de maíz, miel, caramelos duros, gomitas\n"
            "    - nota: Alimentos como el chocolate o la mantequilla de cacahuate NO son la mejor opción\n"
            "- Consultar al médico (puede recetar medicamentos o glucagón inyectable)"
        ),
    },
    "bg_low_close": {
        "en": (
            "Low blood sugar is very common among diabetics. Ask your doctor to find more ways to manage low blood sugar. "
            "It is good practice to keep a blood sugar monitor with you at home to track your blood sugar. Eating a healthy, carb-loaded diet and "
            "possibly taking medication are both common ways of managing low blood sugar. Be patient with yourself, talk to your healthcare provider, "
            "and follow a treatment plan to help hopefully bring your blood sugar back up."
        ),
        "es": (
            "La hipoglucemia es muy común en personas con diabetes. Pide a tu médico más consejos para controlarla. "
            "Es buena práctica contar con un medidor de glucosa en casa para registrar tu glucemia. Seguir una dieta saludable rica en carbohidratos y, "
            "si es necesario, tomar medicación son formas habituales de manejarla. Sé paciente, habla con tu profesional de salud "
            "y cumple un plan de tratamiento para volver a subir tu glucosa."
        ),
    },

    # --- PREDIABETES -----------------------------------------------------
    "bg_pre_para1": {
        "en": (
            "A slightly elevated blood sugar like yours indicates that you are on the path to being diabetic. Currently, your "
            "blood sugar is within a range that can hopefully be brought down with lifestyle changes and minimal medical intervention. Let's "
            "first look at what some common symptoms are for pre-diabetes."
        ),
        "es": (
            "Una glucemia ligeramente elevada como la tuya indica que vas camino a la diabetes. Actualmente tu glucosa está en un rango "
            "que, con suerte, puede reducirse mediante cambios de estilo de vida y mínima intervención médica. Primero veamos algunos síntomas "
            "comunes de la prediabetes."
        ),
    },
    "bg_pre_symptom_note": {
        "en": (
            "Prediabetes actually doesn't usually have any signs or symptoms associated with it. "
            "However, one possible sign is darkened skin on certain parts of the body. Affected areas can include the neck, armpits and groin."
        ),
        "es": (
            "En realidad, la prediabetes no suele presentar signos ni síntomas. "
            "No obstante, un posible indicio es el oscurecimiento de la piel en ciertas partes del cuerpo, como el cuello, las axilas y la ingle."
        ),
    },
    "bg_pre_causes_intro": {
        "en": "Some common causes of pre-diabetes include:",
        "es": "Algunas causas comunes de la prediabetes incluyen:",
    },
    "bg_pre_causes": {
        "en": (
            "- Issue with insulin in your body\n"
            "- Family history and genetics play an important role"
        ),
        "es": (
            "- Problemas con la insulina en tu cuerpo\n"
            "- Los antecedentes familiares y la genética desempeñan un papel importante"
        ),
    },
    "bg_pre_treat_intro": {
        "en": "What are some good ways to treat pre-diabetes? Here are a few:",
        "es": "¿Cuáles son algunas buenas formas de tratar la prediabetes? Aquí tienes unas cuantas:",
    },
    "bg_pre_treat": {
        "en": (
            "- Eating healthy foods\n"
            "- Getting active\n"
            "- Losing excess weight\n"
            "- Controlling your blood pressure and cholesterol\n"
            "- Not smoking"
        ),
        "es": (
            "- Comer alimentos saludables\n"
            "- Mantenerte activo/a\n"
            "- Perder el exceso de peso\n"
            "- Controlar la presión arterial y el colesterol\n"
            "- No fumar"
        ),
    },
    "bg_pre_close": {
        "en": (
            "It is important to recognize that being pre-diabetic is something that can be managed with pure lifestyle changes. "
            "Making changes to your diet, improving physical activity, and consulting a doctor for management are all great ways to prevent "
            "your blood sugar from increasing into diabetic ranges."
        ),
        "es": (
            "Es importante reconocer que la prediabetes puede controlarse con cambios de estilo de vida. "
            "Mejorar la dieta, aumentar la actividad física y consultar a un médico son formas excelentes de evitar "
            "que la glucosa suba a niveles de diabetes."
        ),
    },

    # --- DIABETES --------------------------------------------------------
    "bg_diab_para1": {
        "en": (
            "Your blood sugar is high enough that you are considered a diabetic. Not to worry however. Diabetes is "
            "something that has been studied and treated for decades. This means there are plenty of resources (including your "
            "primary care physician) that can help you manage your blood sugar and help you live a healthy life. First, let's start with "
            "some common symptoms that you might be experiencing as a result of your high blood sugar:"
        ),
        "es": (
            "Tu glucemia es lo bastante alta para considerarse diabetes. Sin embargo, no te preocupes. La diabetes es "
            "una enfermedad estudiada y tratada desde hace décadas. Esto significa que existen muchos recursos (incluido tu médico de cabecera) "
            "que pueden ayudarte a controlar tu glucosa y vivir saludablemente. Primero, repasemos algunos síntomas comunes que podrías experimentar "
            "debido a tu glucosa alta:"
        ),
    },
    "bg_diab_symptoms": {
        "en": (
            "- Urinating large amounts\n"
            "- Excessive thirst\n"
            "- Feeling tired\n"
            "- Frequent hunger\n"
            "- Dry mouth\n"
            "- Weight loss\n"
            "- Blurred vision\n"
            "- Recurrent infections (e.g., urinary infections, skin infections)\n"
            "- Wounds (cuts, scrapes) that heal slowly"
        ),
        "es": (
            "- Orinar grandes cantidades\n"
            "- Sed excesiva\n"
            "- Cansancio\n"
            "- Hambre frecuente\n"
            "- Boca seca\n"
            "- Pérdida de peso\n"
            "- Visión borrosa\n"
            "- Infecciones recurrentes (urinarias, cutáneas)\n"
            "- Heridas (cortes, raspones) que cicatrizan lentamente"
        ),
    },
    "bg_diab_causes_intro": {
        "en": "Experiencing any of the above symptoms is totally normal. So now let's get into what might be causing your blood sugar to stay at such high levels. Here are a few common causes:",
        "es": "Experimentar cualquiera de los síntomas anteriores es totalmente normal. Ahora veamos por qué tu glucemia puede mantenerse tan alta. Algunas causas comunes son:",
    },
    "bg_diab_causes": {
        "en": (
            "- Eating too many carbohydrates\n"
            "- Not exercising enough\n"
            "- Not taking enough insulin medication (for type 1 diabetes) or other medications that regulate blood glucose levels\n"
            "- Medications such as corticosteroids, thiazide diuretics, beta-blockers, and antipsychotics\n"
            "- Certain conditions that affect the pancreas, which produces insulin\n"
            "- Medical conditions that can cause insulin resistance, such as Cushing’s syndrome and acromegaly\n"
            "- Pregnancy\n"
            "- Stress"
        ),
        "es": (
            "- Consumir demasiados carbohidratos\n"
            "- Hacer poco ejercicio\n"
            "- No usar suficiente insulina (diabetes tipo 1) u otros fármacos que regulan la glucosa\n"
            "- Medicamentos como corticosteroides, diuréticos tiazídicos, beta-bloqueantes y antipsicóticos\n"
            "- Afecciones que afectan al páncreas, productor de insulina\n"
            "- Enfermedades que causan resistencia a la insulina, como el síndrome de Cushing y la acromegalia\n"
            "- Embarazo\n"
            "- Estrés"
        ),
    },
    "bg_diab_treat_intro": {
        "en": "Now that you are aware of your high blood sugar, let's get to some treatment options that you have at your disposal:",
        "es": "Ahora que sabes que tu glucemia está alta, veamos algunas opciones de tratamiento a tu alcance:",
    },
    "bg_diab_treat": {
        "en": (
            "- Insulin\n"
            "    - For people with type 1 diabetes, insulin is the main treatment for hyperglycemia. In some cases, it may also be used to treat people with type 2 diabetes.\n"
            "- Glucose-lowering medications\n"
            "    - Various drugs such as metformin may be used to lower blood glucose levels.\n"
            "- Glucose monitoring\n"
            "    - People with diabetes should monitor their blood glucose levels as instructed by their doctor.\n"
            "- Lifestyle changes\n"
            "    - People with diabetes can reduce the risk of developing hyperglycemia or treat existing hyperglycemia by getting regular exercise, following a nutritious diet, and maintaining a healthy weight."
        ),
        "es": (
            "- Insulina\n"
            "    - Para personas con diabetes tipo 1, la insulina es el tratamiento principal. En algunos casos también se usa en tipo 2.\n"
            "- Medicamentos reductores de glucosa\n"
            "    - Varios fármacos, como la metformina, pueden bajar la glucosa.\n"
            "- Monitoreo de glucosa\n"
            "    - Las personas con diabetes deben medir su glucemia según indique el médico.\n"
            "- Cambios de estilo de vida\n"
            "    - El ejercicio regular, una dieta nutritiva y mantener un peso saludable ayudan a prevenir o tratar la hiperglucemia."
        ),
    },
    "bg_diab_close": {
        "en": (
            "Diabetes is a common condition across the world. Don't feel alone in your diagnosis. Always be sure that you are using "
            "an approved blood sugar monitor to track your blood sugar and keep in contact with your healthcare provider to help manage your "
            "symptoms. Having diabetes doesn't mean your life is forever changed. Lots of diabetics live normal, happy lives while being "
            "able to maintain their blood sugar. The most important step in your treatment is seeing a doctor and putting together a plan "
            "that works with your life. Personalized treatment plans are the hallmark of effective diabetes treatment."
        ),
        "es": (
            "La diabetes es una enfermedad común en todo el mundo. No te sientas solo/a. Asegúrate de usar un medidor aprobado para controlar "
            "tu glucosa y mantente en contacto con tu profesional de salud para manejar los síntomas. Tener diabetes no significa que tu vida "
            "cambie para siempre. Muchas personas con diabetes llevan vidas normales y felices mientras controlan su glucemia. "
            "El paso más importante es acudir al médico y elaborar un plan que se adapte a tu vida. Los planes personalizados son la base de un "
            "tratamiento eficaz."
        ),
    },

    }