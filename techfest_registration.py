def main():
    print("Welcome to SMIT TechFest!")
    print("Event organized by <Your Name> of APPDAET <Your Section>\n")

    while True:
        try:
            num_participants = int(input("How many participants will register? "))
            if num_participants <= 0:
                print("Invalid number of participants. Please enter a positive number.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    participants = []

    for i in range(num_participants):
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")
        participants.append({"name": name, "track": track})

    print("\nRegistered Participants:")
    for idx, p in enumerate(participants, start=1):
        print(f"{idx}. {p['name']} - {p['track']}")

    tracks = {p["track"] for p in participants}
    if len(tracks) < 2:
        print("\nNot enough variety in tracks.")
    else:
        print("\nTracks offered in this event:")
        print(", ".join(tracks))

    seen_names = set()
    duplicates = set()
    for p in participants:
        if p["name"] in seen_names:
            duplicates.add(p["name"])
        seen_names.add(p["name"])

    if duplicates:
        for name in duplicates:
            print(f"\nDuplicate name found: {name}")
    else:
        print("\nNo duplicate names.")

    summary = {}
    for p in participants:
        track = p["track"]
        summary[track] = summary.get(track, 0) + 1

    print("\nParticipants per track:")
    for track, count in summary.items():
        print(f"{track}: {count}")


if __name__ == "__main__":
    main()