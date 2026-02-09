import threading
import time

def sort_number():
    data=[9,3,7,11,5]
    print("Original list",data)
    data.sort()
    time.sleep(1)
    print("sorted list is",data)

t3=threading.Thread(target=sort_number)
t3.start()
t3.join()