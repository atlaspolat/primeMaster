from PrimeGenerator import CustomArray
from PrimeGenerator import FileDataManager
import numpy as np
from math import log, e, ceil
import time

import os


def time_test(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.perf_counter()
        result = original_function(*args, **kwargs)
        end = time.perf_counter()
        print(f'Finished in {round(end - start, 3)} second(s)')
        return result

    return wrapper_function


class PrimeSourceManager(object):

    def __init__(self):
        self.primeReaderAppender = open(os.path.join(os.path.dirname(__file__), "primes.txt"),  'a+')
        self.primeReaderAppender.seek(0, 0)
        self.dataFileObj = FileDataManager.FileData()

        self.PrimeList = CustomArray.CustomArray(size=1)

        self.lastReadPrime = 0
        self.__readPointer__ = 0

    ################################################################################
    # initialize the array again

    def initialize_array(self, size: int):
        self.PrimeList = CustomArray.CustomArray(size=size)

    ################################################################################
    # math functions

    @staticmethod
    def number_primes(num):
        return ceil((12 / 10) * (num * log(e, 2)) / log(num, 2))

    ################################################################################
    # wrapper functions
    @staticmethod
    def __set_pointer_for_reading(original_function):
        def wrapper_function(*args, **kwargs):
            self = args[0]
            self.setReadPointer()
            result = original_function(*args, **kwargs)
            self.saveReadPointer()
            return result

        return wrapper_function

    @staticmethod
    def __set_pointer_for_appending(original_function):
        def wrapper_function(*args, **kwargs):
            self = args[0]
            self.setAppendPointer()
            return original_function(*args, **kwargs)

        return wrapper_function

    ################################################################################
    # Operations for the pointer
    def saveReadPointer(self):
        self.__readPointer__ = self.primeReaderAppender.tell()

    def setReadPointer(self):
        self.primeReaderAppender.seek(self.__readPointer__, 0)

    def setAppendPointer(self):
        self.primeReaderAppender.seek(0, 2)

    ################################################################################
    # adding new prime(s)

    # @__set_pointer_for_appending
    # def addNewPrime(self, newNumber: int):
    #
    #     assert newNumber > self.PrimeList.arr[-1], "New prime is less than the last item."
    #
    #     self.primeReaderAppender.write(str(newNumber) + '\n')

    @__set_pointer_for_appending
    def addNewPrimes(self, newNumbers: np.array):

        number_new_primes = 0
        last_item = 0

        if newNumbers[0] == 0:
            print("No new prime found, increase the upper limit")
            return

        for newNumber in newNumbers:
            # assert newNumber > self.PrimeList.arr[-1], "New prime is less than the last item."
            if newNumber == 0:
                break
            else:
                self.primeReaderAppender.write(str(newNumber) + '\n')
                number_new_primes += 1
                last_item = newNumber

        self.dataFileObj.max_prime = int(last_item)
        self.dataFileObj.number_primes += number_new_primes
        self.dataFileObj.update_file_data()
        print("New primes added")

    ################################################################################
    # reading prime number(s)

    # @__set_pointer_for_reading
    # def readOnePrime(self) -> int:
    #
    #     line = int(self.primeReaderAppender.readline())
    #     self.PrimeList.append(line)
    #
    #     return line

    @__set_pointer_for_reading
    def readPrimesLessThan(self, upperLimit):
        assert upperLimit <= self.dataFileObj.max_prime, 'We do not have that many number of primes'

        array_size = PrimeSourceManager.number_primes(upperLimit) + 5
        old_array = self.PrimeList.arr.copy()
        old_size = self.PrimeList.sizeWithoutZero
        self.initialize_array(array_size)

        for x in old_array:
            if not x == 0:
                self.PrimeList.append(x)



        next_prime = int(self.primeReaderAppender.readline())

        array_size = 0

        while next_prime < upperLimit:
            self.PrimeList.append(next_prime)
            array_size += 1
            next_prime = int(self.primeReaderAppender.readline())

        self.PrimeList.append(next_prime)
        array_size += 1
        self.lastReadPrime = next_prime
        self.PrimeList.sizeWithoutZero = array_size + old_size

    def readAllPrimes(self):
        self.readPrimesLessThan(self.dataFileObj.max_prime)
        print("All primes read")


    ################################################################################
    # check if a particular prime exists

    def isPrime(self, _num):

        if _num in [2, 5]:
            return True

        if str(_num)[len(str(_num)) - 1] in ['0', '2', '4', '6', '8', '5']:
            return False

        if self.lastReadPrime < _num:
            self.readPrimesLessThan(_num)
            return self.lastReadPrime == _num

        else:
            _start = 0
            _end = self.PrimeList.sizeWithoutZero

            while _start <= _end:
                _mid = _start + (_end - _start) // 2

                if self.PrimeList.arr[_mid] > _num:
                    _end = _mid - 1
                elif self.PrimeList.arr[_mid] < _num:
                    _start = _mid + 1
                else:
                    return True

            return False

    ################################################################################
    # close the file

    def closeSource(self):
        self.primeReaderAppender.close()


####################################################################################
####################################################################################
####################################################################################

if __name__ == '__main__':
    print(os.path.join(os.path.dirname(__file__), 'ds'))
    print()
    manager = PrimeSourceManager()

    manager.readPrimesLessThan(200)

    print(manager.PrimeList)

    manager.readPrimesLessThan(400)

    print(manager.PrimeList)

    manager.readPrimesLessThan(600)

    print(manager.PrimeList)

    # print(manager.PrimeList.arr)
    # print(manager.PrimeList.arr.size)

    # print(manager.dataFileObj.max_prime)

    # manager.dataFileObj.max_prime = 3131
    #
    # manager.dataFileObj.updated_file_data()

    # a = np.array([93, 97])
    #
    # manager.addNewPrimes(a)

    manager.closeSource()
