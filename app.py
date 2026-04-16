import streamlit as st
from utils.pdf_parser import extract_text_and_images
from utils.llm import extract_observations, call_llm
from utils.report_generator import merge_data, generate_ddr

st.title("🧠 AI DDR Generator")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])

if st.button("Generate DDR Report"):

    if inspection_file and thermal_file:

        with open("inspection.pdf", "wb") as f:
            f.write(inspection_file.read())

        with open("thermal.pdf", "wb") as f:
            f.write(thermal_file.read())

        st.write("📄 Extracting data...")

        inspection_text, inspection_images = extract_text_and_images("inspection.pdf")
        thermal_text, thermal_images = extract_text_and_images("thermal.pdf")

        st.write("🧠 Processing with AI...")

        inspection_data = extract_observations(inspection_text, "inspection report")
        thermal_data = extract_observations(thermal_text, "thermal report")

        # 🔥 MERGE STEP
        merged_prompt = merge_data(inspection_data, thermal_data)
        merged_data = call_llm(merged_prompt)

        # 🔥 DDR GENERATION
        final_prompt = generate_ddr(merged_data)
        ddr_report = call_llm(final_prompt)

        st.success("✅ DDR Report Generated!")

        st.markdown(ddr_report)

    else:
        st.warning("Please upload both files.")