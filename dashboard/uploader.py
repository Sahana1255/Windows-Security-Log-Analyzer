"""
Uploader Module

Handles uploaded EVTX files.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from pathlib import Path
import re
import streamlit as st


# Upload folder
UPLOAD_FOLDER = Path("data") / "uploaded_logs"


def save_uploaded_file(uploaded_file):
    """
    Save an uploaded EVTX file.

    Parameters
    ----------
    uploaded_file
        Streamlit UploadedFile object.

    Returns
    -------
    str
        Path to the saved file.
    """

    try:

        # Create upload folder
        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        # Original filename
        original_name = Path(uploaded_file.name).name

        # Remove invalid Windows characters
        safe_name = re.sub(r'[<>:"/\\|?*]', "_", original_name).strip()

        # Final file path
        file_path = UPLOAD_FOLDER / safe_name

        # Debug information
        st.write("Original filename:", repr(original_name))
        st.write("Sanitized filename:", repr(safe_name))
        st.write("Saving to:", str(file_path.resolve()))

        # Read uploaded file into bytes
        file_bytes = uploaded_file.read()

        st.write("File size:", len(file_bytes), "bytes")

        # Save file
        with file_path.open("wb") as f:
            f.write(file_bytes)

        st.success("File uploaded successfully.")

        return str(file_path)

    except Exception as e:

        st.error(f"Upload Error: {e}")

        raise