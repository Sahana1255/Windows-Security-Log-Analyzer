"""
Privilege Escalation Detection Module

Detects users added to privileged groups
(Event ID 4732).

Author: Your Name
Project: Windows Security Log Analyzer
"""


def detect_privilege_escalation(events):
    """
    Detect privilege escalation events.

    Parameters:
        events (list): List of structured event dictionaries.

    Returns:
        list: List containing only privilege escalation events.
    """

    privilege_events = []

    for event in events:

        if event["event_id"] == 4732:

            privilege_events.append(event)

    return privilege_events