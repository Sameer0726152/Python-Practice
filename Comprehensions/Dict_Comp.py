tea_price_inr = {
    "Masala" : 40,
    "Ginger" : 50,
    "Green" : 60
}

tea_price_dollar = {tea:price / 90 for tea, price in tea_price_inr.items()};
print(f"{tea_price_dollar.values()}")