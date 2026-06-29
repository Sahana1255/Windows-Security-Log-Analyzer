from parser.evtx_parser import read_evtx


def main():
    file_path = "data/sample_logs/Security.evtx"

    events = read_evtx(file_path)

    print(f"Total Events: {len(events)}")

    print("\nFirst Event:\n")
    print(events[0])


if __name__ == "__main__":
    main()