import streamlit as st

# --- Article Info and Hyperlinked References at the Top ---
st.markdown("""
**Carbon Major Streamlit App, Version 0.1**  
Replication for *[Carbon majors and the scientific case for climate liability](https://www.nature.com/articles/s41586-025-08751-3)*  
Authors: [Christopher W. Callahan](https://www.nature.com/articles/s41586-025-08751-3) & [Justin S. Mankin](https://www.nature.com/articles/s41586-025-08751-3)  
Reference Dataset & Code Repository: *[IEEE DataPort](https://ieee-dataport.org/open-access/replication-carbon-majors-and-scientific-case-climate-liability)*
""")

# --- Metadata ---
st.markdown("""
### FaIR Warming Simulations  
**Authors:** Christopher W. Callahan & Justin S. Mankin
""")

# --- Main Title ---
st.title("FaIR Warming Simulations")

# --- 1. Total Warming ---
st.header("1. Total Warming (FaIR Warming Simulations)")
st.image("FaIR Warming Simulations.png", caption="FaIR warming simulations")

# --- 2. Warming from Carbon Majors with Dropdown ---
st.header("2. Warming from Carbon Majors")
contrib_options = [
    "all", "ioc", "soe", "topfive", "topten",
    "Saudi Aramco", "Chevron", "ExxonMobil", "Gazprom", "BP",
    "National Iranian Oil Co.", "Shell", "Coal India", "Pemex", "British Coal Corporation"
]
selected_contrib = st.selectbox("Select Contributor (for highlighting in blue):", contrib_options, index=0)
st.image("Warming from carbon majors.png", caption="Warming from carbon majors\n(Selected contributor highlighted in blue)")

# --- 3. Individual Contributor Warming ---
st.header("3. Individual Contributor Warming")
selected_individual = st.selectbox(
    "Select Individual Contributor Plot (only Gazprom demo available):",
    ["Gazprom"]
)
if selected_individual == "Gazprom":
    st.image("Plot for specific contrib Gazprom.png", caption="Warming for Gazprom (individual plot)")
