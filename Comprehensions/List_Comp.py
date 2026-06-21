menu = [
    "Pizza",
    "Burger",
    "Pasta",
    "Salad",
    "Coffee"
]
idk2 = [item2 for item2 in menu if "S" in item2]
idk = [item for item in menu if item.startswith("P")]
print(f"{idk2}")
print(f"{idk}") 