import threading
import time

def area_tringle():
    triangle=[(3,4),(5,6),(6,8)]
    for b,h in triangle:
        area=0.5*b*h
        print("Area of tringle= ",area)
        time.sleep(1)

t2=threading.Thread(target=area_tringle)
t2.start()
t2.join()