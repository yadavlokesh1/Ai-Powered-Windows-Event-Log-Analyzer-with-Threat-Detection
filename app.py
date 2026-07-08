import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Windows Event Log Analyzer", layout="wide")

st.title("AI Windows Event Log Analyzer")
st.write(
    "Upload a Windows Event Log CSV file to detect important events, severity, resolution steps, and Gemini AI analysis."
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])


def get_resolution(event_id, level):
    if event_id == 4625:
        return [
            "Check the username and source machine/IP.",
            "Verify whether the account is locked or the password was changed.",
            "Check for repeated failed login attempts from the same source.",
            "Review account lockout policy and Security Event ID 4740.",
        ]

    elif event_id == 7031:
        return [
            "Open Services console and check the failed service status.",
            "Restart the affected service.",
            "Check service dependencies.",
            "Review recent patches, updates, or configuration changes.",
        ]

    elif event_id == 41:
        return [
            "Check for sudden power loss or unexpected restart.",
            "Review system uptime and shutdown history.",
            "Check hardware, UPS, power supply, and Windows updates.",
            "Review related events before the reboot time.",
        ]

    elif event_id == 10016:
        return [
            "This is usually a DCOM permission warning.",
            "Check whether the related application is actually failing.",
            "Review Component Services permissions only if the issue is recurring.",
            "This warning can often be ignored if there is no user-facing issue.",
        ]

    elif level == "Warning":
        return [
            "Review the warning message and event source.",
            "Check whether the issue is recurring.",
            "Verify recent system, service, or policy changes.",
        ]

    else:
        return [
            "Review the event message and provider name.",
            "Search Microsoft documentation for the Event ID.",
            "Check recent configuration, patching, service, or policy changes.",
        ]


def get_ai_analysis(event_id, level, source, message):
    prompt = f"""
You are a senior Windows Server Administrator.

Analyze this Windows Event Log and provide a short troubleshooting summary.

Event ID: {event_id}
Level: {level}
Source: {source}
Message: {message}

Return the answer in this format:

Root Cause:
Impact:
Recommended Fix:

Keep it concise and practical.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"AI Error: {e}"


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Logs Preview")
    st.dataframe(df)

    required_columns = ["TimeCreated", "EventID", "Level", "ProviderName", "Message"]
    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        st.error(f"Missing required columns: {missing_columns}")
    else:
        important_levels = ["Error", "Critical", "Warning", "Failure Audit"]
        filtered_df = df[df["Level"].isin(important_levels)]

        st.subheader("Important Events Found")
        st.write(f"Total logs uploaded: {len(df)}")
        st.write(f"Important logs found: {len(filtered_df)}")

        st.dataframe(filtered_df)

        st.subheader("Analysis, Resolution and AI Summary")

        if len(filtered_df) == 0:
            st.success("No Error, Critical, Warning, or Failure Audit events found.")
        else:
            for index, row in filtered_df.iterrows():
                event_id = int(row["EventID"])
                level = row["Level"]
                source = row["ProviderName"]
                message = row["Message"]

                st.markdown("---")
                st.write(f"**Time Created:** {row['TimeCreated']}")
                st.write(f"**Event ID:** {event_id}")
                st.write(f"**Level:** {level}")
                st.write(f"**Source:** {source}")
                st.write(f"**Message:** {message}")

                if level == "Critical":
                    st.error("Severity: High")
                elif level in ["Error", "Failure Audit"]:
                    st.warning("Severity: Medium")
                else:
                    st.info("Severity: Low")

                st.write("**Recommended Resolution:**")
                resolution_steps = get_resolution(event_id, level)

                for step in resolution_steps:
                    st.write(f"- {step}")

                st.write("**Gemini AI Analysis:**")
                ai_result = get_ai_analysis(event_id, level, source, message)
                st.info(ai_result)

else:
    st.info("Please upload a CSV file to start analysis.")
