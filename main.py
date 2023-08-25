class Flight:

    def __init__(self, p_id, start_time, priority):
        self.p_id = p_id
        self.start_time = start_time
        self.priority = priority

    def __repr__(self):
        return f"Flight({self.p_id}, {self.start_time}, {self.priority})"


def sort_by_p_id(flights):
    return sorted(flights, key=lambda flight: flight.p_id)


def sort_by_start_time(flights):
    return sorted(flights, key=lambda flight: flight.start_time)


def sort_by_priority(flights):
    return sorted(flights, key=lambda flight: flight.priority)


def main():

    flights = [
        Flight("P1", 100, "MID"),
        Flight("P23", 234, "MID"),
        Flight("P93", 189, "High"),
        Flight("P42", 9, "High"),
        Flight("P9", 7, "High"),
        Flight("P87", 23, "Low"),
    ]

    print("Choose sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        flights = sort_by_p_id(flights)
    elif choice == 2:
        flights = sort_by_start_time(flights)
    elif choice == 3:
        flights = sort_by_priority(flights)
    else:
        print("Invalid choice!")
        return

    print("Sorted flights:")
    for flight in flights:
        print(flight)


if __name__ == "__main__":
    main()