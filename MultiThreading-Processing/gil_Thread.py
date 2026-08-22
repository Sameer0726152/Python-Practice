import threading
import time
def brew():
    print(f"{threading.current_thread().name} Started")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} Ended")
t1 = threading.Thread(target = brew, name = "Barista-1")
t2 = threading.Thread(target = brew, name = "Barista-2")
t3 = threading.Thread(target = brew, name = "Barista-3")
start = time.time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end = time.time()
print(f"Total time was {end - start:.2f} seconds")