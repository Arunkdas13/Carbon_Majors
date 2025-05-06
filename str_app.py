import streamlit as st

st.markdown("""
### FaIR Warming Simulations  
**Authors:** Christopher W. Callahan & Justin S. Mankin
""")

# --- Titles and Explanations ---
st.title("FaIR Warming Simulations")

# 1. Total warming (FaIR Warming Simulations)
st.header("1. Total Warming (FaIR Warming Simulations)")
st.image("FaIR Warming Simulations.png", caption="FaIR warming simulations")

# 2. Warming from carbon majors with dropdown
st.header("2. Warming from Carbon Majors")
contrib_options = [
    "all", "ioc", "soe", "topfive", "topten",
    "Saudi Aramco", "Chevron", "ExxonMobil", "Gazprom", "BP",
    "National Iranian Oil Co.", "Shell", "Coal India", "Pemex", "British Coal Corporation"
]
selected_contrib = st.selectbox("Select Contributor (for highlighting in blue):", contrib_options, index=0)
st.image("Warming from carbon majors.png", caption="Warming from carbon majors\n(Selected contributor highlighted in blue)")

# 3. Individual contributor warming (example: Gazprom)
st.header("3. Individual Contributor Warming")
selected_individual = st.selectbox(
    "Select Individual Contributor Plot (only Gazprom demo available):",
    ["Gazprom"]
)
if selected_individual == "Gazprom":
    st.image("Plot for specific contrib Gazprom.png", caption="Warming for Gazprom (individual plot)")

