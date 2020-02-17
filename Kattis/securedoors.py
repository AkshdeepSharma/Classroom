def checkIfPersonInBuilding(people_in_building, command, person):
    if command == "entry" and person not in people_in_building:
        people_in_building.add(person)
        return person + " entered", people_in_building
    if command == "entry" and person in people_in_building:
        return person + " entered (ANOMALY)", people_in_building
    if command == "exit" and person in people_in_building:
        people_in_building.discard(person)
        return person + " exited", people_in_building
    if command == "exit" and person not in people_in_building:
        return person + " exited (ANOMALY)", people_in_building


def main():
    length_of_log = int(input())
    people_in_building = set()
    for _ in range(length_of_log):
        command, person = input().split()
        ans, people_in_building = checkIfPersonInBuilding(
            people_in_building, command, person)
        print(ans)


if __name__ == "__main__":
    main()
