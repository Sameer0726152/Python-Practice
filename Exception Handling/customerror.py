def brew(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Flavor not available")
brew("mint")