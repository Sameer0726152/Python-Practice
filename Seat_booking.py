seat_type = input("Enter your preferred seat type (Sleeper/AC/General/Luxury)\n")
print(f"Preferred seat is: {seat_type}")
seat_type = seat_type.lower()
match seat_type:
    case "sleeper":
        print(f"No AC, comfortable")
    case "ac":
        print(f"AC is provided")
    case "general":
        print(f"General compartment")
    case "luxury":
        print(f"The best seat available")
    case _:
        print(f"Invalid input")
