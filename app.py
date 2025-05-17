import streamlit as st

st.set_page_config(page_title="BESS Bot", page_icon="🔋")

st.title("🔋 BESS Bot – Replace Your Diesel Generator")
st.write("Let's find the right Battery Energy Storage System (BESS) size to replace your Diesel Generator for **2 hours backup**.")

# Input fields
dg_rating = st.number_input("1️⃣ Enter your current Diesel Generator size (in kVA)", min_value=5, max_value=500, value=125)
load_type = st.selectbox("2️⃣ Select your load type", ["Office", "Retail", "Mixed"])
has_solar = st.radio("3️⃣ Do you have rooftop solar installed?", ["Yes", "No"])

# Constants (adjustable)
load_factor = 0.8  # real-world DG loading
backup_duration = 2  # hours
efficiency = 0.9  # inverter + battery combined efficiency

# Estimate energy required
real_load_kw = dg_rating * load_factor
required_kwh = real_load_kw * backup_duration / efficiency

# Estimate inverter size
recommended_inverter_kva = dg_rating  # inverter should match DG size

# Environmental savings
diesel_emissions_factor = 0.8  # kg CO2 per kWh from diesel
co2_saved = required_kwh * diesel_emissions_factor

# Payback logic (rough estimate)
if has_solar == "Yes":
    payback_years = 4
else:
    payback_years = 6

# Output
if st.button("🔍 Calculate BESS Recommendation"):
    st.subheader("✅ Your BESS Recommendation:")
    st.markdown(f"- 🔋 **Battery Size:** {required_kwh:.1f} kWh")
    st.markdown(f"- ⚡ **Inverter Size:** {recommended_inverter_kva:.0f} kVA")
    st.markdown(f"- 🌱 **CO2 Savings (per use):** ~{co2_saved:.0f} kg CO2 avoided")
    st.markdown(f"- 💰 **Estimated Payback:** {payback_years} years")

    st.success("You're ready to move beyond diesel! 🚀")

st.markdown("---")
st.markdown("Made with ❤️ by [Ganesh](https://medium.com/@ganeshitya)")
