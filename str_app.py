import streamlit as st

# --- Article Info and Hyperlinked References at the Top ---
st.markdown("""
<h1 style='font-size: 50px;'>
Carbon Major Streamlit App, Version 0.1
</h1>
<p style='font-size: 20px;'>
Replication for <a href='https://www.nature.com/articles/s41586-025-08751-3' target='_blank'><em>Carbon majors and the scientific case for climate liability</em></a><br>
Authors: <a href='https://www.nature.com/articles/s41586-025-08751-3' target='_blank'>Christopher W. Callahan</a> & 
<a href='https://www.nature.com/articles/s41586-025-08751-3' target='_blank'>Justin S. Mankin</a><br>
Reference Dataset & Code Repository: <a href='https://ieee-dataport.org/open-access/replication-carbon-majors-and-scientific-case-climate-liability' target='_blank'>IEEE DataPort</a>
</p>
""", unsafe_allow_html=True)

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
