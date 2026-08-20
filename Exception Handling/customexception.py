class OutofMilk(Exception):
    pass
class OutofSugar(Exception):
    pass
def makechai(milk, sugar):
    if milk == 0:
        raise OutofMilk("Missing milk")
    if sugar == 0:
        raise OutofSugar("Missing Sugar")
    print("Chai is ready")
makechai(2, 4)
makechai(0, 0)