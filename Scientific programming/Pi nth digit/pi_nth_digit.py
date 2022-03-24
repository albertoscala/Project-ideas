from math import floor


def pi_nth_digits(n):
    pi = []

    # Declaring the list by floor((10 * n) / 3) + 1
    size = floor((10 * n) / 3) + 1
    list = []

    # Fill the list with 2 and multiply them by 10
    for i in range(size):
        list.append(2 * 10)

    nines = 0
    predigit = 0

    # For every N
    for j in range(1, size+1):
        q = 0

        for i in range(size, 1, -1):
            b = list[i - 1] + (q * i)
            list[i - 1] = q % (2 * i - 1)
            q = b // (2 * i - 1)

        list[0] = q % 10
        q = q // 10

        if q == 9:
            nines += 1
        elif q == 10:
            pi.append(predigit + 1)

            for k in range(nines):
                pi.append(0)

            predigit = 0
            nines = 0
        else:
            pi.append(predigit)

            if nines != 0:
                for k in range(nines):
                    pi.append(9)

                nines = 0

    pi.append(predigit)

    return pi


'''
def pi_nth_digits(n):

    # Declaring PI as a decimal for a better precision
    temp = Fraction(0)

    # Using the formula for N+2 times to obtain PI
    for i in range(n):
        div = (((-1) ** i) * (factorial(6 * i)) * (13591409 + 545140134 * i))
        den = ((factorial(3 * i)) * (factorial(i) ** 3) * (640320 ** (3 * i)))
        temp += Fraction(div, den)

    # Multiplying for the costants
    temp *= Fraction(12, Fraction(640320 ** 1.5))

    # Reversing the PI
    temp = Fraction(temp.denominator, temp.numerator)

    temp = temp * (10 ** n)

    pi = str(round(temp.numerator // temp.denominator))

    # Returning PI's to Nth digit
    return pi[0] + '.' + pi[1:]
'''

# -------------TESTS-------------


def test_5_digits():
    assert pi_nth_digits(5) == 3.14159


def test_10_digits():
    assert pi_nth_digits(10) == 3.1415926536


def test_20_digits():
    assert pi_nth_digits(20) == 3.14159265358979323846


def test_50_digits():
    assert pi_nth_digits(50) == 3.14159265358979323846264338327950288419716939937511


def test_100_digits():
    assert pi_nth_digits(100) == 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170680


# --------------END--------------


if __name__ == '__main__':
    n = int(input('Insert n length of the digits: '))
    print(pi_nth_digits(n))
