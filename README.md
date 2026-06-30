# 🛡️ Windows Security Log Analyzer

A professional **Python-based Windows Security Event Log Analyzer** that parses **Windows EVTX** files, detects important security events, visualizes them through an interactive dashboard, and assists SOC analysts during investigations.

Built using **Python**, **Streamlit**, **Pandas**, **python-evtx**, and **ReportLab**.

---

# 📖 Overview

Windows Security Log Analyzer is a Security Operations Center (SOC) investigation dashboard designed to analyze Windows Security Event Logs (.evtx).

The application parses raw Windows Event Logs, extracts structured event information, identifies common security events, provides interactive visualizations, and allows analysts to investigate suspicious activity through filters, searches, and detailed event inspection.

The project demonstrates core SOC analyst skills including:

- Windows Event Log Analysis
- Event Correlation
- Security Event Detection
- Log Investigation
- Dashboard Development
- Report Generation

---

# ✨ Features

## 📂 Log Analysis

- Upload Windows Security.evtx files
- Analyze built-in sample logs
- Parse thousands of events efficiently
- XML event extraction

---

## 📊 Dashboard

- Security Overview KPI Cards
- Event Distribution Chart
- Timeline Analysis
- Security Alerts
- Investigation Summary

---

## 🔍 Investigation

- Event Search
- Event Filtering
- Severity Classification
- Event Descriptions
- Event Investigation Panel
- Raw XML Viewer

---

## 📈 Analytics

- Event ID Distribution
- Security Timeline
- Login Analysis
- Account Monitoring

---

## 📄 Reporting

- CSV Export
- PDF Investigation Report

---

# 🛡 Supported Windows Security Events

| Event ID | Description |
|----------|-------------|
| 4624 | Successful Logon |
| 4625 | Failed Logon |
| 4672 | Special Privileges Assigned |
| 4720 | User Account Created |
| 4723 | Password Changed |
| 4726 | User Account Deleted |
| 4728 | Added to Security Group |
| 4732 | Added to Local Group |
| 4740 | Account Locked |
| 4756 | Added to Universal Group |

---

# 🏗 Project Architecture

```
                    Windows Security.evtx
                             │
                             ▼
                     EVTX Parser
                             │
                             ▼
                     XML Extractor
                             │
                             ▼
                  Structured Event Objects
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   Statistics            Filters              Search
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                    Dashboard Components
                             │
      ┌──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼
   Alerts         Charts      Investigation
                             │
                      CSV / PDF Reports
```

---

# 📁 Project Structure

```
Windows-Security-Log-Analyzer/

│
├── app.py
├── requirements.txt
│
├── parser/
│   ├── evtx_parser.py
│   └── xml_extractor.py
│
├── dashboard/
│   ├── alerts.py
│   ├── cards.py
│   ├── charts.py
│   ├── descriptions.py
│   ├── export.py
│   ├── filters.py
│   ├── footer.py
│   ├── investigation.py
│   ├── pdf_button.py
│   ├── search.py
│   ├── severity.py
│   ├── sidebar.py
│   ├── statistics.py
│   ├── summary.py
│   ├── table.py
│   ├── theme.py
│   └── uploader.py
│
├── reports/
│   └── pdf_report.py
│
├── data/
│   ├── sample_logs/
│   └── uploaded_logs/
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/windows-security-log-analyzer.git
```

Navigate to the project

```bash
cd windows-security-log-analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 💻 Technologies Used

- Python
- Streamlit
- Pandas
- python-evtx
- ReportLab

---

# 🔍 Investigation Workflow

1. Upload a Windows Security.evtx file.
2. Select the number of events to analyze.
3. Click **Analyze Security Log**.
4. Review dashboard metrics.
5. Inspect security alerts.
6. Analyze event trends.
7. Filter or search for events.
8. Investigate suspicious activities.
9. Export findings as CSV or PDF.

---

# 📸 Dashboard Preview

> Add screenshots after completing the project.

Example:

```
screenshots/

dashboard.png

alerts.png

charts.png

investigation.png

reports.png
```

---

# 🎯 Skills Demonstrated

This project demonstrates practical skills in:

- Windows Event Log Analysis
- Security Monitoring
- SIEM Dashboard Design
- Python Development
- Data Visualization
- Incident Investigation
- Report Generation
- Modular Software Design

---

# 🚀 Future Improvements

Potential enhancements include:

- MITRE ATT&CK Mapping
- IOC Detection
- Sigma Rule Integration
- Brute Force Detection
- PowerShell Event Analysis
- Multi-page Dashboard
- SQLite Event Storage
- REST API Support
- Dark/Light Theme Toggle
- User Authentication

---

# 👩‍💻 Author

**Sahana**

Cybersecurity Enthusiast | SOC Analyst Aspirant

---

# 📄 License

This project is intended for educational and portfolio purposes.
