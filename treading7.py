import _thread
import time

def task1():
    print("Task 1 is running")

def task2():
    print("Task 2 is runing")

_thread.start_new_thread(task1,())
_thread.start_new_thread(task2,())

time.sleep(1)
print("Main program ends")