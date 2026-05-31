import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import pandas as pd
from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
import streamlit as st

STATE_INFO = {
    1:  ("Sokoto",       13.0622, 5.2339),
    2:  ("Zamfara",      12.1222, 6.2236),
    3:  ("Katsina",      12.9889, 7.6006),
    4:  ("Jigawa",       12.2280, 9.5616),
    5:  ("Yobe",         12.2939, 11.4390),
    6:  ("Borno",        11.8846, 13.1520),
    7:  ("Adamawa",      9.3265,  12.3984),
    8:  ("Gombe",        10.2791, 11.1670),
    9:  ("Bauchi",       10.3158, 9.8442),
    10: ("Kano",         12.0022, 8.5920),
    11: ("Kaduna",       10.5264, 7.4381),
    12: ("Kebbi",        11.4942, 4.2333),
    13: ("Niger",        9.9309,  5.5983),
    14: ("FCT",          8.8965,  7.1858),
    15: ("Nasarawa",     8.4998,  8.1997),
    16: ("Plateau",      9.2182,  9.5179),
    17: ("Taraba",       7.9994,  10.7739),
    18: ("Benue",        7.1907,  8.1346),
    19: ("Kogi",         7.7337,  6.6906),
    20: ("Kwara",        8.4966,  4.5421),
    21: ("Oyo",          8.1574,  3.6146),
    22: ("Osun",         7.5629,  4.5200),
    23: ("Ekiti",        7.7190,  5.3110),
    24: ("Ondo",         7.2500,  5.2000),
    25: ("Edo",          6.3350,  5.6037),
    26: ("Anambra",      6.2209,  6.9370),
    27: ("Enugu",        6.4584,  7.5464),
    28: ("Ebonyi",       6.2649,  8.0130),
    29: ("Cross River",  5.8702,  8.5988),
    30: ("Akwa Ibom",    5.0077,  7.9136),
    31: ("Abia",         5.4527,  7.5248),
    32: ("Imo",          5.4920,  7.0264),
    33: ("Rivers",       4.8396,  6.9110),
    34: ("Bayelsa",      4.7719,  6.0699),
    35: ("Delta",        5.5320,  5.8987),
    36: ("Lagos",        6.5244,  3.3792),
    37: ("Ogun",         7.0000,  3.3500),
}

@st.cache_data
def get_state_risk_data():
    loader = DataLoader("data/raw/NGPR81FL.DTA")
    df = loader.load()
    state_codes = df["state"].copy()
    preprocessor = Preprocessor(df)
    df_processed = preprocessor.preprocessor(df)
    df_processed["state"] = state_codes.values
    df_grouped = df_processed.groupby("state")["rdt_result"].mean()
    rows = []
    for state_code, rate in df_grouped.items():
        if state_code in STATE_INFO:
            name, lat, lon = STATE_INFO[state_code]
            rows.append({
                "state_code": state_code,
                "state": name,
                "latitude": lat,
                "longitude": lon,
                "positivity_rate": round(rate, 4),
                "risk_level": "High" if rate >= 0.65 else "Moderate" if rate >= 0.35 else "Low"
            })
    return pd.DataFrame(rows)