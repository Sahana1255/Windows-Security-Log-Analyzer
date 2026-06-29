"""
Account Creation Detection Module

Detects Windows User Account Creation events
(Event ID 4720).

Author: Your Name
Project: Windows Security Log Analyzer
"""


def detect_account_creation(events):
    """
    Detect account creation events.

    Parameters:
        events (list): List of structured event dictionaries.

    Returns:
        list: List containing only account creation events.
    """

    created_accounts = []

    for event in events:

        if event["event_id"] == 4720:

            created_accounts.append(event)

    return created_accounts