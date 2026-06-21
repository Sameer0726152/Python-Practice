def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Oolong Chai"
    yield "Matcha Chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)     

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai"
    except:
        print("Stall closed")

stall = chai_stall()
print(next(stall))
stall.close