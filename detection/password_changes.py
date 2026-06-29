"""
Password Change Detection Module

Detects Windows Password Change events
(Event ID 4723).

Author: Your Name
Project: Windows Security Log Analyzer
"""


def detect_password_changes(events):
    """
    Detect password change events.

    Parameters:
        events (list): List of structured event dictionaries.

    Returns:
        list: List containing only password change events.
    """

    password_changes = []

    for event in events:

        if event["event_id"] == 4723:

            password_changes.append(event)

    return password_changes
