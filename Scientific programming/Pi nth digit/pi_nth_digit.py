from math import factorial
from fractions import Fraction

def pi_nth_digits(n):

    sum = Fraction(0)
    i = 0
    c = 1

    while True:
        if i%2 == 0:
            sum += Fraction(1, c)
        else:
            sum -= Fraction(1, c)

        if c > 10 ** n:

            sum = sum * (10 ** n)
            pi = str(sum.numerator // sum.denominator)

            return pi[0] + '.' + pi[1:]

        i += 1
        c += 2


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
