"""
XML Extractor Module

This module converts raw XML events into structured
Python dictionaries.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import xml.etree.ElementTree as ET


def extract_event(xml_event):
    """
    Convert a single XML event into a structured Python dictionary.

    Parameters:
        xml_event (str): Raw XML event string.

    Returns:
        dict: Structured event information.
    """

    root = ET.fromstring(xml_event)

    namespace = {
        "ns": "http://schemas.microsoft.com/win/2004/08/events/event"
    }

    event_id = root.find(".//ns:EventID", namespace)
    computer = root.find(".//ns:Computer", namespace)
    timestamp = root.find(".//ns:TimeCreated", namespace)

    username = None

    for data in root.findall(".//ns:Data", namespace):
        if data.get("Name") == "SubjectUserName":
            username = data.text
            break

    return {
        "event_id": int(event_id.text) if event_id is not None else None,
        "computer": computer.text if computer is not None else None,
        "timestamp": timestamp.get("SystemTime") if timestamp is not None else None,
        "username": username,
        "raw_xml": xml_event,
    }


def extract_events(xml_events):
    """
    Convert a list of XML events into structured Python dictionaries.

    Parameters:
        xml_events (list): List of XML event strings.

    Returns:
        list: List of structured event dictionaries.
    """

    structured_events = []

    for xml_event in xml_events:
        structured_events.append(extract_event(xml_event))

    return structured_events