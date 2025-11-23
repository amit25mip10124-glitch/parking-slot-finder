def parking_slot_finder():
    while True:
        try:
            total_slots = int(input("Enter total number of parking slots (positive integer): "))
            if total_slots <= 0:
                print("Please enter a positive integer for slots.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    available_slots = total_slots
    print(f"Parking slot system initialized with {total_slots} total slots.")

    while True:
        print("\nCurrent available slots:", available_slots)
        print("Choose an action:")
        print("1. Car Enter")
        print("2. Car Exit")
        print("3. Exit Program")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            if available_slots > 0:
                available_slots -= 1
                print("Car entered. Updated available slots:", available_slots)
            else:
                print("Parking is full! No slots available.")

        elif choice == '2':
            if available_slots < total_slots:
                available_slots += 1
                print("Car exited. Updated available slots:", available_slots)
            else:
                print("Parking lot is already empty. No cars to exit.")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    parking_slot_finder()
