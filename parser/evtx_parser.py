"""
EVTX Parser Module

Reads Windows Event Log (.evtx) files
and returns XML event records.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from Evtx.Evtx import Evtx


def read_evtx(file_path, max_events=10000):
    """
    Read a Windows EVTX file.

    Parameters
    ----------
    file_path : str
        Path to the EVTX file.

    max_events : int, optional
        Maximum number of events to read.
        If None, read the entire file.

    Returns
    -------
    list
        List of XML event strings.
    """

    events = []

    with Evtx(file_path) as log:

        for i, record in enumerate(log.records()):

            if max_events is not None and i >= max_events:
                break

            events.append(record.xml())

    return events