"""
Event Description Module

Maps Windows Event IDs to readable descriptions.

Author: Your Name
Project: Windows Security Log Analyzer
"""


def get_description(event_id):

    descriptions = {

        4624: "Successful Login",

        4625: "Failed Login",

        4672: "Special Privileges Assigned",

        4720: "User Account Created",

        4723: "Password Changed",

        4726: "User Account Deleted",

        4728: "Added to Security Group",

        4732: "Added to Local Group",

        4740: "Account Locked",

        4756: "Added to Universal Group"

    }

    return descriptions.get(
        event_id,
        "Unknown Event"
    )