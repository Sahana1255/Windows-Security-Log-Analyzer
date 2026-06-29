from parser.evtx_parser import read_evtx
from parser.xml_extractor import extract_events


def main():
    print("===== TEST XML EXTRACTOR =====")

    file_path = "data/sample_logs/Security.evtx"

    # Read the first 10 events
    xml_events = read_evtx(file_path, max_events=10)

    # Convert XML events into dictionaries
    structured_events = extract_events(xml_events)

    print(f"\nTotal Structured Events: {len(structured_events)}\n")

    print("First Structured Event:\n")

    for key, value in structured_events[0].items():
        if key != "raw_xml":
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()