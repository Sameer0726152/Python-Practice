#single return

def chai_wala():
    return "Chai is ready sir"
saying = chai_wala()
print(saying)

#multiple return
def another_chai_wala():
    return "Masala chai", "Sameer"
chai_type, customer = another_chai_wala()
print(f"{chai_type} for {customer}")

#early return
def chai_status(status):
    if status == 0:
        return "Chai not available"
    return "Here is your chai"
idk = chai_status(0)
idk2 = chai_status(4)
print(idk)
print(idk2)