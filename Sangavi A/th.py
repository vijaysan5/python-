import threading
import time

# threading

""" def work():
    for i in range(3):
        print("Working...", i)
        time.sleep(1)

t = threading.Thread(target=work)
t.start()   # start thread
t.join()    # wait for completion

print("Main program finished") """


# multi threading
""" def task(name):
    for i in range(3):
        print(name, "running", i)
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t1.join()

t2.start()
t2.join() """


# thread synchronization 
""" counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)  """

# lock
""" counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()     # Lock
        counter += 1
        lock.release()     # Unlock

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)  """