from multiprocessing import Process, current_process
import time
def count():
    count = 0
    print(f"Counting {current_process().name} started")
    for _ in range(100_000_000):
        count += 1
    print(f"Counting {current_process().name} Ended")
if __name__ == "__main__":
    p1 = Process(target = count, name = "1")
    p2 = Process(target = count, name = "2")
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f"Total time was {end - start:.2f} seconds")