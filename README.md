# AI Windows Event Log Analyzer with Threat Detection

A lightweight Windows Event Log Analyzer built with **Python + Streamlit** to help Windows admins quickly identify important events, severity, and recommended resolution steps from exported CSV logs.

---

## Problem & Solution

**The problem:** Windows administrators spend too much time manually scanning Event Viewer logs to identify critical issues and possible fixes.

**The solution:** A lightweight Python and Streamlit tool that analyzes exported Windows Event Logs, highlights important events, assigns severity, and shows recommended troubleshooting steps.

---

## Why This Tool Matters

Windows Event Viewer can contain hundreds or thousands of logs. During troubleshooting, manually finding useful events is slow, repetitive, and easy to mess up.

This tool makes the process faster by showing only the important stuff:

- Critical events
- Error events
- Warning events
- Failed login attempts
- Severity level
- Recommended resolution steps

Less noise. More signal. Finally, logs behaving like they have a purpose.

---

## Features

- Upload Windows Event Log CSV file
- Preview uploaded logs
- Filter important events
- Detect Error, Critical, Warning, and Failure Audit logs
- Show severity as High, Medium, or Low
- Provide recommended troubleshooting steps
- Simple Streamlit web interface
- Sample CSV included for testing

---

## Event IDs Covered

| Event ID | Description | Severity |
|---|---|---|
| 4625 | Failed logon attempt | Medium |
| 7031 | Windows service terminated unexpectedly | Medium |
| 41 | System rebooted without clean shutdown | High |
| 10016 | DistributedCOM permission warning | Low |

---

## Tech Stack

- Python
- Streamlit
- Pandas

---

## Project Structure

```text
AI-Windows-Event-Log-Analyzer/
│
├── app.py
├── requirements.txt
├── sample_logs.csv
├── README.md
├── .gitignore
└── screenshots/
```

---

## How It Works

```text
Upload Windows Event Log CSV
        ↓
Read data using Pandas
        ↓
Filter important events
        ↓
Assign severity
        ↓
Show recommended resolution steps
```

---

## Sample CSV Format

The uploaded CSV should contain these columns:

```csv
TimeCreated,EventID,Level,ProviderName,Message
```

Example:

```csv
2026-07-01 10:15:22,4625,Failure Audit,Microsoft-Windows-Security-Auditing,An account failed to log on
```

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## Output

After uploading the sample CSV file, the tool shows:

- Uploaded logs preview
- Total logs uploaded
- Important logs found
- Event ID
- Event level
- Event source
- Event message
- Severity
- Recommended resolution steps

---

## Screenshots

Project screenshots are available inside the `screenshots` folder.

---

## Current Status

This version is a **rule-based Windows Event Log Analyzer**.

It currently uses predefined logic to detect important events and provide resolution steps.

AI-based dynamic root cause analysis will be added in a future version. No fake AI flex here, because interviewers have eyes.

---

## Future Enhancements

- Add Gemini AI-based root cause analysis
- Generate downloadable incident reports
- Add more Windows Event IDs
- Add brute-force login detection logic
- Add charts for event trends
- Support direct EVTX file parsing
- Add export report option

---

## Interview Explanation

I created this project to solve a common Windows administration problem: manually analyzing Event Viewer logs during troubleshooting.

The tool takes exported Windows Event Logs in CSV format, filters important events like Error, Critical, Warning, and Failure Audit, assigns severity, and provides recommended resolution steps for common Windows Event IDs.

This helps system administrators troubleshoot faster and follow a structured approach during incidents.

Author
Lokesh Yadav — Infrastructure Specialist | Windows Server · VMware · Nutanix · Cloud · Automation
