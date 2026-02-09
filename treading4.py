import threading
import time
def calculate_squre():
    numbers=[2,3,4,5]
    for n in numbers:
        print("Squre of",n,"=",n*n)
        time.sleep(1)
t1=threading.Thread(target=calculate_squre)
t1.start()
t1.join()