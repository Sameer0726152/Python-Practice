names = ["sam", "rahul", "nihar", "abhijeet"]
bill = [50, 60, 40, 55]
i = 0
for i, amt in zip(names, bill):
    print(f"{i} paid : {amt} rupees")