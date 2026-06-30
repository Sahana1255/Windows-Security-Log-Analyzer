"""
Uploader Module

Handles uploaded EVTX files.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from pathlib import Path
import re

import streamlit as st


# ---------------------------------------------------
# Upload Folder
# ---------------------------------------------------

UPLOAD_FOLDER = Path.cwd() / "data" / "uploaded_logs"


# ---------------------------------------------------
# Save Uploaded File
# ---------------------------------------------------

def save_uploaded_file(uploaded_file):
    """
    Save an uploaded EVTX file.

    Parameters
    ----------
    uploaded_file : UploadedFile
        Streamlit UploadedFile object.

    Returns
    -------
    str
        Absolute path of the saved file.
    """

    try:

        # Create upload folder
        UPLOAD_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        # Safe filename
        filename = Path(uploaded_file.name).name

        filename = re.sub(
            r'[<>:"/\\|?*]',
            "_",
            filename
        ).strip()

        if not filename:
            filename = "uploaded_log.evtx"

        if not filename.lower().endswith(".evtx"):
            filename += ".evtx"

        # Absolute path
        file_path = (UPLOAD_FOLDER / filename).resolve()

        # -----------------------------
        # Debug Information
        # -----------------------------

        st.write("📂 Upload Folder:", UPLOAD_FOLDER)
        st.write("📄 Filename:", filename)
        st.write("📍 File Path:", file_path)
        st.write("📁 Folder Exists:", UPLOAD_FOLDER.exists())
        st.write("📏 File Size:", uploaded_file.size, "bytes")

        # -----------------------------
        # Save File
        # -----------------------------

        with open(str(file_path), "wb") as file:
            file.write(uploaded_file.getbuffer())

        st.success("✅ File uploaded successfully.")

        return str(file_path)

    except Exception as exc:

        st.error("❌ Upload failed.")

        st.exception(exc)

        raise