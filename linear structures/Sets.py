Essential_spices = {"cardamom", "Ginger", "Cloves"}
Optional_spices = {"Cinnamon", "Black pepper", "Ginger"}
All_spices = Essential_spices | Optional_spices
print(f"All spices are: {All_spices}")

Common_spices = Essential_spices & Optional_spices
print(f"Common spices are: {Common_spices}")

Only_in_essntial = Essential_spices - Optional_spices
print(f"Only Essential spices are: {Only_in_essntial}")

print(f"Is clove in essential spices?: {'Cloves' in Essential_spices}")