from multiprocessing import Process
import time
def brew(name):
    print(f"Start of {name} brewing")
    time.sleep(2)
    print(f"End of {name} brewing")
if __name__ == "__main__":
    chai_makers = [Process(target = brew, args = (f"Chai maker #{i + 1}",)) for i in range(3)]
    for p in chai_makers:
        p.start()
    for p in chai_makers:
        p.join()
    print("All Processes end")