def calculate_bill():
    cups = int(input("Enter number of cups ordered\n"))
    amt = int(input("Enter the price of the tea ordered\n"))
    return cups * amt

print(f"Your total bill is: {calculate_bill()}")