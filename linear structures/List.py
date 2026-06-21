Spice = ["ginger", "cardamom"]
Ingredients = ["water", "milk", "tea"]
chai = ["water", "milk"]

print(f"spices are: {Spice}")
print(f"spices are: {Ingredients}")
print(f"spices are: {chai}")

Spice.append("Clove")
print(f"spices are: {Spice}")
Ingredients.insert(2, "Sugar")
print(f"spices are: {Ingredients}")
chai.extend(Spice)
print(f"spices are: {chai}")

Base_chai = ["water", "milk"]
Flavor = ["ginger", "Cardamom"]
Finished_chai = Base_chai + Flavor
print(f"Finished product is: {Finished_chai}")

