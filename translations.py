import streamlit as st

T = {
    # --- Home Page ------------------------------------------
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
            "constituye asesoramiento médico. Consulte a un profesional de la "
            "salud para obtener orientación personalizada."
        ),
    },

    # --- Inputs Page --------------------------------------------------------
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

    # Converters
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
    # BMI section
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
    # Blood Pressure section
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
    # Blood Glucose section
    "blood_glucose_expander_label": {
        "en": "Blood Glucose",
        "es": "Glucosa en Sangre",
    },
    "blood_glucose_input_label": {
        "en": "Please enter blood glucose (mg/dL):",
        "es": "Por favor, introduce la glucosa en sangre (mg/dL):",
    },
    # Waist to Height Ratio section 
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
}