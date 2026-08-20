class notavailable(Exception): pass
def bill(flavor, cups):
    menu = {"Masala" : 20, "Ginger" : 30}
    try:
        if flavor not in menu:
            raise notavailable("Flavor not available")
        if not isinstance(cups, int):
            raise TypeError("Mention cups in integer")
        total = menu[flavor] * cups
        print(f"Your bill is {total} rupees")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thanks for visiting")
bill("Masala", 2)
bill("Elaichi", 3)
bill("Ginger", "Three")