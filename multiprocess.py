import multiprocessing
import random
import time

def whatTimeIsIt():
    now = time.time()
    print(f"It's {time.ctime(now)}")

if __name__ == "__main__":
    for n in range(3):
        randSec = random.random()
        time.sleep(randSec)
        p = multiprocessing.Process(target=whatTimeIsIt)
        p.start()
        p.join()