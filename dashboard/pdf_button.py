"""
PDF Download Button

Creates the PDF report download button.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st

from reports.pdf_report import generate_pdf


def show_pdf_button(stats, events):
    """
    Display PDF report generation button.

    Parameters
    ----------
    stats : dict
        Dashboard statistics.

    events : list
        Filtered security events.
    """

    st.subheader("📄 Investigation Report")

    st.caption(
        "Generate a professional PDF investigation report."
    )

    if st.button(
        "📄 Generate PDF Report",
        use_container_width=True
    ):

        pdf = generate_pdf(
            stats,
            events
        )

        with open(pdf, "rb") as file:

            st.download_button(

                label="⬇ Download Investigation Report",

                data=file,

                file_name="investigation_report.pdf",

                mime="application/pdf",

                use_container_width=True

            )