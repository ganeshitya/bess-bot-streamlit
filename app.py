import streamlit as st
import numpy as np
import random
import plotly.express as px

st.set_page_config(page_title="Outsmart the Diesel", page_icon="♻️", layout="wide")

# Initialize session state
if "level" not in st.session_state:
    st.session_state.level = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

# Sidebar leaderboard
st.sidebar.title("🏆 Leaderboard")
if st.session_state.leaderboard:
    for name, score in st.session_state.leaderboard:
        st.sidebar.write(f"**{name}**: {score} pts")
else:
    st.sidebar.write("No scores yet. Be the first!")

# Level 1: Quiz basics
def level_1():
    st.title("🎮 Outsmart the Diesel – A Climate Quiz Game")
    st.subheader("🟢 Level 1: Basics")

    q1 = st.radio("1️⃣ What gas is primarily emitted by diesel generators?", 
                  ["Oxygen", "CO₂", "Hydrogen", "Nitrogen"], key="q1")

    q2 = st.radio("2️⃣ What's the fuel used in a typical DG?", 
                  ["Solar", "Diesel", "Battery", "Coal"], key="q2")

    if st.button("✅ Submit Answers"):
        if q1 == "CO₂" and q2 == "Diesel":
            st.success("✅ Correct! You're ready for Level 2.")
            st.session_state.show_next = True
        else:
            st.error("❌ Oops! Try again.")

    if st.session_state.show_next:
        if st.button("➡️ Go to Level 2"):
            st.session_state.level = 2

# Level 2: CO2 emissions game
def level_2():
    st.title("🔵 Level 2: Guess the CO₂ Emissions | Estimated Caluclations for Education Purpose only")
    st.markdown("**Choose a DG Size and Runtime. Then guess the CO₂ emissions.**")

    col1, col2 = st.columns(2)
    with col1:
        dg_size = st.slider("DG Size (kVA)", 10, 500, 100, step=10)
    with col2:
        runtime = st.slider("Runtime (hours)", 0.5, 10.0, 2.0, step=0.5)

    # Calculation
    load_factor = 0.8
    emission_factor = 0.8  # kg CO2 per kWh
    energy = dg_size * load_factor * runtime
    actual_emissions = round(energy * emission_factor, 1)

    user_guess = st.number_input("💭 Your Guess (in kg CO₂)", min_value=0.0, step=1.0)

    if st.button("🎯 Submit Guess"):
        lower = actual_emissions * 0.9
        upper = actual_emissions * 1.1

        if lower <= user_guess <= upper:
            st.balloons()
            st.success(f"🎉 You nailed it! Actual emission = {actual_emissions} kg CO₂")
            # Add to leaderboard
            player = f"Player_{random.randint(100, 999)}"
            st.session_state.leaderboard.append((player, 100))
        else:
            st.error(f"😢 Not quite. Actual emission = {actual_emissions} kg CO₂. Try again!")
            st.image("https://em-content.zobj.net/thumbs/240/whatsapp/326/crying-face_1f622.png", width=100)

        # Graph
        x = [i for i in np.arange(0.5, 10.5, 0.5)]
        y = [round(dg_size * load_factor * t * emission_factor, 1) for t in x]
        fig = px.area(x=x, y=y, labels={"x": "Runtime (Hours)", "y": "CO₂ Emissions (kg)"},
                      title="CO₂ Emissions vs Runtime")
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔄 Restart Game"):
        st.session_state.level = 1
        st.session_state.show_next = False
        st.rerun()
        printf ("https://tinyurl.com/dg-bess22")
# Main flow
if st.session_state.level == 1:
    level_1()
elif st.session_state.level == 2:
    level_2()
