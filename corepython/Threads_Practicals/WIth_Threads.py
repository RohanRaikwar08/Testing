import threading


def hello():
    for i in range(1,9):
        print("Rohan:",i)

def hii():
    for i in range(1,9):
        print("Mohan:",i)


t1 = threading.Thread(target = hello)
t2 = threading.Thread(target = hii)


t1.start()
t2.start()