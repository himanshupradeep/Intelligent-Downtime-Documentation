import streamlit as st
import pandas as pd

st.set_page_config(page_title="Intelligent Downtime Documentation", layout="wide")
st.title("🧠 Intelligent Downtime Documentation")


uploaded_file = st.file_uploader("📂 Upload your downtime data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 CSV Preview (First 10 Rows x 10 Columns)")
    preview_df = df.iloc[:10, :10]
    st.dataframe(preview_df)

    selected_row_index = st.selectbox("🔎 Select a row to view full details", preview_df.index)
    if selected_row_index is not None:
        row_data = preview_df.loc[selected_row_index]

        st.markdown("## 🔍 Selected Row Summary")

        def grey_card(title, value):
            st.markdown(
                f"""
                <div style="background-color:#F0F0F0; padding:12px; border-radius:6px; margin:5px 0">
                    <span style="font-weight:600; color:#000000">{title}:</span>
                    <span style="color:#000000"> {value}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Serial Number at top
        grey_card("Serial No", row_data.get("Unnamed: 0", "N/A"))

        # First Row: Downtime ID, Start Time, End Time
        c1, c2, c3 = st.columns(3)
        with c1: grey_card("Downtime ID", row_data.get("Downtime_ID", ""))
        with c2: grey_card("Start Time", row_data.get("Start_Time", ""))
        with c3: grey_card("End Time", row_data.get("End_Time", ""))

        # Second Row: Machine ID, DTC Code
        c4, c5 = st.columns(2)
        with c4: grey_card("Machine ID", row_data.get("Machine_ID", ""))
        with c5: grey_card("DTC Code", row_data.get("DTC_Code", ""))

        # Error Classification Block
        st.markdown("### 🧩 Error Classification")
        for level in ["Error CL1", "Error CL2", "Error CL3", "Error CL4"]:
            grey_card(level, row_data.get(level, "N/A"))

        # Diagnostic Questions Section
        st.markdown("---")
        st.subheader("🛠️ Diagnostic Questions (Record Your Answers Below)")

        questions = [
            "1. What was the observed issue?",
            "2. What was the root cause?",
            "3. How was the failure diagnosed?",
            "4. What tools were used during diagnosis?",
            "5. How long did it take to resolve?",
            "6. Who resolved it?",
            "7. Were there any safety concerns?",
            "8. Was the issue preventable?",
            "9. What preventive action is now in place?",
            "10. Any other recommendations?"
        ]

        for i, q in enumerate(questions):
            st.markdown(f"**{q}**")
            if st.button(f"🎤 Record Answer {i+1}", key=f"record_button_{i}"):
                st.write(f"Recording started for Question {i+1}...")  # Placeholder