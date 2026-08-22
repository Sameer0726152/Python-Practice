import threading
import time
from multiprocessing import Process, current_process, Queue
def count1():
    count = 0
    print(f"Counting {threading.current_thread().name} started")
    for _ in range(100_000_000):
        count += 1
    print(f"Counting {threading.current_thread().name} Ended")

def count2():
    count = 0
    print(f"Counting {current_process().name} started")
    for _ in range(100_000_000):
        count += 1
    print(f"Counting {current_process().name} Ended")

def threading_time(queue):
    t1 = threading.Thread(target = count1, name = "Barista-1")
    t2 = threading.Thread(target = count1, name = "Barista-2")
    start1 = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end1 = time.perf_counter()
    queue.put(end1 - start1)

def multiprocessing_time(queue):
    p1 = Process(target = count2, name = "Process-1")
    p2 = Process(target = count2, name = "Process-2")
    start2 = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end2 = time.perf_counter()
    queue.put(end2 - start2)
if __name__ == "__main__":
    queue1 = Queue()
    queue2 = Queue()
    thread = Process(target = threading_time, args = (queue1,))
    process = Process(target = multiprocessing_time, args = (queue2,))
    thread.start()
    process.start()
    thread_time = queue1.get()
    process_time = queue2.get()
    thread.join()
    process.join()
    print(f"Threading time was {thread_time:.2f} \nMultiProcessing time was {process_time:.2f}")