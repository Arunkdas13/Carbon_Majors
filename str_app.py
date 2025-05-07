import streamlit as st

# --- Header and Metadata ---
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

# --- 4. Acknowledgements ---
st.header("4. Acknowledgements")
st.markdown("""
This app is inspired by the article *["Will it ever be possible to sue anyone for damaging the climate?"](https://www.nature.com/articles/s41558-024-01941-w)* by Christopher W. Callahan and Justin S. Mankin, published in *Nature Climate Change*.  
We gratefully acknowledge the authors for introducing an **end-to-end attribution framework** that links fossil fuel producers’ emissions to specific climate damages, using a combination of **Scope 1 and 3 emissions data**, **FaIR climate model simulations**, and **empirical climate economics**. Their methodology underpins the scientific justification for climate liability claims.

This app also draws from replication materials publicly provided through the [IEEE DataPort repository](https://ieee-dataport.org/open-access/replication-carbon-majors-and-scientific-case-climate-liability), titled **"Replication for Carbon majors and the scientific case for climate liability"**. These materials include Python and Jupyter scripts for:

- Running FaIR climate model simulations of carbon major emissions  
- Scaling regional climate impacts from global averages using CMIP6  
- Calculating regional and event-specific economic damages  
- Producing visualizations found in the original paper  

We thank the authors for their open-access contributions and acknowledge funding support from the **National Science Foundation (NSF)**, the **Neukom Institute**, and the **Wright Center at Dartmouth College and Rockefeller Center** under **NSF Grant #1840344**.

This app is designed to help users visualize the scientific links between corporate emissions and global warming, with the goal of supporting education, transparency, and future efforts in climate accountability.

**Note**: This website may use cookies and similar technologies for analytics and personalization, in line with platform policies. For more, see [IEEE Privacy Policy](https://www.ieee.org/security-privacy.html).
""")
