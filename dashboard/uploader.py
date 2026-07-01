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

        # Create a safe filename
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

        # Final absolute path
        file_path = (UPLOAD_FOLDER / filename).resolve()

        # ---------------------------------------------------
        # Upload File
        # ---------------------------------------------------

        with st.spinner(
            "📤 Uploading Windows Security Event Log..."
        ):

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

        st.success("✅ Security.evtx uploaded successfully.")

        return str(file_path)

    except Exception as exc:

        st.error("❌ Failed to upload Security.evtx.")

        st.exception(exc)

        raise