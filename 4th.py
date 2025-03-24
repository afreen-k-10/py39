total_passengers = 0

for stop in range(1, 6):
    passengers = int(input(f"Enter the number of passengers boarding at stop {stop}: "))
    if passengers >= 0:
        total_passengers += passengers
    else:
        print("Invalid input! Passengers cannot be negative.")

print(f"\nTotal number of passengers at the end: {total_passengers}")