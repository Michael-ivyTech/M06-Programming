import multiprocessing
import random
from datetime import datetime
import time


def whatTimeIsIt(num):
    randSec = random.random()
    time.sleep(randSec)
    print(f"I'm process {num}, and It's {datetime.now()}.")

if __name__ == "__main__":
    processes = []
    for n in range(3):
        p = multiprocessing.Process(target=whatTimeIsIt, args=(n,)) 
        p.start() 
        processes.append(p)
    p.join() 
    print("All processes have finished.")