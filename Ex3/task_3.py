# Race condition is fixed
from threading import Thread, Lock
from multiprocessing.dummy import Pool as ThreadPool 

a = 0
lock = Lock()
def function(arg):
    global a # Please don't use global variables
    for _ in range(arg):
        with lock: 
            a += 1

def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(100,)) #Please use thread pool 1000000
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]

    print("----------------------", a)  

main()