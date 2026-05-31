import streamlit as st
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app.utils.predictor import MalariaPredictor

st.title("🔬 Malaria Risk Prediction")
st.markdown("Fill in the houshold details below to get a malaria risk assessment.")

#load model once using the st.cache_resource
@st.cache_resource
def load_model():
    return MalariaPredictor("models/Random_Forest.pkl")

predictor = load_model()

#FORM
with st.form("prediction_form"):
    st.subheader("Household information")
    col1, col2, col3 = st.columns(3)

    with col1:
        geopolitical_zone = st.selectbox(
            "Geopolitical Zone",
            options=[1, 2, 3, 4, 5, 6],
            format_func=lambda x: {
                1: "North Central", 2: "North East", 3: "North West",
                4: "South East", 5: "South South", 6: "South West"
            }[x]
        )
        residence_type = st.selectbox(
            "Residence Type",
            options=[1, 2],
            format_func=lambda x: {1: "Urban", 2: "Rural"}[x]
        )
        water_source = st.selectbox(
            "Water Source",
            options=[11, 14, 21, 31, 32, 43, 71],
            format_func=lambda x: {
                11: "Piped", 14: "Tube well", 21: "Protected well", 31: "Protected spring", 
                32: "Unprotected spring", 43: "Surface water", 71: "Bottled water"
            }[x]
        )
        floor_material = st.selectbox(
            "Floor Material",
            options=[11, 21, 31, 34, 96],
            format_func=lambda x: {
                11: "Earth", 21: "Wood", 31: "Ceramic", 34: "Cement", 96:"Other"
            }[x]
        )
    with col2:
        wall_material = st.selectbox(
            "Wall Material",
            options=[11, 22, 31, 34, 96],
            format_func=lambda x: {
                11: "Thatch", 22: "Mud bricks", 31: "Cement blocks", 34: "Stone", 96: "Other"
            }[x]
        )
        roof_material = st.selectbox(
            "Roof Material",
            options=[11, 31, 96],
            format_func=lambda x: {
                11: "Thatch", 31: "Iron sheets", 96: "Other"
            }[x]
        )
        sex = st.selectbox(
            "Sex",
            options=[1, 2],
            format_func=lambda x: {
                1: "Male", 2: "Female"
            }[x]
        )
        has_electricity = st.selectbox(
            "Has Electricity",
            options=[0, 1],
            format_func=lambda x: {
                0: "No", 1: "Yes"
            }[x]
        )
    with col3:
        wealth_index = st.slider(
            "Wealth Index",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Poorest, 5 = Richest"
        )
        age = st.number_input("Age (years)", min_value=0, max_value=96, value=25)
        household_size = st.number_input("Household Size", min_value=1, max_value=30, value=5)
        children_under5 = st.number_input("Children Under 5(years)", min_value=0, max_value=10, value=2)
        net_type = st.selectbox(
            "Net Type",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0:"No net", 1: "Treated net only", 2: "Both treated and untreated", 3: "Untreated only"
            }[x]
        )

    submitted = st.form_submit_button("Predict Malaria Risk")

#RESULT
if submitted:
    user_inputs = {
        "geopolitical_zone": geopolitical_zone,
        "water_source": water_source,
        "floor_material": floor_material,
        "wall_material": wall_material,
        "roof_material": roof_material,
        "residence_type": residence_type,
        "sex": sex,
        "age": age,
        "has_electricity": has_electricity,
        "wealth_index": wealth_index,
        "household_size": household_size,
        "children_under5": children_under5,
        "net_type": net_type
    }
    
    result = predictor.predict(user_inputs)

    st.divider()
    prob_pct = round(result["probability"] * 100, 1)

    if result["risk_level"] == "Low":
        st.success(f"Low Risk — {prob_pct}% probability of malaria")
    elif result["risk_level"] == "Moderate":
        st.warning(f"Moderate Risk — {prob_pct}% probability of malaria")
    else:
        st.error(f"High Risk — {prob_pct}% probability of malaria")

    st.metric("Malaria Probability", f"{prob_pct}%")
    st.metric("Prediction", "Positive" if result["prediction"] == 1 else "Negative")