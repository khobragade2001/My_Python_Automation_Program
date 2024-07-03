import time
from threading import Thread

class A(Thread):
    def run (self):
        for i in range(5):
            print("Ashish")
            time.sleep(1)

class B(Thread):
    def run (self):
        for i in range(5):
            print("Khobragade")
            time.sleep(1)

t1 = A()
t1.start()
t2 = B()
t2.start()
