from math import factorial
from decimal import Decimal, getcontext


def pi_nth_digits(n):
    # Setting the floating accuracy to N
    getcontext().prec = n + 1

    # Declaring PI as a decimal for a better precision
    pi = Decimal()

    # Using the formula for N+2 times to obtain PI
    for i in range(n):
        div = Decimal(((-1) ** i) * (factorial(6 * i)) * (13591409 + 545140134 * i))
        den = Decimal((factorial(3 * i)) * (factorial(i) ** 3) * (640320 ** (3 * i)))
        pi += div / den

    # Adding the costants
    pi = pi * 12 / Decimal(640320 ** 1.5)

    # Reversing the PI
    pi = 1 / pi

    # Returning PI's to Nth digit
    return pi


if __name__ == '__main__':
    n = int(input('Insert n length of the digits: '))
    print(pi_nth_digits(n))
