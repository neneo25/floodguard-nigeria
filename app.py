
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json


# Page configuration

st.set_page_config(
    page_title="FloodGuard Nigeria",
    page_icon="🌧️",
    layout="wide"
)


# Load model and data

model = joblib.load("flood_risk_classifier.pkl")
data = pd.read_csv("floodguard_lga_data.csv")

with open("model_features.json", "r") as f:
    feature_columns = json.load(f)


# Header

st.title("🌧️ FloodGuard Nigeria")
st.subheader("AI-Powered Flood Risk Classifier")

st.markdown(
    """
    **FloodGuard Nigeria** uses historical flood-impact data,
    subnational rainfall indicators and population exposure
    to classify flood-impact risk across selected Nigerian LGAs.
    """
)

st.divider()


# Location selection

col1, col2 = st.columns(2)

with col1:
    states = sorted(data["state"].dropna().unique())

    selected_state = st.selectbox(
        "Select State",
        states,
        key="state_selector"
    )

with col2:
    lgas = sorted(
        data.loc[
            data["state"] == selected_state,
            "lga"
        ].dropna().unique()
    )

    selected_lga = st.selectbox(
        "Select LGA",
        lgas,
        key=f"lga_selector_{selected_state}"
    )


# Analyze button

if st.button(
    "🔍 ANALYZE FLOOD RISK",
    use_container_width=True
):

    row = data[
        (data["state"] == selected_state) &
        (data["lga"] == selected_lga)
    ].iloc[0]

    # Prepare model input
    X_input = pd.DataFrame(
        [[row[feature] for feature in feature_columns]],
        columns=feature_columns
    )

    prediction = model.predict(X_input)[0]

    
    # Risk result
   
    st.divider()

    if prediction == "High":
        st.error("🔴 HIGH FLOOD RISK")
    elif prediction == "Medium":
        st.warning("🟠 MEDIUM FLOOD RISK")
    else:
        st.success("🟢 LOW FLOOD RISK")

    st.markdown(
        f"### {selected_lga}, {selected_state}"
    )

    
    # Key indicators
    
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Population Exposure",
            f"{row['total_population']:,.0f}"
        )

    with c2:
        st.metric(
            "Rainfall Anomaly",
            f"{row['avg_rainfall_anomaly']:.1f}%"
        )

    with c3:
        st.metric(
            "Max 10-Day Rainfall",
            f"{row['max_10day_rainfall']:.1f} mm"
        )

    with c4:
        st.metric(
            "3-Month Rainfall",
            f"{row['avg_3month_rainfall']:.1f} mm"
        )

    
    # Risk factors
    
    st.subheader("Key Risk Indicators")

    risk_col1, risk_col2 = st.columns(2)

    with risk_col1:
        st.write(
            "🌧️ **Rainfall conditions**"
        )
        st.write(
            "The classification considers rainfall "
            "intensity, accumulation and anomaly indicators."
        )

    with risk_col2:
        st.write(
            "👥 **Population exposure**"
        )
        st.write(
            "Population exposure is included as a "
            "contextual vulnerability indicator."
        )

    
    # Historical impact
    
    st.subheader("Historical Flood Impact")

    h1, h2 = st.columns(2)

    with h1:
        st.metric(
            "Affected Individuals",
            f"{row['affected_individuals']:,.0f}"
        )

    with h2:
        st.metric(
            "Displaced Individuals",
            f"{row['displaced_individuals']:,.0f}"
        )

    
    # Disclaimer
    
    st.info(
        "⚠️ This is an AI/ML prototype developed using "
        "historical humanitarian and rainfall datasets. "
        "It is intended as a decision-support demonstration "
        "and should not replace official flood warnings."
    )

st.divider()

st.caption(
    "FloodGuard Nigeria | 3MTT AI/ML Capstone Project"
)
