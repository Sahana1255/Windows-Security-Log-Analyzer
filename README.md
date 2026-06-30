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

------------------------------------------------------------------------

This is actually a great idea. It becomes your **project documentation**, and it's something you can also use during interviews to explain your project folder by folder.

I'd structure it like this:

* 📌 Project Overview (What the project does)
* 📂 Folder Structure (One-line explanation for every folder and file in the same order as your project)
* 🛠 Tech Stack
* ⭐ Key Features / Unique Selling Points

---

# 🛡 Windows Security Log Analyzer

## 📖 Project Overview

Windows Security Log Analyzer is a Python-based Security Operations Center (SOC) dashboard that analyzes Windows Security Event Log (.evtx) files. It parses raw Windows event logs, extracts security events, classifies their severity, provides interactive visualizations, supports event investigation, and generates CSV/PDF reports to assist security analysts during incident investigations.

---

# 📂 Project Structure

```
Windows-Security-Log-Analyzer/
```

### `app.py`

Main application entry point that coordinates the complete dashboard workflow, from log loading to investigation and report generation.

---

### `requirements.txt`

Contains all Python packages required to run the application.

---

### `README.md`

Project documentation explaining the application's purpose, features, setup, architecture, and usage.

---

### `.gitignore`

Specifies files and folders that Git should ignore, such as cache files and uploaded logs.

---

## 📂 parser/

Handles reading and converting Windows Event Logs into structured Python objects.

### `evtx_parser.py`

Reads Windows `.evtx` files and extracts raw XML records using the python-evtx library.

### `xml_extractor.py`

Parses XML records and converts them into structured security event dictionaries.

---

## 📂 dashboard/

Contains all Streamlit dashboard components responsible for visualization, investigation, analytics, and user interaction.

### `sidebar.py`

Creates the dashboard sidebar containing upload options, analysis settings, and navigation information.

### `theme.py`

Applies custom CSS styling to give the dashboard a professional SOC-style appearance.

### `cards.py`

Displays KPI cards summarizing important security metrics.

### `statistics.py`

Calculates security statistics such as successful logins, failed logins, account creations, and privilege escalations.

### `severity.py`

Assigns severity levels (High, Medium, Low) to Windows Security Event IDs.

### `descriptions.py`

Maps Windows Event IDs to human-readable security event descriptions.

### `alerts.py`

Displays important security alerts based on detected Windows security events.

### `summary.py`

Generates a high-level investigation summary for the analyzed log.

### `charts.py`

Creates visual analytics including Event Distribution and Event Timeline charts.

### `filters.py`

Filters security events by Event ID, username, severity, or investigation criteria.

### `search.py`

Provides keyword-based searching across extracted security events.

### `table.py`

Displays investigated security events in a structured analyst-friendly table.

### `investigation.py`

Provides detailed event investigation with metadata and raw XML inspection.

### `export.py`

Exports filtered investigation results into CSV format.

### `pdf_button.py`

Provides the interface for generating downloadable PDF investigation reports.

### `uploader.py`

Handles uploading and safely storing user-provided EVTX files.

### `about.py`

Displays project information and application overview inside the dashboard.

### `footer.py`

Displays footer information including project branding and technologies.

---

## 📂 reports/

Contains report generation modules.

### `pdf_report.py`

Generates professional PDF investigation reports using ReportLab.

---

## 📂 data/

Stores log files used by the application.

### `sample_logs/`

Contains sample Windows Security Event Logs for testing and demonstrations.

### `uploaded_logs/`

Stores EVTX files uploaded by users during investigations.

---

## 📂 screenshots/

Stores dashboard screenshots used in project documentation and GitHub README.

---

## 🛠 Technology Stack

### Programming Language

* Python 3

### Dashboard Framework

* Streamlit

### Data Processing

* Pandas

### Windows Event Log Parsing

* python-evtx

### XML Processing

* xml.etree.ElementTree

### Report Generation

* ReportLab

### Data Structures

* Python Dictionaries
* Lists
* Collections (Counter)

### Visualization

* Streamlit Charts
* Bar Charts
* Timeline Charts

### File Handling

* Pathlib
* Regular Expressions (re)

### Version Control

* Git
* GitHub

### Development Environment

* Visual Studio Code

### Operating Systems Tested

* Windows
* Kali Linux

---

# ⭐ Key Features

* Windows EVTX Log Parsing
* XML Event Extraction
* Security Event Detection
* Interactive SOC Dashboard
* KPI Security Overview
* Security Alerts
* Severity Classification
* Event Description Mapping
* Event Filtering
* Keyword Search
* Timeline Analysis
* Event Distribution Visualization
* Investigation Panel
* Raw XML Viewer
* CSV Report Export
* PDF Investigation Report
* Professional Streamlit UI
* Custom Dashboard Theme
* Modular Python Architecture

---

# 🚀 Skills Demonstrated

* Python Development
* Modular Software Architecture
* Windows Security Event Analysis
* SOC Investigation Workflow
* Log Parsing and Processing
* Data Visualization
* Dashboard Development
* Report Automation
* File Handling
* XML Parsing
* Security Monitoring
* Git & GitHub Version Control

---

# 🎯 Project Objective

To build a modular, professional Windows Security Log Analyzer that demonstrates practical SOC analyst skills by parsing Windows Security Event Logs, detecting important security events, visualizing log data, supporting investigations, and generating security reports through an interactive dashboard.

---
