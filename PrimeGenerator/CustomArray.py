import numpy as np


class CustomArray:
    def __init__(self, size: int):
        self.arr = np.zeros((size,), dtype='uint64')
        self.pos = 0
        self.sizeWithoutZero = 0

    def append(self, element):
        try:
            self.arr[self.pos] = element
        except IndexError:
            print("The number of elemenths exceeded the capacity of the array")
            return IndexError
        self.pos += 1

    def __repr__(self):
        return repr(self.arr[:self.pos])