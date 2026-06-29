from Evtx.Evtx import Evtx


def read_evtx(file_path, max_events=10):
    """
    Read a Windows EVTX file and return the first few events as XML.

    Parameters:
        file_path (str): Path to the EVTX file.
        max_events (int): Maximum number of events to read.

    Returns:
        list: List of XML event strings.
    """

    events = []

    with Evtx(file_path) as log:
        for i, record in enumerate(log.records()):

            if i >= max_events:
                break

            events.append(record.xml())

    return events