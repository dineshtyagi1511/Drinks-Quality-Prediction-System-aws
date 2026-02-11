import streamlit as st
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Drinks Quality Predictor",
    page_icon="🍷",
    layout="wide"
)

# ---------------- SIMPLE SOFT CSS ----------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #eef2f3, #ffffff);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.06);
    }

    .result-card {
        background-color: #f0f9ff;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: 600;
        color: #1f2937;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    }

    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #357abd;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center; color:#2c3e50;'>🍷 Drinks Quality Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:gray;'>Predict beverage quality based on chemical properties</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT + RESULT LAYOUT ----------------
col1, col2 = st.columns([2, 1])

# ================= INPUT SECTION =================
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔢 Enter Drink Properties")

    # Two columns for inputs
    input_col1, input_col2 = st.columns(2)

    with input_col1:
        fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
        volatile_acidity = st.number_input("Volatile Acidity", value=0.7)
        citric_acid = st.number_input("Citric Acid", value=0.0)
        residual_sugar = st.number_input("Residual Sugar", value=1.9)
        chlorides = st.number_input("Chlorides", value=0.076)
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0)

    with input_col2:
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0)
        density = st.number_input("Density", value=0.9978)
        pH = st.number_input("pH", value=3.51)
        sulphates = st.number_input("Sulphates", value=0.56)
        alcohol = st.number_input("Alcohol", value=9.4)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_button = st.button("Predict Quality")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= RESULT SECTION =================
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Prediction Result")

    if predict_button:
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

            st.markdown(
                f"<div class='result-card'>Quality Score: {prediction}</div>",
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.info("Enter values and click Predict.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Streamlit | ML Project</p>",
    unsafe_allow_html=True
)
