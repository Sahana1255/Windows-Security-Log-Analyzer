from collections import Counter

from parser.evtx_parser import read_evtx
from parser.xml_extractor import extract_events


def main():

    file_path = "data/sample_logs/Security.evtx"

    xml_events = read_evtx(file_path, max_events=10000)

    events = extract_events(xml_events)

    event_counter = Counter()

    for event in events:
        event_counter[event["event_id"]] += 1

    print("\n========== EVENT ID SUMMARY ==========\n")

    for event_id, count in sorted(event_counter.items()):
        print(f"Event ID {event_id}: {count}")


if __name__ == "__main__":
    main()