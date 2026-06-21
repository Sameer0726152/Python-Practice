def serve_chai():
    print("Welcome!")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield
stall = serve_chai()
next(stall)
stall.send("Masala Chai")
stall.send("Ginger Chai")