import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="CO₂ Explorer", page_icon="🌱")

st.title("🌱 CO₂ Explorer – Visualize Emissions from Diesel Generators")

st.markdown("""
Move the slider below to simulate how **runtime (in hours)** of a diesel generator affects **CO₂ emissions**. 
This is based on average generator load and diesel emission factors.
""")

# Inputs
dg_rating = st.slider("Diesel Generator Size (in kVA)", min_value=10, max_value=500, value=100, step=10)
runtime = st.slider("Runtime (in hours)", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

# Constants
load_factor = 0.8  # real operating load
diesel_emission_factor = 0.8  # kg CO2/kWh

# Calculations
actual_kw = dg_rating * load_factor
energy_used = actual_kw * runtime
co2_emitted = energy_used * diesel_emission_factor

# Generate curve
runtimes = np.linspace(0.5, 10, 50)
co2_values = (dg_rating * load_factor * runtimes) * diesel_emission_factor

# 3D-Style Plot
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=runtimes,
    y=[dg_rating] * len(runtimes),
    z=co2_values,
    mode='lines+markers',
    line=dict(color='green', width=5),
    marker=dict(size=4),
    name="CO₂ Emissions"
))

fig.update_layout(
    scene=dict(
        xaxis_title='Runtime (Hours)',
        yaxis_title='DG Size (kVA)',
        zaxis_title='CO₂ Emitted (kg)',
    ),
    margin=dict(l=10, r=10, b=10, t=40),
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.info(f"🔍 A {dg_rating} kVA DG running for {runtime} hours emits approximately **{co2_emitted:.1f} kg of CO₂**.")
st.markdown("---")
st.caption("Made by Ganesh ✨ | Follow on [Medium](https://medium.com/@ganeshitya)")
