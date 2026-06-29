from parser.evtx_parser import read_evtx
from parser.event_extractor import extract_event


def main():
    print("===== TEST EXTRACTOR =====")

    file_path = "data/sample_logs/Security.evtx"

    # Read only one event
    events = read_evtx(file_path, max_events=1)

    print(f"Events Read: {len(events)}")

    # Extract fields from the first event
    structured_event = extract_event(events[0])

    print("\nExtracted Event:\n")

    for key, value in structured_event.items():
        if key != "raw_xml":
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()