from PrimeGenerator import PrimeSourceManager
from PrimeGenerator import CustomArray
from matplotlib import pyplot as plt


def main():
    target = 1000000

    manager = PrimeSourceManager.PrimeSourceManager()
    manager.readPrimesLessThan(target)
    number_size = manager.PrimeList.sizeWithoutZero




    manager.readPrimesLessThan(2 * target)






    for x in range(2, number_size):
        okay = False
        if manager.PrimeList.arr[x] == 0:
            continue



        double_number = 2 * manager.PrimeList.arr[x]

        for subx in range(1, x):
            test_number = int(double_number - manager.PrimeList.arr[subx])
            # print(
            #     f'{x} prime = {manager.PrimeList.arr[x]}  {double_number} = {test_number} + {int(double_number - test_number)}')
            if manager.isPrime(test_number):
                print(
                    f'{x} prime = {manager.PrimeList.arr[x]}  {double_number} = {test_number} + {int(double_number - test_number)}')
                okay = True

                break

        if not okay:
            print(f'{manager.PrimeList.arr[x]} does not satisfy')




if __name__ == '__main__':
    main()
