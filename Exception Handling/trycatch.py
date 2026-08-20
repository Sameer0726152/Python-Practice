def serve(flavor):
    try:
        print("Preparing chai")
        if(flavor == "unknown"):
            raise ValueError("Flavor not mentioned")
    except ValueError as e:
        print("Error: ", e)
    else:
        print("Served Chai")
    finally:
        print("Next Please")

serve("masala")
serve("unknown")