import threading
def task():
    print("Thread runing")

t=threading.Thread(target=task)
t.start()
print("Main program running")