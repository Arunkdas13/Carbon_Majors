import streamlit as st

# --- Article Info and Hyperlinked References at the Top ---
st.markdown("""
<h1 style='font-size: 30px;'>
Carbon Major Streamlit App, Version 0.1
</h1>
<p style='font-size: 20px;'>
Replication for <a href='https://www.nature.com/articles/s41586-025-08751-3' target='_blank'><em>Carbon majors and the scientific case for climate liability</em></a> 
<span style='white-space: nowrap;'>(Nature 640, 893–901, 2025)</span><br>
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

# --- 4. Abstract at the Bottom ---
st.markdown("""
<hr>
<h3>Abstract</h3>
<p style='font-size: 16px; line-height: 1.6;'>
Will it ever be possible to sue anyone for damaging the climate? Twenty years after this question was first posed, we argue that the scientific case for climate liability is closed. Here we detail the scientific and legal implications of an ‘end-to-end’ attribution that links fossil fuel producers to specific damages from warming. Using scope 1 and 3 emissions data from major fossil fuel companies, peer-reviewed attribution methods and advances in empirical climate economics, we illustrate the trillions in economic losses attributable to the extreme heat caused by emissions from individual companies.
</p>
<p style='font-size: 16px; line-height: 1.6;'>
Emissions linked to Chevron, the highest-emitting investor-owned company in our data, for example, very likely caused between US $791 billion and $3.6 trillion in heat-related losses over the period 1991–2020, disproportionately harming the tropical regions least culpable for warming.
</p>
<p style='font-size: 16px; line-height: 1.6;'>
More broadly, we outline a transparent, reproducible and flexible framework that formalizes how end-to-end attribution could inform litigation by assessing whose emissions are responsible and for which harms. Drawing quantitative linkages between individual emitters and particularized harms is now feasible, making science no longer an obstacle to the justiciability of climate liability claims.
</p>
""", unsafe_allow_html=True)
