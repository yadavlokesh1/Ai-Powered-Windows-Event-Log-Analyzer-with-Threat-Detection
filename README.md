# 🤖 AI Windows Event Log Analyzer with Threat Detection

A lightweight AI-powered tool that analyzes exported Windows Event Logs and generates root cause analysis, severity, and troubleshooting recommendations using Google Gemini.

---

## 🚨 Problem & Solution

**The Problem:** Windows administrators spend valuable time manually reviewing Event Viewer logs to identify critical issues and determine the correct troubleshooting steps.

**The Solution:** Upload an exported Windows Event Log CSV file, and the tool automatically identifies important events, classifies their severity, and uses Google Gemini AI to generate root cause analysis and recommended fixes within seconds.

---

## ✨ Features

- Upload Windows Event Log CSV files
- Detect Critical, Error, Warning & Failure Audit events
- AI-generated Root Cause Analysis
- AI-generated Recommended Resolution
- Severity Classification
- Clean and simple web interface
- Built with Python + Streamlit + Google Gemini

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Google Gemini API

---

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Windows-Event-Log-Analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

You can generate a free Gemini API key from:
https://aistudio.google.com/app/apikey

### 4. Run the application

```bash
streamlit run app.py
```

### 5. Upload your Windows Event Log CSV

The application will automatically:

- Read the CSV file
- Detect important Windows Events
- Classify severity
- Send the event details to Google Gemini
- Display AI-generated:
  - Root Cause
  - Impact
  - Recommended Resolution

---

## 📸 Screenshots

Screenshots are available in the **screenshots/** folder.

---

## 📌 Example Output

After uploading a Windows Event Log CSV, the tool displays:

- Log Preview
- Important Events
- Severity Level
- 🤖 Gemini AI Analysis
- Root Cause
- Recommended Resolution

---

## 💡 Future Improvements

- EVTX file support
- Downloadable PDF reports
- Incident summary generation
- Dashboard & charts
- Email alerts
- Integration with SIEM tools

---
Author
Lokesh Yadav — Infrastructure Specialist | Windows Server · VMware & Nutanix · Multi cloud operations · Automation


