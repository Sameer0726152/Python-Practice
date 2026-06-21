def update_order():
    chai_type = input("order is: ")
    print(f"Order before changing is: {chai_type}")
    def kitchen_order():
        nonlocal chai_type 
        chai_type = "Ginger"
    kitchen_order()
    print(f"Order after changing is: {chai_type}")

update_order()