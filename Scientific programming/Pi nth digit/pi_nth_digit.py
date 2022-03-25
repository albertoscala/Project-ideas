# Implementing spigot algorithm for calculating PI digits
# https://www.cut-the-knot.org/Curriculum/Algorithms/SpigotForPi.shtml

from math import floor


def round(n, len):
    r = int(str(n)[len+1])

    if r >= 5:
        return int(str(n)[:len+1]) + 1

    return int(str(n)[:len+1])


def pi_nth_digits(n):

    pi = ''

    # Declaring the list by floor((10 * n) / 3) + 1
    size = floor((10 * (n+11)) / 3) + 1
    list = []

    # Fill the list with 2 and multiply them by 10
    for i in range(size):
        list.append(2)

    nines = 0
    predigit = 0

    # For every N
    for j in range(1, n+12):
        q = 0

        # Multiply by 10 every element
        # Put the list into the regular form
        for i in range(size, 0, -1):
            b = 10 * list[i - 1] + (q * i)
            list[i - 1] = b % ((2 * i) - 1)
            q = int(b / ((2 * i) - 1))


        # Get the next predigit
        list[0] = q % 10
        q = int(q / 10)

        # Adjust the predigits
        if q == 9:
            nines += 1
        elif q == 10:
            pi += str(predigit + 1)

            for k in range(nines):
                pi += str(0)

            predigit = 0
            nines = 0

        else:
            pi += str(predigit)
            predigit = q

            if nines != 0:
                for k in range(nines):
                    pi += str(9)

                nines = 0

    # Final correction
    pi += str(predigit)

    # Quick correction for the rounding and turning it into a string
    pi = str(round(int(pi[1:]), n))

    # Final Pi result
    return pi[0] + '.' + pi[1:]


# -------------TESTS-------------


def test_5_digits():
    assert pi_nth_digits(5) == '3.14159'


def test_10_digits():
    assert pi_nth_digits(10) == '3.1415926536'


def test_20_digits():
    assert pi_nth_digits(20) == '3.14159265358979323846'


def test_50_digits():
    assert pi_nth_digits(50) == '3.14159265358979323846264338327950288419716939937511'


def test_100_digits():
    assert pi_nth_digits(100) == '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170680'


# --------------END--------------


if __name__ == '__main__':
    n = int(input('Insert n length of the digits: '))
    print(pi_nth_digits(n))
