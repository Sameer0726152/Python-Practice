value = 18
if (remainder := value % 5):
    print(f"Value is not divisible by 5, remainder is {remainder}")
sizes = ["small", "medium", "large"]
if(size := input("Enter your preferred size\n")).lower() in sizes:
    print(f"Chosen size is: {size}")
else:
    print(f"Wrong input")