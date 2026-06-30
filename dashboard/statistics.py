"""
Statistics Module

Calculates dashboard statistics.

Author: Your Name
Project: Windows Security Log Analyzer
"""


def get_statistics(events):
    """
    Calculate dashboard statistics.

    Parameters
    ----------
    events : list
        Structured security events.

    Returns
    -------
    dict
        Dashboard statistics.
    """

    stats = {
        "total_events": len(events),
        "successful_logins": 0,
        "failed_logins": 0,
        "account_creations": 0,
        "password_changes": 0,
        "privilege_escalations": 0,
        "account_lockouts": 0,
        "account_deletions": 0,
        "group_changes": 0
    }

    for event in events:

        event_id = event["event_id"]

        # Successful Login
        if event_id == 4624:
            stats["successful_logins"] += 1

        # Failed Login
        elif event_id == 4625:
            stats["failed_logins"] += 1

        # Account Created
        elif event_id == 4720:
            stats["account_creations"] += 1

        # Password Changed
        elif event_id == 4723:
            stats["password_changes"] += 1

        # Special Privileges Assigned
        elif event_id == 4672:
            stats["privilege_escalations"] += 1

        # Account Locked
        elif event_id == 4740:
            stats["account_lockouts"] += 1

        # Account Deleted
        elif event_id == 4726:
            stats["account_deletions"] += 1

        # Security Group Membership Changed
        elif event_id in [4728, 4732, 4756]:
            stats["group_changes"] += 1

    return stats