"""
Successful Login Detection Module

Detects Windows Successful Login events
(Event ID 4624).

Author: Your Name
Project: Windows Security Log Analyzer
"""


def detect_successful_logins(events):
    """
    Detect successful login events.

    Parameters:
        events (list): List of structured event dictionaries.

    Returns:
        list: List containing only successful login events.
    """

    successful_logins = []

    for event in events:

        if event["event_id"] == 4624:

            successful_logins.append(event)

    return successful_logins