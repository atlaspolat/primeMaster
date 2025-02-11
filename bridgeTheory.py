from matplotlib import pyplot as plt

from PrimeGenerator import PrimeSourceManager


def ruleFunction(*variables: int) -> int:
    return sum(*variables)


if __name__ == '__main__':

    targetValue = 2500

    primeSource = PrimeSourceManager.PrimeSourceManager()
    primeSource.readPrimesLessThan(targetValue)
    S1 = []
    S2 = [x for x in range(8, targetValue, 2)]
    Kernel = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    S1 = Kernel[:]

    for i in S1:
        for j in S1:
            remove_number = i + j
            if remove_number in S2:
                S2.remove(remove_number)

    while len(S2) > 0:
        new_number = S2[0] - S1[0]
        S1.append(new_number)

        for x in S1:
            if x == S1[-1]:
                break
            remove_number = x + S1[-1]
            if remove_number in S2:
                S2.remove(remove_number)


    def isDifferenceSix(index: int) -> bool:
        if S1[index] - S1[index - 1] == 6:
            return 1
        else:
            return 0


    def isPrime(num: int) -> bool:
        return 1 if primeSource.isPrime(num) else 0


    print(S1)
    print(S2)

    colors1 = map(isDifferenceSix, list(range(1, len(S1))))

    colors1 = [0] + list(colors1)

    colors2 = map(isPrime, S1)

    colors2 = list(colors2)

    numberOfVertices = list(range(1, len(S1) + 1))

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ax1.scatter(S1, numberOfVertices, c=colors1, cmap='summer', edgecolors='black', s=20, alpha=0.75)
    ax2.scatter(S1, numberOfVertices, c=colors2, cmap='summer', edgecolors='black', s=20, alpha=0.75)

    ax1.set_xlabel('number')
    ax1.set_ylabel('total bridge vertices')


    ax1.grid(True)



    ax2.set_xlabel('number')
    ax2.set_ylabel('total bridge vertices')



    ax2.grid(True)


    plt.style.use("Solarize_Light2")

    plt.tight_layout()

    plt.show()
