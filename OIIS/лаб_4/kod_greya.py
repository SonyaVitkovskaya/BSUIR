from math import sin, pi
import numpy as np


def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2)
    n ^= (n >> 1)

    return bin(n)[2:]


def gray_to_binary(n):
    """Convert Gray codeword to binary and return it."""
    n = int(n, 2)

    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask

    return bin(n)[2:]


def rad(n, x):
    """Return Rademacher function"""
    if round(sin(2 ** n * pi * x), 6) > 0:
        return 1
    else:
        return -1


def wal_had(x):
    """Return Walsh Hadamard transform result"""
    x = np.asarray(x, dtype=float)
    n = x.shape[0]

    H = np.ones((n, n))
    i = 1
    while i < n:
        for j in range(i):
            for k in range(i):
                H[j+i][k] = H[j][k]
                H[j][k+i] = H[j][k]
                H[j+i][k+i] = -(H[j][k])
        i += i

    return np.dot(x, H)/n


if __name__ == "__main__":
    src_bin = "10110"
    print("Бинарное представление: {}".format(src_bin))
    print("Код Грея: {}".format(binary_to_gray(src_bin)))
    print("Востановленное бинарное представление: {}".format(
        gray_to_binary(binary_to_gray(src_bin))))

    print("\nФункция Радемахера:")
    print("n = {}, x = {}: {}".format(0, 0.5, rad(0, 0.5)))
    print("n = {}, x = {}: {}".format(1, 0.5, rad(1, 0.5)))
    print("n = {}, x = {}: {}".format(1, 0.49, rad(1, 0.49)))
    print("n = {}, x = {}: {}".format(2, 0.5, rad(2, 0.5)))
    print("n = {}, x = {}: {}".format(2, 0.1, rad(2, 0.1)))

    print(
        "\nПреобразование Уолша-Адамара (1, 2, 0, 3): {}".format(wal_had([1, 2, 0, 3])))
