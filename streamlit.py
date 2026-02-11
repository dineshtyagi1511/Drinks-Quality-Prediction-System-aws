import streamlit as st
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline

# Page title
st.title("🍷 Drinks Quality Prediction System")

st.write("Enter the drink properties below to predict quality.")

# Input fields
fixed_acidity = st.number_input("Fixed Acidity", value=0.0)
volatile_acidity = st.number_input("Volatile Acidity", value=0.0)
citric_acid = st.number_input("Citric Acid", value=0.0)
residual_sugar = st.number_input("Residual Sugar", value=0.0)
chlorides = st.number_input("Chlorides", value=0.0)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=0.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=0.0)
density = st.number_input("Density", value=0.0)
pH = st.number_input("pH", value=0.0)
sulphates = st.number_input("Sulphates", value=0.0)
alcohol = st.number_input("Alcohol", value=0.0)

# Predict button
if st.button("Predict Quality"):

    try:
        data = [
            fixed_acidity, volatile_acidity, citric_acid,
            residual_sugar, chlorides, free_sulfur_dioxide,
            total_sulfur_dioxide, density, pH,
            sulphates, alcohol
        ]

        data = np.array(data).reshape(1, 11)

        obj = PredictionPipeline()
        prediction = obj.prediction(data)

        st.success(f"Predicted Quality: {prediction}")

    except Exception as e:
        st.error(f"Error: {e}")
