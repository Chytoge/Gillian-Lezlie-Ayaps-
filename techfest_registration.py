print("Welcome to SMIT TechFest!")
print("Event organized by Your_Name_Here of APPDAET Your_Section")

num_participants = int(input("How many participants will register? "))

if num_participants <= 0:
    print("Invalid number of participants.")
else:
    # Move on to the next task later
    pass

participants = []

for i in range(num_participants):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participant = {"name": name, "track": track}
    participants.append(participant)

print("\nRegistered Participants:")
for idx, p in enumerate(participants, 1):
    print(f"{idx}. {p['name']} - {p['track']}")

    unique_tracks = set(p['track'] for p in participants)

    if len(unique_tracks) < 2:
        print("\nNot enough variety in tracks.")
    else:
        print("\nTracks offered in this event: " + ", ".join(unique_tracks))