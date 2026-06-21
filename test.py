balance = 5000
n = int(input("Enter number of headphones\n"))
headphones = {}

for i in range(1, n+1):
    price = int(input(f"Enter price of headphone {i}: "))
    headphones[i] = price

print("Headphones prices are")
for key, value in headphones.items():
    print(f"headphones {key} : {value}")
cheapest_key = min(headphones, key=headphones.get)
cheapest = headphones[cheapest_key]

if (balance >= cheapest):
    balance -= cheapest
    print(f"Transaction successful")
    print(f"headphone number {cheapest_key} bought")
    print(f"Remaining balance is: {balance}")
else:
    print("transaction failed")
    print(f"Remaining balance is: {balance}")



