def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
make_chai("ginger", "Cow", "Low") #positional args
make_chai(tea="masala", milk="bufffalo", sugar="Medium") #keywords 

def special_chai(*Ingredients, **extras): #kwargs
    print("Ingredients: ", Ingredients)
    print("extras: ", extras)

special_chai("water", "tea powder", sweerner="no", foam="yes" )