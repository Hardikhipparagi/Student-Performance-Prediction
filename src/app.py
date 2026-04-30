import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/model.pkl")

st.set_page_config(page_title="Student Predictor", layout="centered")

st.title("🎓 Student Performance Predictor")
st.markdown("### 📊 AI-powered Risk Detection System")

st.divider()

# Inputs
study_hours = st.slider("📘 Study Hours", 1, 10, 5)
attendance = st.slider("📅 Attendance (%)", 50, 100, 75)
assignments = st.slider("📝 Assignment Score", 40, 100, 70)
midterm = st.slider("📊 Midterm Score", 30, 100, 60)

st.divider()

# Predict
if st.button("🚀 Predict Performance"):

    data = np.array([[study_hours, attendance, assignments, midterm]])

    proba = model.predict_proba(data)[0][1]

    st.subheader("📈 Risk Analysis")

    # 🎯 Risk Meter (Progress Bar)
    st.progress(int(proba * 100))

    st.write(f"### 🎯 Probability of Passing: {proba*100:.1f}%")

    # 🎨 Risk Levels
    if proba > 0.7:
        st.success("✅ Low Risk — Student is likely to PASS")
    elif proba > 0.4:
        st.warning("⚠️ Medium Risk — Needs Attention")
    else:
        st.error("❌ High Risk — Likely to FAIL")

    # 💡 Smart Suggestions
    st.subheader("💡 Suggested Actions")

    if attendance < 65:
        st.write("📅 Improve attendance consistency")

    if study_hours < 4:
        st.write("📘 Increase study hours")

    if assignments < 60:
        st.write("📝 Focus on assignments")

    if midterm < 50:
        st.write("📊 Improve test preparation")