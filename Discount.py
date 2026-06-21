users = [
    {"id" : 1, "name" : "Sameer", "total" : 200, "coupon" : "P90"},
    {"id" : 2, "name" : "Rahul", "total" : 300, "coupon" : "MP40"},
    {"id" : 3, "name" : "Nihar", "total" : 250, "coupon" : "M24"},
    {"id" : 4, "name" : "Abhijeet", "total" : 150, "coupon" : "M416"}
]

discount = {
    "P90" : (0, 100),
    "MP40" : (0.3, 20),
    "M24" : (0.4, 15),
    "M416" : (0.5, 0)
}

for user in users:
    percent, fixed = discount.get(user["coupon"], (0, 0))
    total_discount = user["total"] * percent + fixed
    final_bill = user["total"] - total_discount
    print(f"Customer {user['name']} paid a total amount of {final_bill} rupees and got a discount of {total_discount} rupees")