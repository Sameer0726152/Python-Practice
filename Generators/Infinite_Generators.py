def Infinite_Chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1
refill = Infinite_Chai()
for _ in range(5):
    print(next(refill))