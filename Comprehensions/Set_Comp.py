category = [
    "masala", "ginger", "garlic", "ginger", "masala"
]

idk = {chai for chai in category} #set comp doesnt have repeated values
idk2 = [chai2 for chai2 in category]  #List comp has repeated values
print(f"{idk}")
print(f"{idk2}")

idk3 = {
    "masala" : ['clove', 'garlic', 'masala'],
    "ginger" : ['masala', 'cardemom', 'ginger'],
    "spicy" : ['chili', 'pepper', 'clove']
}
idk4 = {spice for ingredient in idk3.values() for spice in ingredient}
print(f"{idk4}")