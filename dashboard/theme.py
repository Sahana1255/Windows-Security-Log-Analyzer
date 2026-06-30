"""
Dashboard Theme

Professional SOC Dashboard Theme

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def load_theme():

    st.markdown(
        """
<style>

/* -----------------------------
   Hide Streamlit UI
------------------------------*/

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* -----------------------------
   Main App
------------------------------*/

.stApp {
    background: #0b1220;
    color: #f8fafc;
}

/* -----------------------------
   Sidebar
------------------------------*/

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #111827,
        #1f2937
    );

    border-right: 1px solid #374151;
}

/* -----------------------------
   Metric Cards
------------------------------*/

div[data-testid="metric-container"] {

    background: linear-gradient(
        180deg,
        #1e293b,
        #0f172a
    );

    border-radius: 18px;

    padding: 18px;

    border: 1px solid #334155;

    box-shadow:
        0px 8px 24px rgba(0,0,0,.35);

}

/* Metric label */

div[data-testid="metric-container"] label {

    color: #94a3b8 !important;

    font-size: 15px;

}

/* Metric value */

div[data-testid="metric-container"] div {

    color: white;

}

/* -----------------------------
   Buttons
------------------------------*/

.stButton > button {

    width: 100%;

    border-radius: 12px;

    border: none;

    padding: 12px;

    font-weight: bold;

    background: #2563eb;

    color: white;

}

.stButton > button:hover {

    background: #1d4ed8;

}

/* -----------------------------
   Download Buttons
------------------------------*/

.stDownloadButton > button {

    width: 100%;

    border-radius: 12px;

    font-weight: bold;

}

/* -----------------------------
   Dataframe
------------------------------*/

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

    border: 1px solid #334155;

}

/* -----------------------------
   Selectbox
------------------------------*/

div[data-baseweb="select"] {

    border-radius: 10px;

}

/* -----------------------------
   Text Input
------------------------------*/

input {

    border-radius: 10px !important;

}

/* -----------------------------
   Headers
------------------------------*/

h1 {

    color: white;

    font-weight: 700;

}

h2, h3 {

    color: #e2e8f0;

}

/* -----------------------------
   Horizontal Rule
------------------------------*/

hr {

    border-color: #334155;

}

</style>
""",
        unsafe_allow_html=True
    )