from parser.evtx_parser import read_evtx
from parser.xml_extractor import extract_events

from detection.failed_logins import detect_failed_logins
from detection.successful_logins import detect_successful_logins
from detection.account_creation import detect_account_creation
from detection.password_changes import detect_password_changes
from detection.privilege_escalation import detect_privilege_escalation


def main():

    print("========== DETECTION ENGINE TEST ==========\n")

    file_path = "data/sample_logs/Security.evtx"

    # Read XML events
    xml_events = read_evtx(file_path, max_events=100000)

    # Convert XML into structured dictionaries
    structured_events = extract_events(xml_events)

    # Run all detection modules
    failed_events = detect_failed_logins(structured_events)
    successful_events = detect_successful_logins(structured_events)
    account_events = detect_account_creation(structured_events)
    password_events = detect_password_changes(structured_events)
    privilege_events = detect_privilege_escalation(structured_events)

    print(f"Total Events Read           : {len(structured_events)}")
    print(f"Successful Logins (4624)    : {len(successful_events)}")
    print(f"Failed Logins (4625)        : {len(failed_events)}")
    print(f"Account Creations (4720)    : {len(account_events)}")
    print(f"Password Changes (4723)     : {len(password_events)}")
    print(f"Privilege Escalations (4732): {len(privilege_events)}")

    print("\n========== SAMPLE RESULTS ==========\n")

    if successful_events:
        print("First Successful Login")
        print("----------------------")
        for key, value in successful_events[0].items():
            if key != "raw_xml":
                print(f"{key}: {value}")
        print()

    if failed_events:
        print("First Failed Login")
        print("------------------")
        for key, value in failed_events[0].items():
            if key != "raw_xml":
                print(f"{key}: {value}")
        print()

    if account_events:
        print("First Account Creation")
        print("----------------------")
        for key, value in account_events[0].items():
            if key != "raw_xml":
                print(f"{key}: {value}")
        print()

    if password_events:
        print("First Password Change")
        print("---------------------")
        for key, value in password_events[0].items():
            if key != "raw_xml":
                print(f"{key}: {value}")
        print()

    if privilege_events:
        print("First Privilege Escalation")
        print("--------------------------")
        for key, value in privilege_events[0].items():
            if key != "raw_xml":
                print(f"{key}: {value}")
        print()

    if (
        not successful_events
        and not failed_events
        and not account_events
        and not password_events
        and not privilege_events
    ):
        print("No matching security events were found in the first 100000 events.")


if __name__ == "__main__":
    main()