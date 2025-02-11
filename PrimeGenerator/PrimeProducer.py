from PrimeGenerator import PrimeSourceManager
from PrimeGenerator import CustomArray
import numpy as np
from math import isqrt, e, log, ceil
import time


def time_test(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.perf_counter()
        result = original_function(*args, **kwargs)
        end = time.perf_counter()
        print(f'Finished in {round(end - start, 3)} second(s)')
        return result

    return wrapper_function


# def sieve_number_list(is_prime_list: np.ndarray, sieve_prime, target_value, the_last_known_prime):
#     division = int(the_last_known_prime // sieve_prime)
#
#     print("Sieve with", sieve_prime)
#     for siever in range((division + 1) * sieve_prime, target_value + 1, sieve_prime):
#         is_prime_list[siever - the_last_known_prime - 1] = False
#         print(str(siever), "got knocked out")
#
#     print(is_prime_list)
########################################################################################################################
########################################################################################################################
########################################################################################################################


class PrimeProducer(object):

    # def __init__(self):
    def __init__(self, sourceManager):
        self.sourceManager = sourceManager

        # self.sourceManager = PrimeSourceManager.PrimeSourceManager()  # don't forget to turn this into an argument
        self.sourceManager.readAllPrimes()
        self.PrimeList = self.sourceManager.PrimeList
        self.the_last_known_prime = self.sourceManager.dataFileObj.max_prime

    @time_test
    def produce_more_prime(self, targetValue):
        assert targetValue < self.sourceManager.dataFileObj.max_prime ** 2, 'Not in our range at the moment'

        if targetValue <= self.the_last_known_prime:
            print("We already have found the numbers less than this target.")
            return


########################################################################################################################
        new_primes_array_size = PrimeProducer.number_primes(targetValue) - PrimeProducer.number_primes(
            self.the_last_known_prime)
        new_arr_size = targetValue - self.sourceManager.dataFileObj.max_prime

        is_prime_arr = np.full((new_arr_size,), True, dtype="bool")
        new_primes_array = CustomArray.CustomArray(new_primes_array_size)

        print(new_primes_array_size)
        print(new_arr_size)
        print(is_prime_arr.size)
        print(self.PrimeList.arr)

        sieve_number_index = 0
        sieve_number = int(self.PrimeList.arr[sieve_number_index])

        # process_list = []

        while sieve_number <= isqrt(targetValue):
            # p = multiprocessing.Process(target=sieve_number_list,
            #                             args=[is_prime_arr, sieve_number, targetValue, self.the_last_known_prime])
            # p.start()
            # process_list.append(p)

            division = int(self.the_last_known_prime // sieve_number)

            for i in range((division + 1) * sieve_number, targetValue + 1, sieve_number):
                is_prime_arr[i - self.the_last_known_prime - 1] = False

            sieve_number_index += 1
            sieve_number = int(self.PrimeList.arr[sieve_number_index])

        # print("Sieving tasks have been given")
        # # for process in process_list:
        # #     process.join()
        #
        # print("Sieves got together")

        for i in range(0, is_prime_arr.size):
            if is_prime_arr[i]:
                result = new_primes_array.append(i + self.the_last_known_prime + 1)
                if result == IndexError:
                    print("We fall short on the number of primes")
                    break

        self.sourceManager.addNewPrimes(new_primes_array.arr)



    @staticmethod
    def number_primes(num):
        return ceil((12 / 10) * (num * log(e, 2)) / log(num, 2))


if __name__ == '__main__':
    producer = PrimeProducer()
    producer.produce_more_prime(200000000)
    # print(PrimeProducer.number_primes(50000000))
