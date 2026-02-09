import threading
import time
def task():
    time.sleep(2)
    print("Thread runing")

t=threading.Thread(target=task)
t.start()
print("Main finished")
print("Main program running")