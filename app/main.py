import streamlit as st

st.set_page_config(
    page_title="Malaria Prevalence Prediction",
    page_icon="🦟",
    layout="wide"
)

st.title("🦟 Malaria Prevalence Prediction System")
st.subheader("Nigeria - NMIS 2021")

st.markdown("""
    This system uses a **Random Forest Classifier* trained on the Nigeria Malaria 
    Indicator Survey (NMIS) 2021 to predict malaria risk.
            
    **Navigate using the sidebar.**
    - 🔬 **Prediction** — Enter household details to get a malaria risk assessment
    - 🗺️ **Risk Map** — View malaria positivity rates across all Nigerian states.
    
    **Dataset:** 70,428 household members | 10,717 tested | 37 states covered  
    **Best Model:** Random Forest — F1: 0.7287 | AUC-ROC: 0.7989
             
""")


