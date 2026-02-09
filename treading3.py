import threading
import time
def task():
    time.sleep(2)
    print("Thread finished")

t=threading.Thread(target=task)
t.start()
t.join()
print("Main finished")