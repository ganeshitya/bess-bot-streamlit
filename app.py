import streamlit as st
import numpy as np

st.set_page_config(page_title="Outsmart the Diesel", page_icon="♻️", layout="centered")

st.title("🎮 Outsmart the Diesel – A Climate Quiz Game")

# State tracker
if "level" not in st.session_state:
    st.session_state.level = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Level 1: Quiz questions
def level_1():
    st.subheader("🟢 Level 1: Basics")

    q1 = st.radio("1️⃣ What gas is primarily emitted by diesel generators?", 
                  ["Oxygen", "CO₂", "Hydrogen", "Nitrogen"], key="q1")

    q2 = st.radio("2️⃣ What's the fuel used in a typical DG?", 
                  ["Solar", "Diesel", "Battery", "Coal"], key="q2")

    if st.button("✅ Submit Answers"):
        if q1 == "CO₂" and q2 == "Diesel":
            st.success("✅ Correct! Moving to Level 2...")
            st.session_state.level = 2
        else:
            st.error("❌ Oops! Try again.")

# Level 2: Emissions guessing game
def level_2():
    st.subheader("🔵 Level 2: Guess the CO₂ Emissions")

    st.markdown("**Choose a DG Size and Runtime. Then guess the CO₂ emissions.**")

    dg_size = st.slider("DG Size (kVA)", 10, 500, 100, step=10)
    runtime = st.slider("Runtime (hours)", 0.5, 10.0, 2.0, step=0.5)
    
    # Calculation
    load_factor = 0.8
    emission_factor = 0.8  # kg CO2 per kWh
    energy = dg_size * load_factor * runtime
    actual_emissions = energy * emission_factor

    user_guess = st.number_input("💭 Your Guess (in kg CO₂)", min_value=0.0, step=1.0)

    if st.button("🎯 Submit Guess"):
        lower = actual_emissions * 0.9
        upper = actual_emissions * 1.1

        if lower <= user_guess <= upper:
            st.balloons()
            st.success(f"🎉 You nailed it! Actual emission = {actual_emissions:.1f} kg CO₂")
            st.markdown("👉 [Learn how BESS replaces DGs](https://medium.com/@ganeshitya)")
        else:
            st.warning(f"📉 Not quite. Actual emission = {actual_emissions:.1f} kg CO₂. Try again!")

# Run appropriate level
if st.session_state.level == 1:
    level_1()
elif st.session_state.level == 2:
    level_2()
