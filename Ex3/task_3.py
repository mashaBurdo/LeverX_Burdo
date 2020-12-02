# Race condition is fixed
from threading import Lock
import concurrent.futures


class IncrementedVariable:
    '''Class for locked variable incrementation'''
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def locked_update(self, increment_count):
        for _ in range(increment_count):
            with self._lock:
                self.value += 1


def main():
    variable = IncrementedVariable()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = []
        for i in range(5):
            threads.append(executor.submit(variable.locked_update, increment_count=1000000))

    print("----------------------", variable.value)


main()
