# Race condition is fixed
from threading import Lock
import concurrent.futures


class IncrementedVariable:
    '''Class for locked variable incrementation '''
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def locked_update(self, arg):
        for _ in range(arg):
            with self._lock:
                self.value += 1


def main():
    variable = IncrementedVariable()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = []
        for i in range(5):
            threads.append(executor.submit(variable.locked_update, arg=1000000))

    print("----------------------", variable.value)


main()
