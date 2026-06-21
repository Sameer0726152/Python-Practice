chai_types = ["masala", "ginger", "lemon", "green", "ginger"]

wanted_chai = list(filter(lambda chai: chai != "ginger", chai_types))

print(wanted_chai)