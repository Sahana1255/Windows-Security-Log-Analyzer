"""
Severity Module

Assigns severity levels to Windows Security Events.

Author: Your Name
Project: Windows Security Log Analyzer
"""


def get_severity(event_id):
    """
    Return severity for a Windows Event ID.
    """

    severity_map = {

        # High Risk
        4625: "🔴 High",
        4672: "🔴 High",
        4728: "🔴 High",
        4732: "🔴 High",
        4756: "🔴 High",
        4740: "🔴 High",

        # Medium Risk
        4720: "🟡 Medium",
        4723: "🟡 Medium",
        4726: "🟡 Medium",

        # Low Risk
        4624: "🟢 Low"

    }

    return severity_map.get(
        event_id,
        "⚪ Informational"
    )