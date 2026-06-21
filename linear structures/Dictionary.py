Chai_order = dict(type = "Masala chai", size = "Large", Sugar = 2)
print(f"Chai order is: {Chai_order}")

Chai_recipe = {}
Chai_recipe["base"] = "water"
Chai_recipe["spice"] = "ginger"
print(f"chai_recipe is {Chai_recipe}")
print(f"Chai base is: {Chai_recipe["base"]}")

del Chai_recipe["base"]
print(f"chai_recipe is {Chai_recipe}")
print(f"order Keys are: {Chai_order.keys()}")
print(f"order Values are: {Chai_order.values()}")
print(f"order Pairs are: {Chai_order.items()}")

Customer_note = Chai_order.get("Note", "No Note given")
print(f"Customer note is: {Customer_note}")