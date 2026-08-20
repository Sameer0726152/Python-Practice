import threading
import time
def take_order():
    for i in range(1, 4):
        print(f"Order for #{i}")
        time.sleep(2)
def brew_chai():
    for i in range(1, 4):
        print(f"Chai for #{i}")
        time.sleep(3)
order_thread = threading.Thread(target = take_order)
brew_thread = threading.Thread(target = brew_chai)
order_thread.start()
brew_thread.start()
order_thread.join()
brew_thread.join()
print("All tasks done")