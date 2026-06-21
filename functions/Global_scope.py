chai_type = "masala"
print(f"Order before changing is: {chai_type}")
def update_order():
    def kitchen_order():
        global chai_type 
        chai_type = "Ginger"
    kitchen_order()
    print(f"Order after changing is: {chai_type}")
update_order()