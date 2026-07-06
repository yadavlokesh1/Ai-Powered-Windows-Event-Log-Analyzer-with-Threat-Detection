import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Windows Event Log Analyzer", layout="wide")

st.title("AI Windows Event Log Analyzer")
st.write("Upload a Windows Event Log CSV file to detect Error, Critical, Warning, and failed login events.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Logs Preview")
    st.dataframe(df)

    important_levels = ["Error", "Critical", "Warning", "Failure Audit"]

    filtered_df = df[df["Level"].isin(important_levels)]

    st.subheader("Important Events Found")
    st.write(f"Total logs uploaded: {len(df)}")
    st.write(f"Important logs found: {len(filtered_df)}")

    st.dataframe(filtered_df)

    st.subheader("Basic Analysis")

    if len(filtered_df) == 0:
        st.success("No major Error, Critical, Warning, or Failure Audit events found.")
    else:
        for index, row in filtered_df.iterrows():
            st.markdown("---")
            st.write(f"**Event ID:** {row['EventID']}")
            st.write(f"**Level:** {row['Level']}")
            st.write(f"**Source:** {row['ProviderName']}")
            st.write(f"**Message:** {row['Message']}")

            if row["Level"] == "Critical":
                st.error("Severity: High")
            elif row["Level"] == "Error":
                st.warning("Severity: Medium")
            elif row["Level"] == "Failure Audit":
                st.warning("Severity: Medium")
            else:
                st.info("Severity: Low")
else:
    st.info("Please upload a CSV file to start analysis.")
